This project contains an AWS Lambda function to:

✅ Automatically create a daily snapshot of an EC2 EBS volume.

🗑️ Automatically delete snapshots older than 3 days.

🔧 Lambda Function Details

Volume ID: Replace with your EC2 instance's volume ID (e.g., vol-0xxxxxxxxxxxxxxx)

Retention Period: 3 days

Language: Python 3.12

Trigger: Scheduled daily using EventBridge (rate(1 day))

📦 Complete Setup Guide (A to Z)

✅ Step 1: Create EC2 Instance (via AWS Console or CloudShell)

Go to EC2 → Launch Instance

Name: DemoInstance

AMI: Amazon Linux 2023

Instance Type: t2.micro (Free Tier)

Storage: Default

Security Group: Allow HTTP or SSH

Launch the instance

✅ Step 2: Get the EBS Volume ID

Go to EC2 → Instances → Click your instance

Scroll to Block devices

Click on the Volume ID (e.g., vol-0abc123xyz)

Copy this Volume ID for the Lambda script

✅ Step 3: Create IAM Role for Lambda

Go to IAM → Roles → Create Role

Use case: Lambda

Attach permissions:

AmazonEC2FullAccess

CloudWatchLogsFullAccess

Role Name: LambdaEC2BackupRole

✅ Step 4: Create the Lambda Function

Go to Lambda → Create function

Name: EC2BackupAutomation

Runtime: Python 3.12

Execution role: Use existing → LambdaEC2BackupRole

Click Create

✅ Step 5: Add Backup Code

In Lambda → Replace default code with the contents of lambda_function.py

Replace volume_id = 'vol-xxxxxxxxxxxxxxx' with your real Volume ID

Click Deploy

✅ Step 6: Test the Function

Click Test → Create test event (default is fine)

Run the function manually

Go to EC2 → Snapshots → Confirm a snapshot is created

✅ Step 7: Schedule It with EventBridge

Go to EventBridge → Rules → Create Rule

Rule Type: Schedule

Pattern: rate(1 day)

Target: Lambda → EC2BackupAutomation

📁 Files

lambda_function.py: Python script for daily snapshot and cleanup

README.md: This setup guide

📌 Notes

Ensure your EC2 volume is in available or in-use state before Lambda runs

You can adjust the retention_days in the code as needed
