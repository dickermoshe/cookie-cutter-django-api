from django.urls import include, re_path
from .router import router_urls

urlpatterns = [re_path(r"^(?P<version>(v1))/", include(router_urls))]
