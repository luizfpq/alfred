import boto3
import json

bedrock = boto3.client(service_name="bedrock-runtime")
body = json.dumps({
  "max_tokens": 256,
  "messages": [{"role": "user", "content": "Hello, world"}],
  "anthropic_version": "bedrock-2023-05-31"
})

response = bedrock.invoke_model(body=body, modelId="anthropic.claude-3-sonnet-20240229-v1:0")

response_body = json.loads(response.get("body").read())
print(response_body.get("content"))
