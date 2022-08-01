from django.urls import path,include
from mmw.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('crud',views.userviews,basename='user')

urlpatterns = [
     path('',include(router.urls))
 ]
 