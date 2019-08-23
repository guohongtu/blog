import hashlib
import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render

from user.models import UserProfile


def btoken(request):
    if not request.method == 'POST':
        # 当前视图函数只接受post
        result = {'code': 101, 'error': 'Please use POST'}
        return JsonResponse(request)
    json_str = request.body
    if not json_str:
        # post未提交数据
        result = {'code': 102, 'error': 'Please Post data'}
        return JsonResponse(result)

    json_obj = json.loads(json_str)
    # 获取用户名和密码
    username = json_obj.get('username')
    password = json_obj.get('password')
    if not username:
        result = {'code': 103, 'error': 'Please give me username!'}
        return JsonResponse(result)
    if not password:
        result = {'code': 104, 'error': 'Please give me password!'}
        return JsonResponse(result)
    users = UserProfile.objects.filter(username=username)
    if not users:
        result = {'code': 105, 'error': 'The user is not existed'}
        return JsonResponse(result)
    # hash password
    p_m = hashlib.sha1()
    p_m.update(password.encode())
    # 对比密码
    if p_m.hexdigest() != users[0].password:
        result = {'code': 106, 'error': 'The username is wrong or the password is wrong!'}
        return JsonResponse(result)
    #生成token
    token=make_token(username)
    result={'code':200,'username':username,'data':{'token':token.decode()}}
    return JsonResponse(result)


def make_token(username, expire=3600 * 24):
    '''
    :param username:
    :param expire:
    :return:
    '''
    key = 'abcdef123'
    now_t = time.time()
    payload = {'username': username, 'exp': int(now_t + expire)}
    return jwt.encode(payload, key, algorithm='HS256')
