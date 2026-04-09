import json
import os

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    task_id = event.get("pathParameters", {}).get("taskId")

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

    table.delete_item(Key={"taskId": task_id})

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "task deleted", "taskId": task_id})
    }
