# *method-可接受 任意参数
# **kwargs-可接受 多个key=value无形参数
import jwt
from django.http import JsonResponse

from user.models import UserProfile

KEY = 'abcdef123'


def login_check(*methods):
    def _loging_check(func):
        def wrapper(request, *args, **kwargs):
            # token放在request header-->authorization
            # token=request.META.get('HTTP_AUTHORIZATION')
            token = request.META.get('HTTP_AUTHORIZATION')
            if not methods:
                # 如果没传methods参数，则直接返回视图
                return func(request, *args, **kwargs)
            # method有值
            if not request.method in methods:
                # 如果当前请求的方法不在methods内，则直接返回视图
                return func(request, *args, **kwargs)
            # 严格要求参数大小写，统一大写
            # 严格要求methods里的参数是POST,GET,PUT,DELETE

            # token校验
            if not token:
                result = {'code': 107, 'error': 'Please give me token'}
                return JsonResponse(result)
            # 校验token,pyjwt注意异常检测
            try:
                # pyjwt decode->验证token
                res = jwt.decode(token, KEY, algorithms='HS256')
            except Exception as e:
                print('---token error is %s' % (e))
                result = {'code': 108, 'error': 'Please login'}
                return JsonResponse(result)
            # token校验成功，根据用户名取出用户
            username = res['username']
            user = UserProfile.objects.get(username=username)
            # request.user=user
            request.user = user
            return func(request, *args, **kwargs)

        return wrapper

    return _loging_check


def get_user_by_request(request):
    '''
    通过request获取用户
    :param request:
    :return:user对象 or None
    '''
    token = request.META.get('HTTP_AUTHORIZATION')
    # 检查token
    if not token or token == 'null':
        return None
    try:
        res = jwt.decode(token, KEY, algorithms='HS256')
    except Exception as e:
        print("--get_uer_by_request -jwt decode error is %s" % (e))
        return None
    # 获取token中的用户名
    username = res['username']
    user = UserProfile.objects.get(username=username)
    return user
