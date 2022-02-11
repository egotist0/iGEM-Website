from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'v1/array/', views.arraysGenericAPIView_v1.as_view()),
    url(r'v2/array/', views.arraysGenericAPIView_v2.as_view()),

    # url(r'array/(?P<pk>\d+)/$', views.arrayGenericAPIView.as_view()),

     url(r'v1/svm/', views.svmsGenericAPIView.as_view()),
    # url(r'svm/(?P<pk>\d+)/$', views.svmGenericAPIView.as_view()),

    url(r'v1/seq/', views.seqsGenericAPIView.as_view()),
    # url(r'seq/(?P<pk>\d+)/$', views.seqGenericAPIView.as_view()),
]

