from django.db import models

# Create your models here.
from topic.models import Topic
from user.models import UserProfile


class Message(models.Model):
    # topic外键
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.CharField(max_length=60, verbose_name='留言内容')
    # UserProfile外键
    publisher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # 当前内容的父级留言
    parent_message = models.IntegerField(verbose_name='回复留言')
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'message'
