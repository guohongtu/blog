# Generated by Django 2.0.3 on 2019-08-01 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topic', '0002_auto_20190726_2039'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=60, verbose_name='留言内容')),
                ('parent_message', models.IntegerField(verbose_name='回复留言')),
                ('create_time', models.DateTimeField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic')),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]
