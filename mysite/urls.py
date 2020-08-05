"""mysite URL Configuration
   # 路由配置

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from mysite import views
from django.conf import settings
from django.conf.urls.static import static
#from django.http import HttpResponse
from django.views.generic import TemplateView
'''
映射路径 路由
patterns 模式
'''
# urls.py

#url(r'^robots\.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /admin', content_type='text/plain')),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_views),
    path('robots.txt',TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('album/', views.album_views),
    path('about/', views.about_views),
    path('onbug/', views.onbug_views),
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    path('myblog/', include('myblog.urls', namespace='myblog')),
    path('comment/', include('comment.urls', namespace='comment')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
