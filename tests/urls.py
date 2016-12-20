from tests.test import views

try:
    from django.conf.urls import patterns
    urlpatterns = patterns('',
                           (r'^test_api', views.test_api)
                           )
except ImportError:
    from django.conf.urls import url
    urlpatterns = [
        url(r'^test_api', views.test_api)
    ]
