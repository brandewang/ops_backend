from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    url(r'^app/$', views.AppList.as_view()),
    url(r'^app/(?P<pk>[0-9]+)/$', views.AppDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
