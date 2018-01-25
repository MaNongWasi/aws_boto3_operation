from __future__ import print_function
import boto3
#import json
import sys

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(tableName)


response = table.put_item(
	Item={
	'key1':'data1',
	'key2':'data2',
	}
)

print (response["ResponseMetadata"]["RetryAttempts"])

