from django.http import HttpResponse
from django.shortcuts import render, redirect
import hashlib
import random

hexMass = ['sha256', 'md5', 'sha224', 'sha384', 'sha512']
answers = ['b5bea41b6c623f7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b',
           'b326b5062b2f0e69046810717534cb09',
           '6aedcf1f4f9595467c7483d7f5c216be2e7027d76c03e8eac4a2c32d',
           'f2b40fcce9088bd92bacc099e215fd6ed11dc85464bdf25e7646db94a2938d72cd08fa6d85ca426e5db73f6979dbdcde',
           '9120cd5faef07a08e971ff024a3fcbea1e3a6b44142a6d82ca28c6c42e4f852595bcf53d81d776f10541045abdb7c37950629415d0dc66c8d86c64a5606d32de']


def index(request):
    response = render(request, 'main/index.html')
    if request.COOKIES.get('admin') is None:
        firstCoding = random.choice(hexMass)
        secondCoding = random.choice(hexMass)
        while firstCoding == secondCoding:
            secondCoding = random.choice(hexMass)

        response.set_cookie('admin', 'fcbcf165908dd18a9e49f7ff27810176db8e9f63b4352213741664245224f8aa')
        response.set_cookie('_help_yandex_1', hexMass.index(firstCoding))
        response.set_cookie('_help_yandex_2', hexMass.index(secondCoding))
        response.set_cookie('yid', 'false')

        hash1 = "hashlib." + firstCoding + "(b'true').hexdigest()"
        hash2 = "hashlib." + secondCoding + "(b'true').hexdigest()"
        global firstCoding_obj
        firstCoding_obj = eval(hash1)
        global secondCoding_obj
        secondCoding_obj = eval(hash2)
    return response


def final(request):
    secret = request.COOKIES.get('admin')
    secondCoding_obj = eval("hashlib." + hexMass[int(request.COOKIES.get('_help_yandex_2'))] + "(b'true').hexdigest()")
    if secret == secondCoding_obj:
        response = render(request, 'main/access_admin.html')
        response.set_cookie('_help_yandex_2', request.COOKIES.get('_help_yandex_2'), 600)
        response.set_cookie('_help_yandex_1', request.COOKIES.get('_help_yandex_1'), 600)
        response.set_cookie('admin', request.COOKIES.get('admin'), 600)
        response.set_cookie('yid', request.COOKIES.get('yid'), 600)
        return response
    return redirect('/')


def shop(request):
    secret = request.COOKIES.get('admin')
    firstCodeRight = request.COOKIES.get('yid')
    print(firstCodeRight)
    firstCoding_obj = eval("hashlib." + hexMass[int(request.COOKIES.get('_help_yandex_1'))] + "(b'true').hexdigest()")
    secondCoding_obj = eval("hashlib." + hexMass[int(request.COOKIES.get('_help_yandex_2'))] + "(b'true').hexdigest()")
    print('hg')
    if secret is None:
        return HttpResponse('')
    else:
        if firstCodeRight.lower() == 'true':
            if secret == secondCoding_obj:
                return redirect('/C0N6RATULAT10N5')
            else:
                return HttpResponse('Ты отгадал одну из кодировок, попробуй еще одну другую кодировку')
        else:
            if secret == firstCoding_obj:
                response = HttpResponse('Ты отгадал одну из кодировок, попробуй еще одну другую кодировку')
                response.set_cookie('yid', 'true')
                return response
            elif secret in answers:
                return HttpResponse('Ты на верном пути, попробуй другую кодировку')
        return HttpResponse('Думай лучше!')


def access_admin(request):
    return HttpResponse('Поздравляю, отличная работа! http://localhost:8000/4dm1n_4cc355')