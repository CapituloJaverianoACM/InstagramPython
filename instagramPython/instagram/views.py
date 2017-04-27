from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from instagram.models import Post
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'instagram/index.html')

def createUser(request):
    curr_email = request.POST['email']
    curr_name = request.POST['name']
    curr_nickName = request.POST['nickName']
    curr_password = request.POST['password']
    user_object = User.objects.create_user(first_name=curr_name, username = curr_nickName, password = curr_password, email = curr_email)
    user_object.save()
    return redirect('login')

def getAllPhotosFollow( id_user ):
    user = User.objects.get(pk=id_user)
    ids_follow = user.follow.all();
    #print ids_follow;

@login_required
def mainPage(request):
    curr_user = request.user
    photo_list = "";
    context = { 'curr_user' : curr_user, 'photo_list' : photo_list }
    return render(request, 'instagram/mainPage.html', context)

@login_required
def profile(request):
    curr_user = request.user
    media_user = Post.objects.filter( user_id = curr_user.id );
    #seguidores =
    context = { 'curr_user' : curr_user, 'media_user' : media_user }  # Comillas es el nombre en el HTML, variable
    return render(request, 'instagram/profile.html', context)

@login_required
def uploadPhoto(request):
    curr_user = request.user
    context = { 'curr_user' : curr_user }
    return render(request, 'instagram/uploadPhoto.html', context)

@login_required
def uploadFile(request):
    curr_user = request.user
    post_user = Post.objects.filter(user_id=curr_user.id).count();
    mediaFile = request.FILES[ 'photo' ];
    newNameFile = curr_user.nickname + "-" + id_user + "-" + str(post_user);
    fs = FileSystemStorage()
    filename = fs.save(newNameFile, mediaFile)
    uploaded_file_url = fs.url(filename)
    photo = uploaded_file_url;
    description = request.POST[ 'description' ];
    newPost = Post( photo = photo, description = description, user_id = curr_user );
    #newPost.save();
    media_user = Post.objects.filter( user_id = curr_user.id );
    context = { 'curr_user' : curr_user, 'media_user' : media_user }
    return render(request, 'instagram/profile.html', context)

@login_required
def search( request ):
    curr_user = request.user
    if request.method == 'POST':
        query = request.POST['query']
        try:
            user_list = User.objects.filter(username__icontains=query)
        except User.DoesNotExist:
            user_list = None
        context = { 'curr_user' : curr_user, 'user_list' : user_list }
        return render(request, 'instagram/search.html', context)
    else:
        context = { 'curr_user' : curr_user }
        return render(request, 'instagram/search.html', context)

def follow( request ):
    #print "Soy: " + request.POST['id_follow']
    #print "Sigo a: " + request.POST['curr_user'];
    return render(request, 'instagram/index.html')
