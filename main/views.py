from django.http import HttpResponse
from django.shortcuts import render, redirect
import hashlib


# Create your views here.
def index(request):
    response = render(request, 'main/index.html')
    if request.COOKIES.get('admin') is None:
        response.set_cookie('admin', 'fcbcf165908dd18a9e49f7ff27810176db8e9f63b4352213741664245224f8aa')
    return response


def shop(request):
    secret = request.COOKIES.get('admin')
    if secret is None:
        return HttpResponse('')
    else:
        sha256_obj = hashlib.sha256(b'true').hexdigest()
        md5_obj = hashlib.md5(b'true').hexdigest()
        if secret == sha256_obj:
            return HttpResponse('Ты на верном пути, попробуй другую кодировку')
        if secret == md5_obj:
            return redirect('/access_admin')
        return HttpResponse('Думай лучше!')
