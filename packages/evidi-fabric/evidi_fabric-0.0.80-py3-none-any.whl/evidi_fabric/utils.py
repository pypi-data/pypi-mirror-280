from datetime import datetime
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, expr, lit, date_format, to_timestamp, concat_ws
from pyspark.sql.types import TimestampType
from pyspark.sql import Row


def get_merge_condition(
    cols: list[str],
    dtypes: dict[str, str] | None = None,
    source_alias: str | None = None,
    target_alias: str | None = None,
) -> expr:
    """
    Generates the merge condition for the merge operation in spark
    :param key_cols: List of columns that are used as keys for the merge operation
    :param dtypes: Dictionary of column names and their data types (can be found using dict(df.dtypes))
    :param source_alias: Alias of the source dataframe
    :param target_alias: Alias of the target dataframe
    :return: The merge condition as a spark expression
    """
    if (source_alias and not target_alias) or (target_alias and not source_alias):
        raise ValueError("Both source_alias and target_alias must either be specified or empty not a mixture")

    use_alias = source_alias is not None
    if use_alias:
        if dtypes:
            conditions = []
            for col in cols:
                dtype = dtypes[col]
                if dtype == "string":
                    conditions.append(f"COALESCE({source_alias}.{col},'') = COALESCE({target_alias}.{col},'')")
                elif dtype == "bigint":
                    conditions.append(f"COALESCE({source_alias}.{col},-1) = COALESCE({target_alias}.{col},-1)")
                elif dtype[:7] == "decimal":
                    conditions.append(f"COALESCE({source_alias}.{col},-1.0) = COALESCE({target_alias}.{col},-1.0)")
                elif dtype == "timestamp":
                    conditions.append(
                        f"COALESCE({source_alias}.{col},'1970-01-01 00:00:00') = COALESCE({target_alias}.{col},'1970-01-01 00:00:00')"
                    )
                elif dtype == "double":
                    conditions.append(f"COALESCE({source_alias}.{col},-1.0) = COALESCE({target_alias}.{col},-1.0)")
                elif dtype == "int":
                    conditions.append(f"COALESCE({source_alias}.{col},-1) = COALESCE({target_alias}.{col},-1)")
                elif dtype == "date":
                    conditions.append(
                        f"COALESCE({source_alias}.{col},'1970-01-01') = COALESCE({target_alias}.{col},'1970-01-01')"
                    )
                else:
                    raise ValueError(f"Unsupported data type: {dtype} for column: {col}")

            return expr(" AND ".join(conditions))
        else:
            return expr(" AND ".join([f"{source_alias}.{col} = {target_alias}.{col}" for col in cols]))
    else:
        return expr(" AND ".join(cols))


def _get_df_rows_to_be_overwritten(
    df_source: DataFrame, df_target: DataFrame, overwrite_cols: list[str], ids: list[str]
) -> DataFrame:
    select_expr = [f"source.{col}" for col in overwrite_cols] + [
        f"target.{col}" for col in df_target.columns if col not in overwrite_cols
    ]
    where_clause = " OR ".join([f"source.{col} != target.{col}" for col in overwrite_cols])

    dtypes = dict(df_target.dtypes)
    merge_condition = get_merge_condition(cols=ids, dtypes=dtypes, source_alias="source", target_alias="target")
    df_rows_to_be_overwritten = (
        df_target.alias("target")
        .join(df_source.alias("source"), on=merge_condition, how="left")
        .filter(where_clause)
        .selectExpr(*select_expr)
    )
    return df_rows_to_be_overwritten


