"""fill_in_time URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views


# URLの全体設計
urlpatterns = [
    # 今回作成するアプリ「fill_in_time_app」にアクセスするURL
    path('fill_in_time_app/', include('fill_in_time_app.urls')),
    # 何もURLを指定しない場合（app_config/views.pyで、自動的に「fill_in_time_app」にアクセスするよう設定済み）
    path('', views.index, name='index'),
    # 管理サイトにアクセスするURL
    path('admin/', admin.site.urls),
]

# メディアファイル公開用のURL設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)