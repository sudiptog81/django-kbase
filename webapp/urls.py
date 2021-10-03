from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static

import kbase

from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('kbase.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = kbase.views.not_found
