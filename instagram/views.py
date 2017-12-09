from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from instagram.models import *
from instagram.forms import *
from django.core.files.storage import FileSystemStorage

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            curr_email = form.cleaned_data['email']
            curr_name = form.cleaned_data['name']
            curr_username = form.cleaned_data['username']
            curr_password = form.cleaned_data['password']
            user_object = User.objects.create_user(first_name=curr_name, username = curr_username, password = curr_password, email = curr_email)
            myuser = MyUser( user = user_object )
            myuser.save()
            return redirect('login')
        else:
            context = {'form':form}
            return render(request, 'index.html', context)
    else:
        if request.user.is_authenticated:
            return redirect('home')
        form = UserForm()
        context = {'form':form}
        return render(request, 'index.html', context)


@login_required
def home(request):
    curr_user = request.user
    photo_list = []
    for user_aux in Follow.objects.filter( from_user = curr_user.myuser ):
        search_user = MyUser.objects.get( pk = user_aux.to_user.id )
        post_aux = Post.objects.filter(owner_user=search_user.user.id)
        if post_aux:
            for photo_aux in post_aux:
                print ("Photo con id:" + str(photo_aux.pk) )
                print (photo_aux.like_set.count())
                photo_list.append( photo_aux )
    for post_aux in Post.objects.filter(owner_user = curr_user):
        photo_list.append(post_aux)
    likes = []
    for like in Like.objects.filter(user = curr_user):
        likes.append(like.post.pk)
    context = { 'curr_user' : curr_user, 'photo_list' : photo_list, 'likes' : likes }
    return render(request, 'home.html', context)

@login_required
def profile(request, _username):
    try:
        curr_user = User.objects.get(username=_username)
    except User.DoesNotExist:
        return render(request, 'error_user.html')
    media_user = Post.objects.filter( owner_user = curr_user )
    follow_number = Follow.objects.filter( from_user = curr_user.myuser ).count()
    followers_number = Follow.objects.filter( to_user = curr_user.myuser ).count()
    if _username != request.user:
        if Follow.objects.filter(from_user = request.user.myuser, to_user = curr_user.myuser).count() > 0:
            already_follow = True
        else:
            already_follow = False
    context = { 'register_user' : request.user,
                'curr_user' : curr_user,
                'media_user' : media_user,
                'follow_number' : follow_number,
                'followers_number' : followers_number,
                'already_follow' : already_follow
                }
    return render(request, 'profile.html', context)

@login_required
def uploadFile(request):
    curr_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_user = Post.objects.filter(owner_user=curr_user.id).count();
            mediaFile = form.cleaned_data[ 'photo' ];
            newNameFile = curr_user.username + "-" + str(curr_user.id) + "-" + str(post_user);
            fs = FileSystemStorage()
            filename = fs.save(newNameFile, mediaFile)
            uploaded_file_url = fs.url(filename)
            photo = uploaded_file_url;
            description = form.cleaned_data[ 'description' ];
            newPost = Post( photo = photo, description = description, owner_user = curr_user );
            newPost.save();
            return redirect('profile',curr_user.username)
        else:
            context = { 'curr_user' : curr_user, 'form' : form }
            return render(request, 'uploadPhoto.html', context)
    else:
        form = PostForm()
        context = { 'curr_user' : curr_user, 'form' : form }
        return render(request, 'uploadPhoto.html', context)

@login_required
def search( request ):
    curr_user = request.user
    if request.method == 'POST':
        query = request.POST['search']
        try:
            user_list = User.objects.filter(username__icontains=query)
        except User.DoesNotExist:
            user_list = None
        context = { 'curr_user' : curr_user, 'user_list' : user_list }
        return render(request, 'search.html', context)
    else:
        context = { 'curr_user' : curr_user }
        return render(request, 'search.html', context)

def follow( request, _username ):
    to = User.objects.get(username=_username)
    fo = Follow.objects.create( from_user = request.user.myuser, to_user = to.myuser )
    request.user.myuser.follow = fo
    return redirect('profile',to.username)

def unfollow(request, _username):
    to = User.objects.get(username=_username)
    row = Follow.objects.filter( from_user = request.user.myuser, to_user = to.myuser )
    row.delete()
    return redirect('profile', to.username)

def doLike(request, id_photo):
    curr_user = request.user
    post = Post.objects.get(pk = id_photo)
    if not Like.objects.filter(user = curr_user, post = post).exists():
        new_like = Like(user = curr_user, post = post)
        new_like.save()
    return redirect('home')

def removeLike(request, id_photo):
    curr_user = request.user
    post = Post.objects.get(pk = id_photo)
    if Like.objects.filter(user = curr_user, post = post).exists():
        Like.objects.filter(user = curr_user, post = post).delete()
    return redirect('home')

def doComment(request, id_photo):
    comment = request.POST['comment']
    curr_user = request.user
    post = Post.objects.get(pk = id_photo)
    new_comment = Comment(text = comment, user = curr_user, post = post)
    new_comment.save()
    return redirect('home')
