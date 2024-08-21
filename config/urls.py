from django.contrib import admin
from django.views.generic.base import TemplateView
from django.urls import include, path
from django.conf import settings
from college import views
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("", views.home, name="home"),
    path('admin/', admin.site.urls),
    # path("account/", include("account.urls")),
    path("news/", include("college.urls"), name="newsList"),
    # path("account/", include("django.contrib.auth.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
]

if settings.DEBUG:
    urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
