from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from instagram.models import Post,MyUser,Follow
from django.core.files.storage import FileSystemStorage

def index(request):
    if request.user.is_authenticated:
        return redirect('mainPage')
    return render(request, 'instagram/index.html')

def createUser(request):
    curr_email = request.POST['email']
    curr_name = request.POST['name']
    curr_nickName = request.POST['nickName']
    curr_password = request.POST['password']
    myuser_object = MyUser()
    user_object = User.objects.create_user(first_name=curr_name, username = curr_nickName, password = curr_password, email = curr_email)
    myuser = MyUser( user = user_object )
    myuser.save()
    user_object.save()
    return redirect('login')

@login_required
def mainPage(request):
    curr_user = request.user
    photo_list = []
    for user_aux in Follow.objects.filter( from_id = curr_user.myuser ):
        search_user = MyUser.objects.get( pk = user_aux.to_id.id )
        post_aux = Post.objects.filter(user_id=search_user.user.id)
        if not post_aux:
            print ("No hay nada")
        else:
            for photo_aux in post_aux:
                print (photo_aux.user_id.username)
                photo_list.append( photo_aux );
    context = { 'curr_user' : curr_user, 'photo_list' : photo_list }
    return render(request, 'instagram/mainPage.html', context)

@login_required
def profile(request, _username):
    curr_user = User.objects.get(username=_username)
    media_user = Post.objects.filter( user_id = curr_user.id );
    follow_number = Follow.objects.filter( from_id = curr_user.myuser ).count();
    followers_number = Follow.objects.filter( to_id = curr_user.myuser ).count();
    context = { 'register_user' : request.user, 'curr_user' : curr_user, 'media_user' : media_user, 'follow_number' : follow_number,
    'followers_number' : followers_number }
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
    newNameFile = curr_user.username + "-" + str(curr_user.id) + "-" + str(post_user);
    fs = FileSystemStorage()
    filename = fs.save(newNameFile, mediaFile)
    uploaded_file_url = fs.url(filename)
    photo = uploaded_file_url;
    description = request.POST[ 'description' ];
    newPost = Post( photo = photo, description = description, user_id = curr_user );
    newPost.save();
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

def follow( request, _username ):
    to = User.objects.get(username=_username);
    fo = Follow.objects.create( from_id = request.user.myuser, to_id = to.myuser )
    request.user.myuser.follow = fo;
    return redirect(request, 'index')
