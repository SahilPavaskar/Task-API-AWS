import json
import os
import uuid
from datetime import datetime, timezone

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))

    title = body.get("title")
    description = body.get("description", "")
    status = body.get("status", "pending")

    if not title:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "title is required"})
        }

    now = datetime.now(timezone.utc).isoformat()

    item = {
        "taskId": str(uuid.uuid4()),
        "title": title,
        "description": description,
        "status": status,
        "createdAt": now,
        "updatedAt": now
    }

    table.put_item(Item=item)

    return {
        "statusCode": 201,
        "body": json.dumps(item)
    }
