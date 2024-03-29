# Generated by Django 2.0.3 on 2019-07-16 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='用户名')),
                ('nickname', models.CharField(max_length=30, verbose_name='昵称')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('password', models.CharField(max_length=40, verbose_name='密码')),
                ('sign', models.CharField(max_length=50, verbose_name='个人签名')),
                ('info', models.CharField(max_length=150, verbose_name='个人描述')),
                ('avatar', models.ImageField(upload_to='avatar/')),
            ],
        ),
    ]
