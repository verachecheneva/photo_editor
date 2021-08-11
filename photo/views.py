from django.shortcuts import render, get_object_or_404, redirect
import requests
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File


from .models import Photo
from .forms import PhotoForm, ChangeImageForm


def index(request):
    photo_count = Photo.objects.count()
    if photo_count > 0:
        photo_list = Photo.objects.all()
        return render(request, 'index.html', {'photo_list': photo_list})
    return render(request, 'index.html')


def photo_page(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.method == 'POST':
        form = ChangeImageForm(request.POST)
        if form.is_valid():
            width = form.cleaned_data.get('width')
            height = form.cleaned_data.get('height')
            photo.resize_photo(width, height)
            im = True
            return render(request, 'photo_page.html', {'photo': photo, 'change_form': form, 'im': im})

    form = ChangeImageForm()
    return render(request, 'photo_page.html', {'photo': photo, 'change_form': form})


def new_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            if photo.image_url and not photo.image:
                r = requests.get(photo.image_url)

                img_temp = NamedTemporaryFile()
                img_temp.write(r.content)
                img_temp.flush()

                photo.image.save("image.jpg", File(img_temp), save=True)
            photo.save()
            photo_id = Photo.objects.latest('pub_date').id
            return redirect(photo_page, photo_id)
        return render(request, 'new_photo.html', {'photo_form': form})
    form = PhotoForm()
    return render(request, 'new_photo.html', {'photo_form': form})

