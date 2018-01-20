from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from . models import *
from .forms import PostCreateForm, SignUpForm,CreateAuthor
from django.contrib.auth.models import User
from django.contrib import messages

def post_list(request):
    post = articale.objects.all().order_by('-created_date')
    search = request.GET.get('q')
    if search:
        post = post.filter(
        Q(title__icontains=search)|
        Q(articale_body__icontains=search)
        )
    paginator = Paginator(post, 4)
    page = request.GET.get('page')
    total_post = paginator.get_page(page)
    context = {'post':total_post}
    template_name = 'post_list01.html'
    return render(request,template_name,context)

def get_author(request, name):
    posted_by = get_object_or_404(User, username=name)
    auth = get_object_or_404(author, name=posted_by.id)
    post = articale.objects.filter(article_author=auth.id)
    context = {'auth':auth, 'post':post}
    template_name ='profile.html'
    return render(request, template_name, context)

def post_details(request, id):
    post = get_object_or_404(articale, pk = id)
    first = articale.objects.first()
    last = articale.objects.last()
    related_post = articale.objects.filter(category=post.category).exclude(id=id)[:4]
    context = {'post':post, 'first':first, 'last':last, 'related_post':related_post}
    template_name = 'post_details01.html'
    return render(request, template_name, context)

def post_category(request, name):
    cat_id = get_object_or_404(category, name=name)
    post = articale.objects.filter(category=cat_id)
    context = {'post':post, 'cat_id':cat_id}
    template_name = 'category.html'
    return render(request, template_name, context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    else:
        if request.method=='POST':
            user=request.POST.get('name')
            password=request.POST.get('pass')
            auth = authenticate(request,username=user,password=password)
            if auth is not None:
                login(request,auth)
                return redirect('post_list')
            else:
                messages.add_message(request, messages.ERROR, 'Provide valid username and password')
    template_name = 'login.html'
    return render(request,template_name)

def user_logout(request):
    logout(request)
    template_name = 'logout.html'
    return render(request,template_name)

def post_create(request):
    if request.user.is_authenticated:
        var = get_object_or_404(author,name=request.user.id)
        form = PostCreateForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author=var
            instance.save()
            return redirect('post_list')
        template_name='form.html'
        context = { 'form':form}
        return render(request,template_name,context)
    else:
        return redirect('login')

def post_update(request,id):
    if request.user.is_authenticated:
        var = get_object_or_404(author,name=request.user.id)
        post=get_object_or_404(articale,id=id)
        form = PostCreateForm(request.POST or None,request.FILES or None,instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author=var
            instance.save()
            messages.success(request,'Post is updated successfully')
            return redirect('profile')
        template_name='form.html'
        context = { 'form':form}
        return render(request,template_name,context)
    else:
        return redirect('login')

def post_delete(request,id):
    if request.user.is_authenticated:
        post=get_object_or_404(articale,id=id)
        post.delete()
        return redirect('profile')
    else:
        return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        user=get_object_or_404(User,id=request.user.id)
        author_profile=author.objects.filter(name=user.id)
        if author_profile:
            authorUser=get_object_or_404(author,name=request.user.id)
            post=articale.objects.filter(article_author=authorUser.id)
            template_name='user_profile.html'
            context={'post':post,'user':authorUser}
            return render(request,template_name,context)
        else:
            form=CreateAuthor(request.POST or None,request.FILES or None)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.name=user
                instance.save()
                return redirect('profile')
            context = {'form':form}
            template_name = 'createauthor.html'
            return render(request,template_name,context)
    else:
        return redirect('login')

def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,'Signup is successfully complated')
        return redirect('login')
    template_name = 'signup.html'
    context={'form':form}
    return render(request,template_name,context)
