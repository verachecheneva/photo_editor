from django.shortcuts import render, get_object_or_404, redirect

from .models import Photo
from .forms import PhotoForm


def index(request):
    photo_count = Photo.objects.count()
    if photo_count > 0:
        photo_list = Photo.objects.all()
        return render(request, 'index.html', {'photo_list': photo_list})
    return render(request, 'index.html')


def photo_page(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'photo_page.html', {'photo': photo})


def new_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            photo_id = Photo.objects.latest('pub_date').id
            return redirect(photo_page, photo_id)
        return render(request, 'new_photo.html', {'photo_form': form})
    form = PhotoForm()
    return render(request, 'new_photo.html', {'photo_form': form})

