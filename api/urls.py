from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter

# from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'app', views.AppViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'appgrp', views.AppGrpViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^test', views.test),
    url(r'^gitlab/get_modules', views.gitlab_get_modules)
]

# urlpatterns = [
#     url(r'^app/$', views.AppList.as_view()),
#     url(r'^app/(?P<pk>[0-9]+)/$', views.AppDetail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
