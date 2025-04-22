import os
import requests
import csv
import boto3
import io
import json

# Env vars (use task definition or Secrets Manager)
DT_API_URL = "https://mySampleEnv.live.dynatrace.com/api/v2/metrics"
DT_API_TOKEN = os.getenv("DT_API_TOKEN")  # secure this
KINESIS_STREAM = os.getenv("KINESIS_STREAM", "my-dynatrace-stream")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# Headers and parameters
headers = {
    "Authorization": f"Api-Token {DT_API_TOKEN}",
    "Accept": "text/csv; header=present"
}
params = {
    "fields": "displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions",
    "metricSelector": "builtin:host.cpu.(idle,usage,load)"
}

def send_to_kinesis(record, partition_key):
    kinesis = boto3.client("kinesis", region_name=AWS_REGION)
    response = kinesis.put_record(
        StreamName=KINESIS_STREAM,
        Data=json.dumps(record),
        PartitionKey=partition_key
    )
    return response

def fetch_and_stream():
    response = requests.get(DT_API_URL, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return

    csv_text = response.text
    reader = csv.DictReader(io.StringIO(csv_text))

    for row in reader:
        # Optional: clean/transform the row before sending
        print(f"Sending: {row['metricId'] if 'metricId' in row else row}")
        send_to_kinesis(record=row, partition_key=row.get("metricId", "default"))

if __name__ == "__main__":
    fetch_and_stream()
