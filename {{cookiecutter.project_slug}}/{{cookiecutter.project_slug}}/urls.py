from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.versioning import URLPathVersioning
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "schema/",
        SpectacularAPIView.as_view(
            versioning_class=URLPathVersioning,
            api_version="v1",
        ),  # type: ignore
        name="schema",
    ),  # type: ignore
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),  # type: ignore
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
