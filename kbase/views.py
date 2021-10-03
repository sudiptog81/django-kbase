from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import Http404

from kbase.forms import CreateArticleForm, CreateCategoryForm, RegistrationForm, LoginForm
from kbase.models import Article, Category


def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is None:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })
        login(request, user)
        return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form
    })


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        newuser = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        newuser.set_password(request.POST['password'])
        try:
            newuser.save()
            login(request, newuser)
            return redirect('/')
        except:
            form = RegistrationForm(request.POST)
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {
        'form': form
    })


@login_required
def signout(request):
    logout(request)
    return redirect('/')


def articles(request):
    articles = Article.objects.all().order_by('-created_on')
    return render(request, 'articles.html', {'articles': articles})


def search(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
        ).order_by('-created_on')
    return render(request, 'search.html', {'articles': articles, 'query': query})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def article(request, slug):
    def get_queryset(slug):
        if slug:
            queryset = Article.objects.filter(
                Q(slug__iexact=slug)
            ).first()
            if not queryset:
                raise Http404()
        return queryset

    article = get_queryset(slug)
    categories = article.categories.all()

    return render(request, 'article.html', {'article': article, 'categories': categories})


def category(request, name):
    def get_queryset(name):
        if name:
            queryset = Article.objects.filter(categories__name__iexact=name)
            if not queryset:
                raise Http404()
        return queryset

    articles = get_queryset(name)

    return render(request, 'category.html', {'articles': articles, 'category': name})


@login_required
def create_article(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.contributor = request.user
            article.save()
            article.categories.add(*form.cleaned_data['categories'])
            print(article)
            return redirect('/')
    else:
        form = CreateArticleForm()

    return render(request, 'create_article.html', {'form': form})


@login_required
def update_article(request, slug):
    instance = get_object_or_404(Article, slug=slug)
    form = CreateArticleForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(instance.get_absolute_url())
    return render(request, 'update_article.html', {'form': form})


@login_required
def delete_article(request, slug):
    if request.method == 'POST':
        instance = get_object_or_404(Article, slug=slug)
        if not instance:
            raise Http404()
        instance.delete()
        return redirect('/articles')


@login_required
def create_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateCategoryForm()

    return render(request, 'create_category.html', {'form': form})


def not_found(request, exception):
    if exception:
        code = exception.get('status_code')
    else:
        code = 404
    return render(request, '404.html', {'status': code}, status=code)
