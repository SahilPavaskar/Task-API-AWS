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

    response = table.get_item(Key={"taskId": task_id})
    item = response.get("Item")

    if not item:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "task not found"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }
