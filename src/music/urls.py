from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'music'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album-detail'),
    path('album/create/', views.AlbumCreateView.as_view(), name='album-create'),
    path('album/update/<int:pk>/', views.AlbumUpdateView.as_view(), name='album-update'),
    path('album/delete/<int:pk>/', views.AlbumDeleteView.as_view(), name='album-delete'),
    path('ajax/song/like/', views.SongLikeView.as_view(), name='like-song'),
    path('ajax/song/delete/', views.SongDeleteView.as_view(), name='delete-song'),
    path('album/<int:album_id>/add/song/', views.SongCreateView.as_view(), name='song-create'),
    # path('ajax/song/like/', views.like_song, name='like-song'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
