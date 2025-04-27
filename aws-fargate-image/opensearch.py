import requests
import json
import boto3
from requests.auth import HTTPBasicAuth

# --- Configuration ---
OPENSEARCH_URL = "https://your-opensearch-domain:9200"
INDEX_NAME = "your-index-name"
USERNAME = "your-username"
PASSWORD = "your-password"
HOSTNAME_TO_SEARCH = "host.example.com"
KINESIS_STREAM_NAME = "your-kinesis-stream"
TIME_FIELD = "@timestamp"  # Adjust if your time field is different

# --- AWS Kinesis client ---
kinesis = boto3.client("kinesis")

# --- OpenSearch Query: Last 5 Minutes ---
query = {
    "query": {
        "bool": {
            "must": [
                {"match": {"host.keyword": HOSTNAME_TO_SEARCH}},
                {"range": {
                    TIME_FIELD: {
                        "gte": "now-5m",
                        "lte": "now"
                    }
                }}
            ]
        }
    },
    "size": 100  # Number of docs to return
}

# --- Generator to Fetch Rows ---
def fetch_opensearch_rows():
    search_url = f"{OPENSEARCH_URL}/{INDEX_NAME}/_search"
    response = requests.get(
        search_url,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        headers={"Content-Type": "application/json"},
        data=json.dumps(query)
    )

    if response.status_code == 200:
        results = response.json()
        for hit in results["hits"]["hits"]:
            yield hit["_source"]
    else:
        raise Exception(f"OpenSearch query failed: {response.status_code} {response.text}")

# --- Send Data to Kinesis ---
def send_to_kinesis(record):
    kinesis.put_record(
        StreamName=KINESIS_STREAM_NAME,
        Data=json.dumps(record),
        PartitionKey=record.get("host", "default")
    )

# --- Main Process ---
for row in fetch_opensearch_rows():
    send_to_kinesis(row)
    print(f"Sent to Kinesis: {row}")
