from django.http import HttpResponse
from django.shortcuts import render, redirect
import hashlib
import random

hexMass = ['sha256', 'md5', 'sha224', 'sha384', 'sha512']

# Create your views here.
def index(request):
    response = render(request, 'main/index.html')
    firstCoding = random.choice(hexMass)
    secondCoding = random.choice(hexMass)

    while firstCoding == secondCoding:
        secondCoding = random.choice(hexMass)

    hash1 = "hashlib." + firstCoding + "(b'true').hexdigest()"
    hash2 = "hashlib." + secondCoding + "(b'true').hexdigest()"

    global firstCoding_obj
    firstCoding_obj = eval(hash1)
    global secondCoding_obj
    secondCoding_obj = eval(hash2)
    if request.COOKIES.get('admin') is None:
        response.set_cookie('admin', 'fcbcf165908dd18a9e49f7ff27810176db8e9f63b4352213741664245224f8aa')
    return response


def final(request):
    secret = request.COOKIES.get('admin')
    if secret == secondCoding_obj:
        response = render(request, 'main/access_admin.html')
        return response
    return redirect('/')

def shop(request):
    secret = request.COOKIES.get('admin')
    if secret is None:
        return HttpResponse('')
    else:
        if secret == firstCoding_obj:
            return HttpResponse('Ты на верном пути, попробуй другую кодировку')
        if secret == secondCoding_obj:
            return redirect('/C0N6RATULAT10N5')
        return HttpResponse('Думай лучше!')

def access_admin(request):
    return HttpResponse('Поздравляю, отличная работа! http://localhost:8000/4dm1n_4cc355')