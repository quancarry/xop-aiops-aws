import random

def generate_access_log():
    # Simulate access log format
    ip_address = f"192.168.0.{random.randint(1, 255)}"  # Random IP address
    timestamp = datetime.utcnow().strftime("%d/%b/%Y:%H:%M:%S +0000")
    method = random.choice(["GET", "POST", "PUT", "DELETE"])
    url = random.choice(["/index.html", "/home", "/about", "/contact", "/product                                                                                                                         s"])
    status_code = random.choice([200, 404, 500, 301])
    response_size = random.randint(100, 5000)

    # Simulate an access log entry
    access_log = f'{ip_address} - - [{timestamp}] "{method} {url} HTTP/1.1" {sta                                                                                                                         tus_code} {response_size}'

    return access_log

def main():
    # Get the access log entry
    access_log = generate_access_log()

    # Send to Kinesis
    kinesis = boto3.client("kinesis", region_name="us-east-1")
    kinesis.put_record(
        StreamName="my-fargate-output",
        Data=access_log,
        PartitionKey="access-log"
    )

    print(f"Sent to Kinesis: {access_log}")

if __name__ == "__main__":
    main()
