from django.shortcuts import render,redirect
from .forms import ImageUploadForm
from .models import UploadedImage


def upload_image(request):
    images = UploadedImage.objects.all()
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageUploadForm()
    return render(request, 'uploadimage.html', {'form': form,'image': images})

def home(request):
    latest_image = UploadedImage.objects.all()
    return render(request, "index.html", {'image': latest_image})

def posts(request):
    latest_image = UploadedImage.objects.all()
    return render(request, "posts.html", {'image': latest_image})

def edit_image(request, image_id):
    image = UploadedImage.objects.get(id=image_id)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageUploadForm(instance=image)
    return render(request, 'editimage.html', {'form': form, 'image': image})


def delete_image(request, image_id):
    image = UploadedImage.objects.get(id=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('home')
    return render(request, 'confirmdelete.html', {'image': image})
