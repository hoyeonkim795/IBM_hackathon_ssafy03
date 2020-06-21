from os.path import join, dirname
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# authenticator = IAMAuthenticator('zyhuldAdd4JA6bjKqcfrVS9RcQ3bVYZhcOgBA9KkaJRB')

def authenticate(k):
    authenticator = IAMAuthenticator(k)
    return authenticator

# text_to_speech = TextToSpeechV1(
#     authenticator=authenticator
# )


def tts(a):
    speech_to_text = TextToSpeechV1(authenticator=a)
    return speech_to_text



def set_url(tts, api_url):
    tts.set_service_url(api_url)
    return tts


# with open('hello_world.wav', 'wb') as audio_file:
#     audio_file.write(
#         text_to_speech.synthesize(
#             'hi hyunoo',
#             voice='ko-KR_YunaVoice',
#             accept='audio/wav'        
#         ).get_result().content)


def start_tts(tts, filename, text):
    with open(join(dirname(__file__), '../media/timeline_audio', filename), 'wb') as audio_file:
        audio_file.write(
            tts.synthesize(
                text,
                voice='en-US_MichaelV3Voice',
                accept='audio/wav'        
            ).get_result().content)
        

