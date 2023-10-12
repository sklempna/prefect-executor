from minio import Minio
from io import StringIO
import pandas as pd

client = Minio(
    "localhost:9000",
    access_key="",
    secret_key="",
    secure=False
)
t = client.get_object("testbucket", "example.csv")
s = str(t.data, "utf-8")
f = StringIO(s)
print("bla")