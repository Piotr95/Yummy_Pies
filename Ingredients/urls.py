from django.conf.urls import url
from django.contrib import admin
from Ingredients import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Ingredients'
urlpatterns = [
    url(r'Ingredients', views.list_of_Ingredients, name="Ing"),
    url(r'Ingredient_create', views.create_Ingredient, name="Create"),
    url(r'^(?P<Ingredient_id>[0-9]+)/delete_album/$', views.delete_Ingredient, name="Delete"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)