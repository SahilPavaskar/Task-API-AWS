# Serverless Task API on AWS

![AWS SAM](https://img.shields.io/badge/AWS%20SAM-Infrastructure%20as%20Code-orange)
![API Gateway](https://img.shields.io/badge/API%20Gateway-REST%20API-blue)
![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-Serverless-yellow)
![DynamoDB](https://img.shields.io/badge/DynamoDB-NoSQL-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

A serverless CRUD API built with **AWS SAM**, **Amazon API Gateway**, **AWS Lambda**, and **Amazon DynamoDB**.

This project was built to gain practical experience designing, deploying, and testing a backend application on AWS using **serverless services** and **infrastructure as code**.

---

## Project Snapshot

- Built a fully functional **serverless REST API**
- Implemented full **CRUD operations** for task management
- Used **separate Lambda functions per route**
- Deployed infrastructure with **AWS SAM / CloudFormation**
- Stored application data in **DynamoDB**
- Verified live endpoints using `curl`

---

## Architecture

```text
Client -> API Gateway -> Lambda -> DynamoDB
```

### AWS Services Used

- **Amazon API Gateway** — exposes HTTP endpoints and routes requests
- **AWS Lambda** — runs stateless backend logic
- **Amazon DynamoDB** — stores task data
- **AWS SAM** — defines and deploys infrastructure as code

---

## Features

- Create a task
- List all tasks
- Get a task by ID
- Update a task
- Delete a task
- Deployable with AWS SAM
- CloudFormation output for API base URL

---

## Live API Base URL

```text
https://rlgiw9bu6e.execute-api.us-east-1.amazonaws.com/Prod
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{taskId}` | Retrieve a single task |
| PUT | `/tasks/{taskId}` | Update a task |
| DELETE | `/tasks/{taskId}` | Delete a task |

---

## Sample Task Object

```json
{
  "taskId": "8744a6f7-f7f2-4585-9dfa-df0a0e74a0c4",
  "title": "My first task",
  "description": "Testing my serverless API",
  "status": "pending",
  "createdAt": "2026-04-09T02:39:07.876753+00:00",
  "updatedAt": "2026-04-09T02:39:07.876753+00:00"
}
```

---

## Project Structure

```text
task-api-aws/
├── README.md
├── template.yaml
├── samconfig.toml
├── events/
├── docs/
└── src/
    ├── createTask/
    │   └── app.py
    ├── listTasks/
    │   └── app.py
    ├── getTask/
    │   └── app.py
    ├── updateTask/
    │   └── app.py
    └── deleteTask/
        └── app.py
```

---

## Tech Stack

- **AWS SAM**
- **Amazon API Gateway**
- **AWS Lambda**
- **Amazon DynamoDB**
- **Python 3.12**
- **AWS CLI**
- **Git**

---

## How It Works

1. The client sends an HTTP request to API Gateway.
2. API Gateway matches the request to a route.
3. The route invokes the mapped Lambda function.
4. The Lambda function performs the required operation in DynamoDB.
5. A JSON response is returned to the client.

This project demonstrates the core AWS serverless pattern for backend application development.

---

## DynamoDB Design

This version uses a simple table design:

- **Table name:** `TasksTable`
- **Partition key:** `taskId`

This schema keeps the MVP easy to understand while supporting the complete CRUD flow.

---

## Setup and Prerequisites

Make sure the following are installed and configured:

- AWS CLI
- AWS SAM CLI
- Python 3.12
- Git
- AWS account with appropriate permissions

### Verify installation

```bash
git --version
python3 --version
aws --version
sam --version
aws sts get-caller-identity
```

---

## Deployment

### Build

```bash
sam build
```

### First deployment

```bash
sam deploy --guided
```

### Later deployments

```bash
sam deploy
```

---

## Retrieve CloudFormation Output

```bash
aws cloudformation describe-stacks \
  --stack-name task-api-aws \
  --query "Stacks[0].Outputs" \
  --output table
```

---

## Usage Examples

### Create a task

```bash
curl -X POST https://rlgiw9bu6e.execute-api.us-east-1.amazonaws.com/Prod/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Sample task",
    "description": "Created from API request",
    "status": "pending"
  }'
```

### List all tasks

```bash
curl https://rlgiw9bu6e.execute-api.us-east-1.amazonaws.com/Prod/tasks
```

### Get a task by ID

```bash
curl https://rlgiw9bu6e.execute-api.us-east-1.amazonaws.com/Prod/tasks/<taskId>
```

### Update a task

```bash
curl -X PUT https://rlgiw9bu6e.execute-api.us-east-1.amazonaws.com/Prod/tasks/<taskId> \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated task",
    "description": "Updated through PUT",
    "status": "completed"
  }'
```

### Delete a task

```bash
curl -X DELETE https://rlgiw9bu6e.execute-api.us-east-1.amazonaws.com/Prod/tasks/<taskId>
```

---

## Example Responses

### Create / Get / Update

```json
{
  "taskId": "12345678-abcd-1234-abcd-1234567890ab",
  "title": "Updated task",
  "description": "Updated through PUT",
  "status": "completed",
  "createdAt": "2026-04-09T02:39:07.876753+00:00",
  "updatedAt": "2026-04-09T03:07:36.135897+00:00"
}
```

### Delete

```json
{
  "message": "task deleted",
  "taskId": "12345678-abcd-1234-abcd-1234567890ab"
}
```

---

## Key Takeaways

This project demonstrates:

- Building a backend using **AWS-native serverless services**
- Designing **RESTful API routes**
- Writing **Lambda-based application logic** in Python
- Using **DynamoDB** as a managed NoSQL persistence layer
- Managing infrastructure with **AWS SAM / CloudFormation**
- Deploying, testing, and iterating on a cloud project end to end

---

## Current Limitations

This is the MVP version and does not yet include:

- Authentication / authorization
- Per-user task ownership
- Pagination
- Request schema validation
- Automated tests
- File attachments
- Frontend integration
- Monitoring dashboards and alarms

---

## Future Improvements

Possible next upgrades:

- Add **Amazon Cognito** for authentication
- Add **user-based task isolation**
- Add **input validation**
- Add **structured error handling**
- Add **Amazon S3** for attachments
- Add **EventBridge** for reminders
- Add **DynamoDB Streams** for event-driven workflows
- Add **unit and integration tests**
- Add an **architecture diagram** in `/docs`

---

## Local Developer Commands

```bash
sam validate
sam build
sam deploy
sam list endpoints --stack-name task-api-aws
sam delete
```

---

## Author

Built as a hands-on AWS serverless learning project.
