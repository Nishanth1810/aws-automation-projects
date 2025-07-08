import boto3
import datetime

# Initialize EC2 client
ec2 = boto3.client('ec2')

# ✅ Your actual volume ID
volume_id = 'vol-0203de441ca9a93f3'

# Retain snapshots for 3 days
retention_days = 3

def lambda_handler(event, context):
    # Today's date
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    # Create snapshot
    description = f"Snapshot on {today} for {volume_id}"
    snapshot = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=description,
        TagSpecifications=[{
            'ResourceType': 'snapshot',
            'Tags': [{
                'Key': 'DeleteOn',
                'Value': (datetime.datetime.now() + datetime.timedelta(days=retention_days)).strftime('%Y-%m-%d')
            }]
        }]
    )
    print(f"✅ Created snapshot: {snapshot['SnapshotId']}")

    # Delete expired snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    for snap in snapshots:
        tags = {t['Key']: t['Value'] for t in snap.get('Tags', [])}
        if tags.get('DeleteOn') == today:
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
            print(f"🗑️ Deleted snapshot: {snap['SnapshotId']}")
