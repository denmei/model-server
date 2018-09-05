from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('music_recommender.api_v0.urls'))
]