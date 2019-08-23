from django.conf.urls import url

from message import views

urlpatterns = [
    # v1/topics/author_id
    url(r'^/(?P<topic_id>[\d]+)$', views.messages, name='messages')
]
