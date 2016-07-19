# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from models import Used_stuff
import json

# Create your views here.
english_category_names = ['cloth', 'fashion goods', 'beauty', 'birth/child', 'mobile', 'computer', 'camera', 'electronic device',
            'music/instrument', 'game', 'sports/hobby', 'travel', 'daily_supplies', 'office_supplies', 'furniture/interior',
            'art', 'book/reference_book', 'vehicle/goods', 'etc']

korean_category_names = ['의류', '패션잡화', '미용', '출산/유아', '모바일', '컴퓨터', '카메라', '영상기기', '음악/악기', '게임', '스포츠/취미', '여행',
                         '생활용품', '사무용품', '가구/인테리어', '미술/예술', '도서/참고서', '차/오토바이/자전거', '기타']

def main(request):
    stuffs = Used_stuff.objects.all()
    return render_to_response('index.html', RequestContext(request, {"stuffs": stuffs, 'english_category_names': english_category_names,
                                                                     'korean_category_names': korean_category_names}))

def filter_main(request, category):  # django model filter
    print category
    stuffs = Used_stuff.objects.filter(category=int(category))
    return render_to_response('index.html', RequestContext(request, {"stuffs": stuffs, 'english_category_names': english_category_names,
                                                                     'korean_category_names': korean_category_names}))
def test(request):
    return render_to_response('index3.html', RequestContext(request, {}))

def register_call(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    user.save()

    user = authenticate(username=username, password=password, email=email)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/')

        else:
            return HttpResponse('disabled account')

    else:
        return HttpResponse('invalid login')


def login_call(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('disabled account')

    else:
        return HttpResponse('invalid login')

def logout_call(request):
    logout(request)
    return redirect('/')



'''Data Generation As Json Code'''

def filtered_userstuff_data(request):

    category = request.GET['category']

    stuffs = Used_stuff.objects.filter(category=category)
    json_stuff = []
    for stuff in stuffs:
        json_stuff.append({'name':stuff.name})
    return HttpResponse(json.dumps(json_stuff, indent=4, sort_keys=True), content_type="application/json")

