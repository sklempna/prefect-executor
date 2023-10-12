from minio import Minio
from prefect import flow
from datetime import datetime, timezone
import os

@flow(log_prints=True)
def get_documents(after_ts="1900-01-01 00:00:00"):

    after_datetime = datetime.strptime(after_ts, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)

    client = Minio(
        "minio:9000",
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY"),
        secure=False
    )

    for bucket in client.list_buckets():
        print(bucket.name)

        objects = [o for o in client.list_objects(bucket.name) if o.last_modified >= after_datetime]
        for object in objects:
            print(f"+- {object.object_name} - last modified: {object.last_modified}")

if __name__ == "__main__":
    get_documents.serve(name="get-documents")