"""blog_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^test_api', views.test_api),
    url(r'v1/users', include('user.urls')),
    url(r'v1/token', include('btoken.urls')),
    url(r'v1/topic', include('topic.urls')),
    url(r'v1/messages',include('message.urls'))


]
# from django.conf import settings
# from django.conf.urls.static import static
# 添加图片路由映射http://127.0.0.1:8000/media/aaa.jpg
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







