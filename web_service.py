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


@app.route('/test')
def test():
    return "Works!"

@app.route('/secret')
def secret():
    
    response = table.query(
        KeyConditionExpression=Key('code_name').eq('thedoctor')
    )
    return json.dumps((response.get('Items')), indent=4, cls=DecimalEncoder)


@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'container': 'https://hub.docker.com/r/sreemaish/python-dynamo-webservice', 'project': 'https://github.com/SREEMATHI1/python-dynamo-sample'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
