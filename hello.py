from flask import Flask, jsonify, json
from os import environ, path
from dotenv import load_dotenv
import boto3
from boto3.dynamodb.conditions import Key 

app = Flask(__name__)


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        if isinstance(o, set):  # <---resolving sets as lists
            return list(o)
        return super(DecimalEncoder, self).default(o)



basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

USERS_TABLE = environ.get('USERS_TABLE')
client = boto3.resource('dynamodb',
                      aws_access_key_id=environ.get('aws_access_key_id'),
                      aws_secret_access_key=environ.get('aws_secret_access_key'),
                      region_name='us-east-1'                      
                      )
table = client.Table(environ.get('USERS_TABLE'))

@app.route('/hello')
def hello():
    return jsonify({'test':'i am learning flask'})


@app.route('/secret')
def secret():
    
    response = table.query(
        KeyConditionExpression=Key('code_name').eq('thedoctor')
    )
    return json.dumps((response.get('Items')), indent=4, cls=DecimalEncoder)
   
    """resp = client.get_item(
        TableName=USERS_TABLE,
        Key={
            'code_name': {'S': 'thedoctor'}
        }
    )
    item = resp.get('Item')
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    return response"""


@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'container': '< LINK_TO_HUB >' , 'project': 'github.com/omerxx/ecscale' })

if __name__ == '__main__':
    app.run()
