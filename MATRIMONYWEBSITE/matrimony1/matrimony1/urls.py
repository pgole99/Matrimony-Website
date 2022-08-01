"""matrimony1 URL Configuration

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
from django.urls import path,include
from mmw import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('contact/',views.contact,name='contact'),
    path('info/',views.info,name='info'),
    path('about/',views.about,name='about'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('register/',views.register,name='register'),
    path('person1/',views.personinfo1,name='person'),
    path('delete/<int:id>/',views.delete_data,name='delete'),
    path('<int:id>/',views.update_data,name='update'),
    path('login/',views.user_login,name='login1'),
    path('signup/',views.signup,name='signup'),
    path('',views.logout1,name='logout1'),
    path('api/',include('mmw.api.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
