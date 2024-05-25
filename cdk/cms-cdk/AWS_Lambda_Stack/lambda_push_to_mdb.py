
import boto3
import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

def handler(event, context):


    try:

        #Read data passed to eventbus (e.g. sagemaker-lambda-partner)
        predicted_value = event['detail']['predicted_value']
        vin = event['detail']['vin']

        print("prediction: " + str(predicted_value))
        print("VIN: " + str(vin))

        # Set up MongoDB Atlas connection
        try:
            
            #Set up our Client
            client = boto3.client('secretsmanager')

       
            #Calling SecretsManager
            get_secret_value_response = client.get_secret_value(
            SecretId="CMS_ATLAS_URL"
            )
       
            #Extracting the key/value from the secret
            ATLAS_URI = get_secret_value_response['SecretString']
        

            client = MongoClient(host=ATLAS_URI)


            db = client['Integrations']
            collection = db['Sagemaker']
        except ConnectionFailure:
            print('Failed to connect to MongoDB Atlas.')
        except OperationFailure as error:
            print(f'Failed to authenticate with MongoDB Atlas: {error}')

        # Define the document to update or insert
        filter = {'vin': str(vin)}
        update = {'$set': {'prediction': str(predicted_value)}}

        print (filter)
        print (update)

        # Perform the upsert operation
        try:
            result = collection.update_one(filter, update, upsert=True)
            print(f'{result.modified_count} document(s) updated.')
        except OperationFailure as error:
            print(f'Failed to update or insert document: {error}')

    except Exception as e:
        print("error" + str(e))
        raise e
