import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('_sX-7ZuY39EjyTVYHxe-7tl04k9eVIIbJ7846MZO2BMQ')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.kr-seo.speech-to-text.watson.cloud.ibm.com/instances/f568fcb0-c3d4-4f13-b89e-d17b67d5adc2')

with open(join(dirname(__file__), './media/timeline_audio', 'corona.wav'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/wav',
        model='ko-KR_NarrowbandModel',
        word_alternatives_threshold=0.9,
    
        keywords=['\ub54c\ubb38\uc5d0', '\uc790\uafb8'],
        keywords_threshold=0.5
    ).get_result()


keyword = dict(speech_recognition_results, indent=2)["results"][0]["alternatives"][0]["transcript"]
typing = keyword.split()
print(typing)
# keywords = result["keywords_result"]

