from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileCiteForm, ProfileImageForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('music:home')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

# class UserRegisterView(View):
#
#     def get(request, *args, **kwargs):
#         form = UserCreationForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'user/register.html', context)
#
#
#     def post(request, *args, **kwargs):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('music:home')
@login_required
def profile(request, *args, **kwargs):
    if request.method == 'POST':
        if 'cite_update' in request.POST:
            c_form = ProfileCiteForm(request.POST, instance = request.user.profile)
            if c_form.is_valid():
                c_form.save()
                return redirect('user:profile')
        elif 'image_update' in request.POST:
            i_form = ProfileImageForm(request.POST, request.FILES, instance = request.user.profile)
            old_photo = request.user.profile.image
            if i_form.is_valid():
                profile = i_form.save(commit=False)
                profile.image = request.FILES['image']
                image_type = profile.image.url.split('.')[-1]
                image_type = image_type.lower()
                if image_type not in IMAGE_FILE_TYPES:
                    # c_form = ProfileCiteForm()
                    # i_form = ProfileImageForm(instance = request.user.profile)
                    # profile.image = old_photo
                    return redirect('user:profile')
                profile.save()
                return redirect('user:profile')
    else:
        c_form = ProfileCiteForm()
        i_form = ProfileImageForm(instance = request.user.profile)

        context = {
            'c_form': c_form,
            'i_form': i_form
        }
        return render(request, 'user/profile.html', context)

# class ProfileView(View):
#     def get(request, *args, **kwargs):
#         form = ProfileCiteForm(instance = request.user.profile)
#         context = {
#             form: 'form'
#         }
#         return render(request, 'user/profile.html', context)
#
#
#     def post(request, *args, **kwargs):
#         form = ProfileCiteForm(request.POST, instance = request.user.profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Cite has been updated!")
#             return redirect('user:profile')

class GuestProfileView(View):

    def get(self, request, name):
        user = get_object_or_404(User, username=name)
        context = {
            'user': user
        }
        return render(request, 'user/guest_profile.html', context)
