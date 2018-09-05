from django.contrib import admin
from music_recommender.models import Artist


myModels = [Artist]
admin.site.register(myModels)
