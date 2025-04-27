import functions_framework
from google.cloud import bigquery

# Method 1 : coverting into ndjosn and process it
@functions_framework.cloud_event
def gcs_to_bq_load_func(cloud_event):
    data = cloud_event.data
    bucket = data["bucket"] # dictionary
    print(type(data))
    object_name = data["name"]
    print(bucket)
    print(object_name)

    if object_name.startswith("$") and object_name.endswith(".json"):
        print("Load this data into big query table")
        # schema definition
        schema=[
                bigquery.SchemaField("CustomerID", "INT64"),
                bigquery.SchemaField("FirstName", "STRING"),
                bigquery.SchemaField("LastName", "STRING"),
                bigquery.SchemaField("Email", "STRING"),
                bigquery.SchemaField("Phone", "STRING")
            ]
        # bigquery loadjob config
        # calling api
        # we can put it in try and except block
        # json to bq load

        # Construct a BigQuery client object.
        client = bigquery.Client(project = "rare-tome-458105-n0")

        # TODO(developer): Set table_id to the ID of the table to create.
        table_id = "rare-tome-458105-n0.cloud_functions_dataset.use_case_one"

        job_config = bigquery.LoadJobConfig(
                    schema = schema,
                    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        )
        uri = f"gs://{bucket}/{object_name}"

        load_job = client.load_table_from_uri(
        uri,
        table_id,
        location="US",  # Must match the destination dataset location.
        job_config=job_config,
        )  # Make an API request.

        load_job.result()  # Waits for the job to complete.

        destination_table = client.get_table(table_id)
        print("Loaded {} rows.".format(destination_table.num_rows))
        
    else:
        print("This file is not supported to load into big query")


