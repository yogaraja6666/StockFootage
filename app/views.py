from django.shortcuts import render, get_object_or_404, redirect
from .forms import ImageUploadForm, CustomUserForm
from .models import Post
from django.db import models
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        print("uploading problem")
        form = ImageUploadForm()
    return render(request, 'uploadimage.html', {'form': form})

def home(request):
    orientation = request.GET.get('orientation')
    query = request.GET.get('query')
    photos = Post.objects.order_by('-uploaded_at')

    if orientation:
        photos = photos.filter(orientation=orientation)

    if query:
        photos = photos.filter(models.Q(title__icontains=query) | models.Q(tag__icontains=query))    
  
        
    # Split the photos into three columns
    num_photos = len(photos)

    if num_photos == 0:
        return render(request, 'noresult.html')
        
    num_per_column = (num_photos + 2) // 3  # Distribute photos evenly
    columns = [photos[i:i+num_per_column] for i in range(0, num_photos, num_per_column)]
    
    postdata = Post.objects.all()
    if request.method =='GET':
        st=request.GET.get('Postname')
        if st!=None:
            postdata = Post.objects.filter(title__icontains=st)
    return render(request, 'index.html', {'columns': columns,'postdata':postdata})


'''
def base(request):
    postdata = Post.objects.all()
    if request.method =='GET':
        st=request.GET.get('Postname')
        if st!=None:
            postdata = Post.objects.filter(title__icontains=st)
    data={
        'postsdata' : postdata
    }
    return render(request, 'base.html',data)
'''




def posts(request):
    orientation = request.GET.get('orientation')
    user = request.user
    photo = Post.objects.filter(user=user).order_by('-uploaded_at')
    if orientation:
        photo = photo.filter(orientation=orientation)
    num_photos1 = len(photo)
    num_per_column1 = (num_photos1 + 2) // 3  # Distribute photos evenly
    if num_per_column1 <= 0:
        num_per_column1 = 1
    columns1 = [photo[i:i+num_per_column1] for i in range(0, num_photos1, num_per_column1)]
    return render(request, 'posts.html', {'columns1': columns1})


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        # Handle form submission to edit the post
        return redirect('home')
    else:
        form = ImageUploadForm(instance=post)
    return render(request, 'editimage.html', {'form' : form , 'post': post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'confirmdelete.html', {'post': post})

def suggest_keywords(request):
    query = request.GET.get('query', '')
    if query:
        suggestions = list(Post.objects.filter(title__icontains=query).values_list('title', flat=True)[:5])
    else:
        suggestions = []
    return JsonResponse({'suggestions': suggestions})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("login succes",username,password)
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL name
        else:
            print("login failed")
            return redirect('login')
    return render(request,'login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    return render(request, 'register.html',{"form":form})




