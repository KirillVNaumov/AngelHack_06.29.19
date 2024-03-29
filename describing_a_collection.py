import boto3
from botocore.exceptions import ClientError

if __name__ == "__main__":

    collectionId='Gamers'
    print('Attempting to describe collection ' + collectionId)
    client=boto3.client('rekognition')

    try:
        response=client.describe_collection(CollectionId=collectionId)
        print("Collection Arn: "  + response['CollectionARN'])
        print("Face Count: "  + str(response['FaceCount']))
        print("Face Model Version: "  + response['FaceModelVersion'])
        print("Timestamp: "  + str(response['CreationTimestamp']))

        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print ('The collection ' + collectionId + ' was not found ')
        else:
            print ('Error other than Not Found occurred: ' + e.response['Error']['Message'])
    print('Done...')


