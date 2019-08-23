from django.http import JsonResponse

from user.models import UserProfile
import redis


def test_api(request):
    # JsonResponse1,将返回内容序列化成json
    # return JsonResponse({'code':200})

    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    # 加入Redis锁
    try:
        with r.lock('guo', blocking_timeout=3) as lock:
            u = UserProfile.objects.get(username='guo')
            u.score += 1
            u.save()
    except Exception as e:
        print("lock is failed")
    return JsonResponse({'msg': 'test is ok'})