def add_concatenated_key(df: DataFrame, cols: list[str], key_col_name: str) -> DataFrame:
    """
    Adds a concatenated key to the dataframe
    :param df: The dataframe
    :param cols: The columns that are to be concatenated
    :param key_col_name: The name of the new key column
    :return: The dataframe with the new key column
    """
    select_cols = [key_col_name] + [c for c in df.columns if c != key_col_name]

    # Process columns, casting TimestampType to string with full timestamp format
    processed_cols = [
        date_format(col(c), "yyyyMMddHH'T'mmssSSS").alias(c)
        if df.schema[c].dataType == TimestampType()
        else col(c).cast("string")
        for c in cols
    ]

    # Add the concatenated key column
    df = df.withColumn(key_col_name, concat_ws("#", *processed_cols)).select(*select_cols)

    return df


def _validate_input(
    df: DataFrame, ids_tracked: list[str], cols_to_drop: list[str] = [], overwrite_cols: list[str] = []
) -> None:
    """
    Validates the input dataframe
    :param df: The dataframe
    :param cols: The columns that are to be validated
    """
    if cols_to_drop is None:
        cols_to_drop = []

    if overwrite_cols is None:
        overwrite_cols = []

    cols = df.columns

    illegal_cols_to_drop = [col for col in cols_to_drop if col in ids_tracked]
    if illegal_cols_to_drop:
        raise ValueError(
            f"The columns: {illegal_cols_to_drop} cannot be dropped as they are part of the tracked columns or ids columns"
        )

    reserved_col_names = ["valid_from" "valid_to" "valid_from_date_key" "valid_to_date_key" "IsDeleted"]

    illegal_cols = [col for col in reserved_col_names if col in cols]
    if illegal_cols:
        illegal_cols_str = ", ".join(illegal_cols)
        raise ValueError(f"The columns: {illegal_cols_str} are reserved and cannot be used in the dataframe")

    if any([col for col in overwrite_cols if col in ids_tracked]):
        impossible_cols = [col for col in overwrite_cols if col in ids_tracked]
        impossible_cols_str = ", ".join(impossible_cols)
        raise ValueError(f"The columns: {impossible_cols_str} cannot be tracked and overwritten at the same time!")


def get_scd2_updates(
    df_source: DataFrame,
    df_target: DataFrame,
    ids: list[str],
    tracked_cols: list[str],
    key_col_name: str,
    is_current_col: str = "is_current",
    current_datetime: datetime = datetime.now(),
    cols_to_drop: list[str] = [],
) -> DataFrame:
    """
    Generates the updates for SCD2 type 2 updates
    :param df_source: The source dataframe
    :param df_target: The target dataframe
    :param ids: The columns that are used as keys for the merge operation
    :param tracked_cols: The columns that are tracked for changes
    :param is_current_col: The column that specifies if a row is the current row
    :param current_datetime: The current datetime
    :return: The updated and new rows in a dataframe
    """
    keys = ids + tracked_cols + ["valid_from"]
    ids_tracked = ids + tracked_cols

    _validate_input(df_source, ids_tracked, cols_to_drop)

    df_source = add_default_scd2_cols_to_source(
        df_source, key_col_name, keys, ids_tracked, current_datetime, is_current_col
    )
    df_target_current = df_target.filter(
        (col(is_current_col) == True) & (col("IsDeleted") == False)
    )  # Only update current rows

    dtypes = dict(df_source.dtypes)
    merge_condition_ids_tracked = get_merge_condition(
        cols=ids_tracked, dtypes=dtypes, source_alias="source", target_alias="target"
    )
    df_new_and_updated_rows = (
        df_source.alias("source")
        .join(df_target_current.alias("target"), on=merge_condition_ids_tracked, how="left_anti")
        .selectExpr("source.*")
    )

    # Get old rows from gold, which is getting changed - based on the sales_key
    merge_condition_ids = get_merge_condition(cols=ids, dtypes=dtypes, source_alias="source", target_alias="target")
    df_existing_rows_target = (
        df_target_current.alias("target")
        .join(df_new_and_updated_rows.alias("source"), on=merge_condition_ids, how="inner")
        .selectExpr("target.*")
        .withColumn(is_current_col, lit(False))
        .withColumn("valid_to", lit(current_datetime))
        .withColumn("valid_to_date_key", date_format(lit(current_datetime), "yyyyMMdd"))
    )

    df_deleted_rows = (
        df_target.alias("target")
        .filter(col("IsDeleted") == False)  # Only deletes that have not already been deleted
        .join(df_source.alias("source"), on=merge_condition_ids, how="left_anti")
        .selectExpr("target.*")
        .withColumn(is_current_col, lit(False))
        .withColumn("valid_to", lit(current_datetime))
        .withColumn("valid_to_date_key", date_format(lit(current_datetime), "yyyyMMdd"))
        .withColumn("IsDeleted", lit(True))
    )

    df_scd2 = df_existing_rows_target.unionByName(df_new_and_updated_rows, allowMissingColumns=True).unionByName(
        df_deleted_rows, allowMissingColumns=True
    )

    # df_scd2 = add_concatenated_key(df_scd2, keys, key_col_name)
    df_scd2 = df_scd2.drop(*cols_to_drop) if cols_to_drop else df_scd2
    merge_condition = get_merge_condition(cols=ids_tracked, dtypes=dtypes, source_alias="source", target_alias="target")
    return df_scd2, merge_condition


