import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


#authenticator = IAMAuthenticator('_sX-7ZuY39EjyTVYHxe-7tl04k9eVIIbJ7846MZO2BMQ')


# authenticator 지정
def authenticate(k):
    authenticator = IAMAuthenticator(k)
    return authenticator

# speech_to_text = SpeechToTextV1(
#     authenticator=authenticator
# )


# speech_to_text 지정
def stt(a):
    speech_to_text = SpeechToTextV1(authenticator=a)
    return speech_to_text


# 얘는 views.py에서 만들기


def set_url(stt, api_url):
    stt.set_service_url(api_url)
    return stt


# with open(join(dirname(__file__), './media/timeline_audio', 'corona.wav'),
#                'rb') as audio_file:
#     speech_recognition_results = speech_to_text.recognize(
#         audio=audio_file,
#         content_type='audio/wav',
#         model='ko-KR_NarrowbandModel',
#         word_alternatives_threshold=0.9,
    
#         keywords=['\ub54c\ubb38\uc5d0', '\uc790\uafb8'],
#         keywords_threshold=0.5
#     ).get_result()


# open 함수화
def start_stt(stt, filename):
    with open(join(dirname(__file__), '../media/timeline_audio', filename), 'rb') as audio_file:
        speech_recognition_results = stt.recognize(
        audio=audio_file,
        content_type='audio/wav',
        model='en-US_ShortForm_NarrowbandModel',
        word_alternatives_threshold=0.9,
    
        keywords=['\ub54c\ubb38\uc5d0', '\uc790\uafb8'],
        keywords_threshold=0.5
    ).get_result()
    return speech_recognition_results


def get_keyword(srr):
    keyword = dict(srr, indent=2)["results"][0]["alternatives"][0]["transcript"]
    return keyword



# keyword = dict(speech_recognition_results, indent=2)["results"][0]["alternatives"][0]["transcript"]
# typing = keyword.split()
# print(typing)
# keywords = result["keywords_result"]

