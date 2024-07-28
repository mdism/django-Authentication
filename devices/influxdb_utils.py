# myapp/influxdb_utils.py
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# Configure InfluxDB connection
influxdb_url = "http://192.168.0.199:8086"
influxdb_token = "your-influxdb-token"
influxdb_org = "your-org"
influxdb_bucket = "iot_data"

client = InfluxDBClient(url=influxdb_url, token=influxdb_token, org=influxdb_org)
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

def write_data(device_id, data):
    point = Point("device_data").tag("device_id", device_id)
    for key, value in data.items():
        point = point.field(key, value)
    write_api.write(bucket=influxdb_bucket, record=point)

def query_data(query):
    return query_api.query(org=influxdb_org, query=query)
