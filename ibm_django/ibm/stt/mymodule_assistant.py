import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


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