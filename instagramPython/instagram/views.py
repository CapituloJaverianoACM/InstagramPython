from django.shortcuts import render,redirect
from instagram.models import User,Post
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render(request, 'instagram/index.html')

def login(request):
    if request.method == 'POST':
        curr_nickName = request.POST['nickName']
        curr_password = request.POST['password']
        auten=User.objects.all().filter(nickname=curr_nickName,password=curr_password)
        if auten:
            return redirect('mainPage', id_user = auten[0].id)
        else:
            #COLOCAR ALGO PARA MOSTRAR ERRORES
            return render(request, 'instagram/login.html')
    else:
        return render(request, 'instagram/login.html')

def createUser(request):
    curr_email = request.POST['email']
    curr_name = request.POST['name']
    curr_nickName = request.POST['nickName']
    curr_password = request.POST['password']
    user_object = User(name=curr_name, nickname = curr_nickName, password = curr_password, email = curr_email)
    user_object.save()
    return redirect('login')

def getAllPhotosFollow( id_user ):
    user = User.objects.get(pk=id_user)
    ids_follow = user.follow.all();
    #print ids_follow;

def mainPage(request, id_user):
    curr_user = User.objects.get(pk=id_user)
    photo_list = "";
    context = { 'curr_user' : curr_user, 'photo_list' : photo_list }
    return render(request, 'instagram/mainPage.html', context)

def profile(request, id_user):
    curr_user = User.objects.get(pk=id_user)
    media_user = Post.objects.filter( user_id = id_user );
    #seguidores =
    context = { 'curr_user' : curr_user, 'media_user' : media_user }  # Comillas es el nombre en el HTML, variable
    return render(request, 'instagram/profile.html', context)

def uploadPhoto(request, id_user):
    curr_user = User.objects.get(pk=id_user)
    context = { 'curr_user' : curr_user }
    return render(request, 'instagram/uploadPhoto.html', context)

def uploadFile(request, id_user):
    curr_user = User.objects.get(pk=id_user)
    post_user = Post.objects.filter(user_id=id_user).count();
    mediaFile = request.FILES[ 'photo' ];
    newNameFile = curr_user.nickname + "-" + id_user + "-" + str(post_user);
    fs = FileSystemStorage()
    filename = fs.save(newNameFile, mediaFile)
    uploaded_file_url = fs.url(filename)
    photo = uploaded_file_url;
    description = request.POST[ 'description' ];
    newPost = Post( photo = photo, description = description, user_id = curr_user );
    #newPost.save();
    media_user = Post.objects.filter( user_id = id_user );
    context = { 'curr_user' : curr_user, 'media_user' : media_user }
    return render(request, 'instagram/profile.html', context)

def search( request, id_user ):
    curr_user = User.objects.get(pk=id_user)
    if request.method == 'POST':
        query = request.POST['query']
        try:
            user_list = User.objects.filter(nickname__icontains=query)
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
