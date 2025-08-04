from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai import Credentials

api_key="a_Y4ACT-LB_rWPd373JUZ9ElPZgELwqEw8839CWVkUj7"
service_url="https://au-syd.ml.cloud.ibm.com"
project_id = "82bce3df-8624-462d-b136-4fe097d1ed14"


#Credentials authentication
creds=Credentials(api_key=api_key, url=service_url)
model_id="ibm/granite-3-8b-instruct"
model=Model(model_id=model_id, credentials=creds, project_id=project_id)
prompt="Explain in 3 points why startups fail"
params={"decoding_method":"greedy","max_new_tokens":300}
response=model.generate_text(prompt=prompt, params=params)
print("\n---AI Response--\n")
print(response)