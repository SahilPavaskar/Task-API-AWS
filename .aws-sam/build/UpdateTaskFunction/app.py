import json
import os
from datetime import datetime, timezone

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    task_id = event.get("pathParameters", {}).get("taskId")
    body = json.loads(event.get("body", "{}"))

    title = body.get("title")
    description = body.get("description")
    status = body.get("status")

    if not task_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "taskId is required"})
        }

    existing = table.get_item(Key={"taskId": task_id}).get("Item")

    if not existing:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "task not found"})
        }

    updated_item = {
        "taskId": task_id,
        "title": title if title is not None else existing.get("title"),
        "description": description if description is not None else existing.get("description", ""),
        "status": status if status is not None else existing.get("status", "pending"),
        "createdAt": existing.get("createdAt"),
        "updatedAt": datetime.now(timezone.utc).isoformat()
    }

    table.put_item(Item=updated_item)

    return {
        "statusCode": 200,
        "body": json.dumps(updated_item)
    }