def _update_df_scd2_with_overwritten_rows(
    df_source: DataFrame,
    df_target: DataFrame,
    df_scd2: DataFrame,
    ids: list[str],
    tracked_cols: list[str],
    overwrite_cols: list[str],
) -> DataFrame:
    """
    Updates the SCD2 dataframe with the rows that are to be overwritten. It does so be first updating the existing df_scd2 with the new values and then adding the rows from the target that currently are not a part of df_scd2
    :parmamdf_source: The source dataframe
    :param df_target: The target dataframe
    :param df_scd2: The SCD2 dataframe
    :param ids: The columns that are used as keys for the merge operation
    :param overwrite_cols: The columns that are to be overwritten
    :return: The updated SCD2 dataframe
    """
    keys = ids + tracked_cols + ["valid_from"]
    cols = df_scd2.columns
    select_expr = [f"source.{col}" for col in overwrite_cols] + [
        f"scd2.{col}" for col in df_scd2.columns if col not in overwrite_cols
    ]

    dtypes = dict(df_scd2.dtypes)

    df_rows_to_be_overwritten = _get_df_rows_to_be_overwritten(df_source, df_target, overwrite_cols, ids)

    merge_condition_keys = get_merge_condition(cols=keys, dtypes=dtypes, source_alias="scd2", target_alias="overwrite")
    merge_condition_ids = get_merge_condition(cols=ids, dtypes=dtypes, source_alias="scd2", target_alias="source")
    df_scd2_updated = (
        df_scd2.alias("scd2")
        .join(
            df_source.alias("source"),  # source will always have the latest data
            on=merge_condition_ids,
            how="inner",
        )
        .selectExpr(select_expr)
        .unionByName(
            df_rows_to_be_overwritten.alias("overwrite")
            .join(
                df_scd2.alias("scd2"),
                on=merge_condition_keys,
                how="leftanti",
            )
            .selectExpr("overwrite.*"),
            allowMissingColumns=True,
        )
        .unionByName(df_scd2.filter(col("IsDeleted") == True), allowMissingColumns=True)
        .select(*cols)
    )

    merge_condition = get_merge_condition(cols=keys, dtypes=dtypes, source_alias="source", target_alias="target")
    return df_scd2_updated, merge_condition


