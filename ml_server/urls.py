"""
ml_server URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^main/', include('main.urls')),

    url(r'^$', RedirectView.as_view(url='/main/', permanent=True)),
    url(r'^music_recommender/', include('music_recommender.urls')),
    url(r'^docs/', include_docs_urls(title='ML-Server Api', authentication_classes=[], permission_classes=[]))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

