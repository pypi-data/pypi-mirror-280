import logging
from typing import Dict, List

from quollio_core.profilers.lineage import (
    gen_column_lineage_payload,
    gen_table_lineage_payload,
    parse_databricks_table_lineage,
)
from quollio_core.profilers.stats import gen_table_stats_payload
from quollio_core.repository import databricks, qdc

logger = logging.getLogger(__name__)


def databricks_table_level_lineage(
    conn: databricks.DatabricksConnectionConfig,
    endpoint: str,
    qdc_client: qdc.QDCExternalAPIClient,
    tenant_id: str,
    dbt_table_name: str = "quollio_lineage_table_level",
) -> None:
    with databricks.DatabricksQueryExecutor(config=conn) as databricks_executor:
        results = databricks_executor.get_query_results(
            query=f"""
            SELECT
                DOWNSTREAM_TABLE_NAME,
                UPSTREAM_TABLES
            FROM {conn.catalog}.{conn.schema}.{dbt_table_name}
            """
        )
        tables = parse_databricks_table_lineage(results)
        update_table_lineage_inputs = gen_table_lineage_payload(
            tenant_id=tenant_id,
            endpoint=endpoint,
            tables=tables,
        )

        req_count = 0
        for update_table_lineage_input in update_table_lineage_inputs:
            logger.info(
                "Generating table lineage. downstream: %s -> %s-> %s",
                update_table_lineage_input.downstream_database_name,
                update_table_lineage_input.downstream_schema_name,
                update_table_lineage_input.downstream_table_name,
            )
            status_code = qdc_client.update_lineage_by_id(
                global_id=update_table_lineage_input.downstream_global_id,
                payload=update_table_lineage_input.upstreams.as_dict(),
            )
            if status_code == 200:
                req_count += 1
        logger.info("Generating table lineage is finished. %s lineages are ingested.", req_count)
    return


def databricks_column_level_lineage(
    conn: databricks.DatabricksConnectionConfig,
    endpoint: str,
    qdc_client: qdc.QDCExternalAPIClient,
    tenant_id: str,
    dbt_table_name: str = "quollio_lineage_column_level",
) -> None:
    with databricks.DatabricksQueryExecutor(config=conn) as databricks_executor:
        results = databricks_executor.get_query_results(
            query=f"""
            SELECT
                *
            FROM
                {conn.catalog}.{conn.schema}.{dbt_table_name}
            """
        )

    update_column_lineage_inputs = gen_column_lineage_payload(
        tenant_id=tenant_id,
        endpoint=endpoint,
        columns=results,
    )

    req_count = 0
    for update_column_lineage_input in update_column_lineage_inputs:
        logger.info(
            "Generating column lineage. downstream: %s -> %s -> %s -> %s",
            update_column_lineage_input.downstream_database_name,
            update_column_lineage_input.downstream_schema_name,
            update_column_lineage_input.downstream_table_name,
            update_column_lineage_input.downstream_column_name,
        )
        status_code = qdc_client.update_lineage_by_id(
            global_id=update_column_lineage_input.downstream_global_id,
            payload=update_column_lineage_input.upstreams.as_dict(),
        )
        if status_code == 200:
            req_count += 1
    logger.info(
        "Generating column lineage is finished. %s lineages are ingested.",
        req_count,
    )
    return


def _get_monitoring_tables(
    conn: databricks.DatabricksConnectionConfig, monitoring_table_suffix: str = "_profile_metrics"
) -> List[Dict[str, str]]:
    tables = []
    query = f"""
        SELECT
            table_catalog,
            table_schema,
            table_name,
            CONCAT(table_catalog, '.', table_schema, '.', table_name) AS table_fqdn
        FROM
            system.information_schema.tables
        WHERE
            table_name LIKE "%{monitoring_table_suffix}"
            AND table_name NOT LIKE ('quollio_%')
        """
    with databricks.DatabricksQueryExecutor(config=conn) as databricks_executor:
        tables = databricks_executor.get_query_results(query)
    if len(tables) > 0:
        logger.info("Found %s monitoring tables.", len(tables))
        return tables
    else:
        logger.info("No monitoring tables found.")
        return []


def _get_column_stats(
    conn: databricks.DatabricksConnectionConfig, monitoring_table_suffix: str = "_profile_metrics"
) -> List[Dict[str, str]]:
    tables = _get_monitoring_tables(conn, monitoring_table_suffix)
    if not tables:
        return []
    stats = []
    for table in tables:
        monitored_table = table["table_fqdn"].removesuffix("_profile_metrics")
        monitored_table = monitored_table.split(".")
        if len(monitored_table) != 3:
            raise ValueError(f"Invalid table name: {table['table_fqdn']}")
        with databricks.DatabricksQueryExecutor(config=conn) as databricks_executor:
            query = """
                    WITH profile_record_history AS (
                        SELECT
                            COLUMN_NAME
                            , distinct_count as CARDINALITY
                            , MAX as MAX_VALUE
                            , MIN as MIN_VALUE
                            , AVG as AVG_VALUE
                            , MEDIAN as MEDIAN_VALUE
                            , STDDEV as STDDEV_VALUE
                            , NUM_NULLS as NULL_COUNT
                            , get(frequent_items, 0).item AS MODE_VALUE
                            , row_number() over(partition by column_name order by window desc) rownum
                        FROM
                            {monitoring_table}
                        WHERE
                            column_name not in (':table')
                    )
                    SELECT
                        "{monitored_table_catalog}" as DB_NAME
                        , "{monitored_table_schema}" as SCHEMA_NAME
                        , "{monitored_table_name}" as TABLE_NAME
                        , COLUMN_NAME
                        , CARDINALITY
                        , MAX_VALUE
                        , MIN_VALUE
                        , AVG_VALUE
                        , MEDIAN_VALUE
                        , STDDEV_VALUE
                        , NULL_COUNT
                        , MODE_VALUE
                    FROM
                        profile_record_history
                    WHERE
                        rownum = 1
                """.format(
                monitoring_table=table["table_fqdn"],
                monitored_table_catalog=monitored_table[0],
                monitored_table_schema=monitored_table[1],
                monitored_table_name=monitored_table[2],
            )
            logger.debug(f"The following sql will be fetched to retrieve stats values. {query}")
            stats.append(databricks_executor.get_query_results(query))
    return stats


def databricks_column_stats(
    conn: databricks.DatabricksConnectionConfig,
    endpoint: str,
    qdc_client: qdc.QDCExternalAPIClient,
    tenant_id: str,
    monitoring_table_suffix: str = "_profile_metrics",
) -> None:
    table_stats = _get_column_stats(conn, monitoring_table_suffix)
    for table in table_stats:
        logger.debug("Table %s will be aggregated.", table)
        stats = gen_table_stats_payload(tenant_id=tenant_id, endpoint=endpoint, stats=table)
        for stat in stats:
            status_code = qdc_client.update_stats_by_id(
                global_id=stat.global_id,
                payload=stat.body.as_dict(),
            )
            if status_code == 200:
                logger.info("Stats for %s is successfully ingested.", stat.global_id)
    return
