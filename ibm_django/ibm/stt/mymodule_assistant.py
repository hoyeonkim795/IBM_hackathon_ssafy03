import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#authenticator = IAMAuthenticator('RP9pUsl_Z-uZd4fTxaa78wlivZ1rQhpL_XZOekDD1mjn')

def authenticate(api_key):
    authenticator = IAMAuthenticator(api_key)
    return authenticator

# assistant = AssistantV2(
#     version='2020-04-01',
#     authenticator = authenticator
# )

def set_assistant(authenticator):
    assistant = AssistantV2(
        version='2020-04-01',
        authenticator= authenticator
    )
    return assistant


#assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/6d8c3435-9650-4202-af84-07fc845a4f34')


def set_url(assistant, api_url):
    assistant.set_service_url(api_url)
    return assistant

# response = assistant.message_stateless(
#     assistant_id='a212691b-e3f4-41ee-9015-20e2370aee5f',
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