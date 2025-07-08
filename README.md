# AWS EC2 Automated Snapshot Backup

This project contains an AWS Lambda function to:
- ✅ Automatically create a daily snapshot of a given EC2 EBS volume.
- 🗑️ Automatically delete snapshots older than 3 days.

## 🔧 Lambda Function Details

- **Volume ID:** `vol-0XXXXXXXXXXXX`
- **Retention Period:** 3 days
- **Language:** Python 3.12
- **Trigger:** Scheduled daily using EventBridge (`rate(1 day)`)

## 📦 Setup Steps

1. Create the Lambda function in AWS Console.
2. Paste the contents of `lambda_function.py` into the function editor.
3. Assign it an IAM role with:
   - `AmazonEC2FullAccess`
   - `CloudWatchLogsFullAccess`
4. Create an EventBridge Rule:
   - Schedule: `rate(1 day)`
   - Target: your Lambda function

## 📁 Files

- `lambda_function.py`: The automation script
