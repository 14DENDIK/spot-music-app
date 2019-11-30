from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.views import View
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Album, Song
from like.models import Like
from .forms import SongCreateForm


AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']

class HomeView(View):

    def get(self, request):
        albums = Album.objects.all()
        songs = Song.objects.all().order_by('-id')[:10]

        context = {
            'albums': albums,
            'songs': songs
        }

        return render(request, 'music/home.html', context)


# class AlbumDetailView(DetailView):
#     model = Album
#     template_name = 'music/album-detail.html'
#     context_object_name = 'album'

class AlbumDetailView(View):
    def get(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        if self.request.user.is_authenticated:
            user1 = self.request.user
            for song1 in album.song_set.all():
                try:
                    liked_song = Like.objects.get(song=song1, user=user1)
                    song1.is_liked = True
                except ObjectDoesNotExist:
                    song1.is_liked = False
                song1.save()

        context = {
            'album': album,
        }
        return render(request, 'music/album_detail.html', context)


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'artist', 'image']
    template_name = 'music/album_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    fields = ['title', 'artist', 'image']
    template_name = 'music/album_update.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        album = self.get_object()
        if self.request.user == album.created_by:
            return True
        return False


class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    success_url = '/'
    context_object_name = 'album'

    def test_func(self):
        album = self.get_object()
        if self.request.user == album.created_by:
            return True
        return False


class SongLikeView(LoginRequiredMixin, View):

    def get(self, request):
        user1 = self.request.user
        songId = request.GET.get('songId', None)
        song1 = Song.objects.get(pk=songId)

        try:
            user_likes_song = song1.like_set.get(user=user1)
            user_likes_song.delete()
            data = {
                'is_liked': False
            }
        except ObjectDoesNotExist:
            user_likes_song = Like.objects.create(song=song1, user=user1)
            data = {
                'is_liked': True
            }

        return JsonResponse(data)


class SongDeleteView(LoginRequiredMixin, View):
    def get(self, request):
        print("Im inside of the function")
        songId = request.GET.get('songId', None)
        Song.objects.get(pk=songId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class SongCreateView(LoginRequiredMixin, View):
    def get(self, request, album_id):
        album = get_object_or_404(Album, pk=album_id)
        if self.request.user == album.created_by:
            form = SongCreateForm()
            context = {
                'album': album,
                'form': form
            }
            return render(request, 'music/song_create.html', context)
        else:
            raise PermissionDenied()

    def post(self, request, album_id):
        album = get_object_or_404(Album, pk=album_id)
        form = SongCreateForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.album = album
            song.music = request.FILES['music']
            song.created_by = self.request.user
            music_type = song.music.url.split('.')[-1]
            music_type = music_type.lower()
            if music_type not in AUDIO_FILE_TYPES:
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'File you upload must be in "wav", "mp3", or "ogg" format'
                }
                return render(request, 'music/song_create.html', context)

            song.save()
            return redirect('music:album-detail', pk=album_id)

    # def post(self, request, pk):
    #     songGenre = request.POST.get('genre')
    #     songFile = request.FILES.get('file')
    #     album = Album.objects.get(id=pk)
    #
    #     album.song_set.create(name=songName, genre=songGenre, music=songFile)
    #     return HttpResponse(reverse('music:album-detail', kwargs={'pk': album.id}))

# class SongCreateView(LoginRequiredMixin, CreateView):
#     model = Song
#     fields = ['album', 'name', 'genre', 'music']
#     template_name = 'music/song_create.html'
#     success_url = 'music:home'
