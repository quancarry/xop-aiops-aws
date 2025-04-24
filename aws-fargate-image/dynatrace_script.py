import boto3
import requests
from datetime import datetime

def get_dynatrace_metrics():
    # Dynatrace API setup
    url = "https://mySampleEnv.live.dynatrace.com/api/v2/metrics"
    headers = {
        "Authorization": "Api-Token dt0c01.abc123.abcdefjhij1234567890",
        "Accept": "text/csv; header=present"
    }
    params = {
        "fields": "displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions",
        "metricSelector": "builtin:host.cpu.(idle,usage,load)"
    }

    # Perform GET request
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        print("Dynatrace data retrieved successfully.")
        return response.text  # CSV format
    else:
        raise Exception(f"Failed to retrieve Dynatrace metrics: {response.status_code} - {response.text}")

def main():
    # Get Dynatrace metrics data
    metrics_data = get_dynatrace_metrics()

    # Send to AWS Kinesis
    kinesis = boto3.client("kinesis", region_name="us-east-1")
    kinesis.put_record(
        StreamName="my-fargate-output",
        Data=metrics_data,
        PartitionKey="dynatrace-metrics"
    )

    print("Sent Dynatrace metrics to Kinesis.")

if __name__ == "__main__":
    main()
