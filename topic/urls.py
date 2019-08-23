from django.conf.urls import url

from topic import views

urlpatterns = [
    # v1/topics/author_id
    url(r'/(?P<author_id>[\w]+)$',views.topics,name='topics')
]
