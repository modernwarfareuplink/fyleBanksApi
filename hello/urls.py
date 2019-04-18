from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ifsc/(?P<ifsc>[a-zA-Z0-9-]{11})/?$', views.ifscFetch, name="ifscFetch"),
    url(r'^search/?$', views.branchFetch, name="branchFetch"),
    url(r'^credits/?$', views.credits, name="credits"),
]
