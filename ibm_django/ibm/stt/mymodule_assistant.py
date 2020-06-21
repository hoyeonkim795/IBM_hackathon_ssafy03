import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#authenticator = IAMAuthenticator('RP9pUsl_Z-uZd4fTxaa78wlivZ1rQhpL_XZOekDD1mjn')

def authenticate(api_key):
    authenticator = IAMAuthenticator(api_key)
    return authenticator

# assistant = AssistantV2(
    # assistant_id='0f1acf04-bddb-4195-b475-fdea90a92179',
#     version='2020-04-01',
#     authenticator = authenticator
# )

def set_assistant(authenticator):
    assistant = AssistantV2(
        version='2020-04-01',
        authenticator= authenticator
    )
    return assistant




def set_url(assistant, api_url):
    assistant.set_service_url(api_url)
    return assistant

# response = assistant.message_stateless(
#     assistant_id='',
#     input={
#         'message_type': 'text',
#         'text': 'tell a joke'
#     }
# ).get_result()


def get_response(assistant, a_id, text):
    response = assistant.message_stateless(
        assistant_id= a_id,
        input={
            'message_type': 'text',
            'text': text
        }
    ).get_result()
    texts = response['output']['generic'][0]['text']
    return texts

#print(json.dumps(response, indent=2))