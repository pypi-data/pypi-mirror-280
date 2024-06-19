from pathlib import Path

from dotenv import load_dotenv
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
from datetime import datetime

from datacontract.data_contract import DataContract

# logging.basicConfig(level=logging.INFO, force=True)

datacontract = "fixtures/dataframe/datacontract.yaml"

load_dotenv(override=True)


# TODO this test conflicts with the test_test_kafka.py test
def _test_test_dataframe(tmp_path: Path):
    spark = _create_spark_session(tmp_dir=str(tmp_path))
    _prepare_dataframe(spark)
    data_contract = DataContract(
        data_contract_file=datacontract,
        spark=spark,
    )

    run = data_contract.test()

    print(run.pretty())
    assert run.result == "passed"
    assert all(check.result == "passed" for check in run.checks)
    spark.stop()


def _prepare_dataframe(spark):
    schema = StructType(
        [
            StructField("field_one", StringType(), nullable=False),
            StructField("field_two", IntegerType(), nullable=True),
            StructField("field_three", TimestampType(), nullable=True),
        ]
    )
    data = [
        Row(
            field_one="AB-123-CD",
            field_two=15,
            field_three=datetime.strptime("2024-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
        ),
        Row(
            field_one="XY-456-ZZ",
            field_two=20,
            field_three=datetime.strptime("2024-02-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
        ),
    ]
    # Create DataFrame
    df = spark.createDataFrame(data, schema=schema)
    # Create temporary view
    # Name must match the model name in the data contract
    df.createOrReplaceTempView("my_table")


def _create_spark_session(tmp_dir: str) -> SparkSession:
    """Create and configure a Spark session."""
    spark = (
        SparkSession.builder.appName("datacontract-dataframe-unittest")
        .config("spark.sql.warehouse.dir", f"{tmp_dir}/spark-warehouse")
        .config("spark.streaming.stopGracefullyOnShutdown", "true")
        .config(
            "spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,org.apache.spark:spark-avro_2.12:3.5.0",
        )
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    print(f"Using PySpark version {spark.version}")
    return spark
