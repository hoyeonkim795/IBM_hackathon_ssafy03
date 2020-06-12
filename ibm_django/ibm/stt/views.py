from django.shortcuts import render, redirect
from os.path import join, dirname
from . import mymodule_stt
from . import mymodule_tts
#from mytest import keyword
from .models import Audio
from .forms import AudioForm

# Create your views here.

def index(request):
    stt_api_key = '_sX-7ZuY39EjyTVYHxe-7tl04k9eVIIbJ7846MZO2BMQ'
    stt_api_url = 'https://api.kr-seo.speech-to-text.watson.cloud.ibm.com/instances/f568fcb0-c3d4-4f13-b89e-d17b67d5adc2'
    tts_api_key = 'zyhuldAdd4JA6bjKqcfrVS9RcQ3bVYZhcOgBA9KkaJRB'
    tts_api_url = 'https://api.kr-seo.text-to-speech.watson.cloud.ibm.com/instances/c07cdd3a-f37f-4b6d-8696-c7cab643d85c'
    filename = 'corona.wav'
    authenticator = mymodule_stt.authenticate(stt_api_key)
    speech_to_text = mymodule_stt.stt(authenticator)
    mymodule_stt.set_url(speech_to_text, stt_api_url)
    speech_recognition_results = mymodule_stt.start_stt(speech_to_text, filename)
    keywords = mymodule_stt.get_keyword(speech_recognition_results)

    authenticator2 = mymodule_tts.authenticate(tts_api_key)
    text_to_speech = mymodule_tts.tts(authenticator2)
    mymodule_tts.set_url(text_to_speech, tts_api_url)
    filename2 = 'hello_world.wav'
    mymodule_tts.start_tts(text_to_speech, filename2, '질병관리본부 번호는 1339 입니다')
    file_dir = join(dirname(__file__), './', filename2)
    context = {
        'keywords' : keywords,
        'file_dir' : file_dir
    }
    return render(request, 'stt/index.html', context)

# Create your views here.


def create(request):
    #POST
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        # 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('stt:index')

        else:
            return redirect('stt:index')


    else :
        form = AudioForm()
    context = {
        'form': form,

    }
    return render(request,'stt/form.html',context)