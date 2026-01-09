import time
from datetime import datetime
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    use_ssl=False,
)

index_name = "script-logs"

counter = 1

while True:
    doc = {
        "@timestamp": datetime.utcnow().isoformat(),
        "level": "INFO",
        "message": f"Log message #{counter}",
        "service": "demo-script"
    }

    response = client.index(
        index=index_name,
        body=doc
    )

    print(f"Sent log {counter}, result={response['result']}")

    counter += 1
    time.sleep(1)
