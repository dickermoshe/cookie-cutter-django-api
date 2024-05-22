from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.versioning import URLPathVersioning
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.http import JsonResponse


def health_check(request):
    return JsonResponse({"status": "ok"})

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
        path("api/", include("api.urls")),
    path("health/", health_check),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