def add_default_scd2_cols_to_source(
    df_source: DataFrame,
    key_col_name: str,
    key_cols: list[str],
    id_cols: list[str],
    current_datetime: datetime = datetime.now(),
    is_current_col: str = "is_current",
) -> DataFrame:
    """
    Adds the default SCD2 columns to the source dataframe
    :param df_source: The source dataframe
    :param current_datetime: The current datetime
    :param is_current_col: The column that specifies if a row is the current row
    :return: The source dataframe with the default SCD2 columns added
    """
    select_cols = (
        [key_col_name]
        + list(df_source.columns)
        + [is_current_col, "valid_from", "valid_to", "valid_from_date_key", "valid_to_date_key", "IsDeleted"]
    )
    df = (
        df_source.withColumn(is_current_col, lit(True))
        .withColumn("valid_from", lit(current_datetime))
        .withColumn("valid_to", to_timestamp(lit("9999-12-31")))
        .withColumn("valid_from_date_key", date_format(lit(current_datetime), "yyyyMMdd"))
        .withColumn("valid_to_date_key", lit("99991231"))
        .withColumn("IsDeleted", lit(False))
    )
    df = add_concatenated_key(df, key_cols, key_col_name)
    df = df.select(*select_cols)
    return df


def get_scd2_updates_with_overwrite(
    df_source: DataFrame,
    df_target: DataFrame,
    ids: list[str],
    tracked_cols: list[str],
    key_col_name: str,
    overwrite_cols: list[str] | None = None,
    is_current_col: str = "is_current",
    current_datetime: datetime = datetime.now(),
    cols_to_drop: list[str] = [],
) -> DataFrame:
    """
    Generates the updates for SCD2 type 2 updates
    :param df_source: The source dataframe
    :param df_target: The target dataframe
    :param ids: The columns that are used as keys for the merge operation
    :param tracked_cols: The columns that are tracked for changes
    :param overwrite_cols: The columns that are to be overwritten
    :param is_current_col: The column that specifies if a row is the current row
    :param current_datetime: The current datetime
    :return: The updated and new rows in a dataframe

    Example of usage:
    df, merge_condition = get_scd2_updates_with_overwrite(df_source = df_salessilver,
                                                                                                              df_target = df_gold,
                                                                                                              ids = ["opportunityid"],
                                                                                                              tracked_cols = ["sales_status"],
                                                                                                              overwrite_cols = ["salesname", "salesnumber"],
                                                                                                              current_datetime=current_datetime)
    """
    ids_tracked = ids + tracked_cols
    _validate_input(df_source, ids_tracked, cols_to_drop, overwrite_cols)

    df_scd2, merge_condition = get_scd2_updates(
        df_source, df_target, ids, tracked_cols, key_col_name, is_current_col, current_datetime
    )
    if overwrite_cols:
        df_scd2, merge_condition = _update_df_scd2_with_overwritten_rows(
            df_source, df_target, df_scd2, ids, tracked_cols, overwrite_cols
        )

    df_scd2 = df_scd2.drop(*cols_to_drop) if cols_to_drop else df_scd2
    return df_scd2, merge_condition


def generate_unknown_row(
    df: DataFrame,
    default_int: int = -1,
    default_bigint: int = -1,
    default_str: str = "Unknown",
    default_datetime: datetime = datetime(1900, 1, 1),
    default_decimal: float = 0.0,
    default_timestamp: str = "1901-01-01 00:00:00",
    default_double: float = 0.0,
) -> DataFrame:
    """
    Generates a row with default values for the columns of a dataframe
    """
    spark = get_or_create_spark()
    dtypes = dict(df.dtypes)
    unknown_row = {}
    cols = df.columns
    for col in cols:
        dtype = dtypes[col]
        if dtype == "string":
            unknown_row[col] = default_str
        elif dtype == "int":
            unknown_row[col] = default_int
        elif dtype == "bigint":
            unknown_row[col] = default_bigint
        elif dtype == "datetime":
            unknown_row[col] = default_datetime
        elif dtype[:7] == "decimal":
            unknown_row[col] = default_decimal
        elif dtype == "timestamp":
            unknown_row[col] = default_timestamp
        elif dtype[:7] == "double":
            unknown_row[col] = default_double
        else:
            raise ValueError(f"Unsupported data type: {dtype} for column: {col}")

    unknown_row = Row(**unknown_row)
    df_extra = spark.createDataFrame([unknown_row], df.schema)
    return df_extra


