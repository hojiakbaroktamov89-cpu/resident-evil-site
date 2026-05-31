from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import home, game_detail, character_detail, movie_detail, history_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('game/<int:pk>/', game_detail, name='game_detail'),
    path('character/<int:pk>/', character_detail, name='character_detail'),
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
    path('history/<int:pk>/', history_detail, name='history_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
