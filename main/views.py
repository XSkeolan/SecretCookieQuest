from django.http import HttpResponse
from django.shortcuts import render, redirect
import hashlib
import random

hexMass = ['sha256', 'md5', 'sha224', 'sha384', 'sha512']

# 6aedcf1f4f9595467c7483d7f5c216be2e7027d76c03e8eac4a2c32d
def index(request):
    response = render(request, 'main/index.html')
    if request.COOKIES.get('admin') is None:
        firstCoding = random.choice(hexMass)
        secondCoding = random.choice(hexMass)
        response.set_cookie('admin', 'fcbcf165908dd18a9e49f7ff27810176db8e9f63b4352213741664245224f8aa')
        response.set_cookie('_help_yandex_1', hexMass.index(firstCoding))
        response.set_cookie('_help_yandex_2', hexMass.index(secondCoding))
        while firstCoding == secondCoding:
            secondCoding = random.choice(hexMass)

        hash1 = "hashlib." + firstCoding + "(b'true').hexdigest()"
        hash2 = "hashlib." + secondCoding + "(b'true').hexdigest()"
        global firstCoding_obj
        firstCoding_obj = eval(hash1)
        global secondCoding_obj
        secondCoding_obj = eval(hash2)
        with open('/tmp/runtime-server/temp', 'w+') as f:
            f.write(secondCoding_obj)
    return response


def final(request):
    secret = request.COOKIES.get('admin')
    secondCoding_obj = eval("hashlib." + hexMass[request.COOKIES.get('_help_yandex_2')] + "(b'true').hexdigest()")
    if secret == secondCoding_obj:
        response = render(request, 'main/access_admin.html')
        return response
    return redirect('/')

def shop(request):
    secret = request.COOKIES.get('admin')
    firstCoding_obj = eval("hashlib." + hexMass[int(request.COOKIES.get('_help_yandex_1'))] + "(b'true').hexdigest()")
    secondCoding_obj = eval("hashlib." + hexMass[int(request.COOKIES.get('_help_yandex_2'))] + "(b'true').hexdigest()")
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