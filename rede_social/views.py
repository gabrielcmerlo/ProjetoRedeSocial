from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Friendship, User
from .forms import PostForm  # Criaremos este form depois

@login_required
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    
    # Lista de amigos em ordem alfabética
    friendships = Friendship.objects.filter(user=request.user)
    friends = [friendship.friend for friendship in friendships]
    friends = sorted(friends, key=lambda x: x.username)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'pages/index.html', {
        'posts': posts,
        'friends': friends,
        'form': form
    })

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'pages/post_detail.html', {'post': post})

@login_required
def add_friend(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        friend = get_object_or_404(User, username=username)
        Friendship.objects.get_or_create(user=request.user, friend=friend)
        return redirect('home')
    return render(request, 'pages/add_friend.html')

@login_required
def messages(request):
    return render(request, 'pages/messages.html')