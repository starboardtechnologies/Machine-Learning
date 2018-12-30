import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
text = "What is the weather like in France?"

print('Calling DetectEntities')
print(json.dumps(comprehend.detect_entites(Text=text, LanguageCode='en'), sort_keys=True, indent=4) 
print('End of DetectEntities\n')