def add_unknown_row_to_df(
    df: DataFrame,
    default_int: int = -1,
    default_bigint: int = -1,
    default_str: str = "Unknown",
    default_datetime: datetime = datetime(1900, 1, 1),
    default_decimal: float = 0.0,
    default_timestamp: str = "1901-01-01 00:00:00",
    default_double: float = 0.0,
) -> DataFrame:
    """
    Adds a row with default values for the columns of a dataframe
    """
    df_unknown_row = generate_unknown_row(
        df,
        default_int=default_int,
        default_bigint=default_bigint,
        default_str=default_str,
        default_datetime=default_datetime,
        default_decimal=default_decimal,
        default_timestamp=default_timestamp,
        default_double=default_double,
    )
    df = df_unknown_row.unionByName(df)
    return df


if __name__ == "__main__":
    from evidi_fabric.spark import get_or_create_spark
    from datetime import timedelta

    spark = get_or_create_spark()
    ids = ["opportunity_id"]
    tracked_cols = ["sales_status_t"]
    overwrite_cols = ["salesname_o", "salesnumber_o"]
    key_col_name = "opportunity_key"
    current_datetime = datetime.now()
    df_source = spark.createDataFrame(
        [
            ("1", "Anders", "001", "Lukket"),
            ("2", "must be overwritten", "002", "Åben"),
            ("3", "Claus", "003", "Lukket"),
        ],
        ["opportunity_id", "salesname_o", "salesnumber_o", "sales_status_t"],
    )
    df_target = spark.createDataFrame(
        [("1", "Anders", "001", "Åben"), ("2", "Bent", "002", "Åben")],
        ["opportunity_id", "salesname_o", "salesnumber_o", "sales_status_t"],
    )

    id_cols = ids  # + tracked_cols
    key_cols = ids + tracked_cols + ["valid_from"]
    df_target = add_default_scd2_cols_to_source(
        df_target,
        key_col_name,
        key_cols,
        id_cols,
        current_datetime=datetime.now() - timedelta(days=1),
        is_current_col="is_current",
    )

    df_delete = spark.createDataFrame(
        [
            (
                "3#Lukket#2024061908T2808802",
                "3",
                "Claus",
                "003",
                "Lukket",
                False,
                datetime(2024, 6, 18, 10, 28, 8, 802416),
                datetime(2024, 6, 19, 10, 28, 8, 802416),
                "20240618",
                "20240619",
                True,
            )
        ],
        [
            "opportunity_key",
            "opportunity_id",
            "salesname_o",
            "salesnumber_o",
            "sales_status_t",
            "is_current",
            "valid_from",
            "valid_to",
            "valid_from_date_key",
            "valid_to_date_key",
            "IsDeleted",
        ],
    )

    df_target = df_target.unionByName(df_delete)

    select_cols = [key_col_name] + [col for col in df_target.columns]

    df_target = add_concatenated_key(df_target, key_cols, key_col_name)
    cols_to_drop = []  # ["opportunity_id"]
    df_target = df_target.drop(*cols_to_drop)

    print(df_target.show())
    print(df_source.show())

    df_scd2, merge_condition = get_scd2_updates(
        df_source=df_source,
        df_target=df_target,
        ids=ids,
        tracked_cols=tracked_cols,
        key_col_name=key_col_name,
        is_current_col="is_current",
        current_datetime=current_datetime,
        cols_to_drop=cols_to_drop,
    )

    print(df_scd2.show())
    df_scd2_wo, merge_condition_wo = get_scd2_updates_with_overwrite(
        df_source=df_source,
        df_target=df_target,
        ids=ids,
        tracked_cols=tracked_cols,
        key_col_name=key_col_name,
        overwrite_cols=overwrite_cols,
        is_current_col="is_current",
        current_datetime=current_datetime,
        cols_to_drop=cols_to_drop,
    )

    print(df_scd2_wo.show())
    print("hertil!")
