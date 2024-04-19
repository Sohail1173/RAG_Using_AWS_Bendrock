import boto3
import json




prompt="""

        what is machine learning?
"""

bedrock = boto3.client(service_name='bedrock-runtime', region_name='ap-southeast-2')

payload={
    
    "prompt": "[INST]"+prompt+"[/INST]",
    "max_tokens": 200,
    "temperature": 0.1,
    "top_p": 0.9,
     "top_k":50
}

body=json.dumps(payload)

modelId = 'mistral.mistral-7b-instruct-v0:2'
accept = 'application/json'
contentType = 'application/json'

response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

response_body = json.loads(response.get('body').read())
print(response_body["outputs"][0].get("text"))

