from django.shortcuts import render,get_object_or_404,redirect
from .models import News, Category,Comment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import CommentForm
from django.views.decorators.http import require_POST
from django.conf import settings
import redis

r = redis.Redis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,
                db=settings.REDIS_DB)


def base(request):
    all_news = News.published.prefetch_related('attachments').all()  # Prefetch attachments for efficiency
    categories = Category.objects.all()
    latest_news = News.published.prefetch_related('attachments').all()[:4]
    return render(request, 'news/base.html', {
        'all_news': all_news,
        'categories': categories,
        'latest_news': latest_news,
    })



@login_required
def news_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    all_news = News.published.prefetch_related('attachments').all()
    
    
    paginator = Paginator(all_news, 5)
    page_number = request.GET.get('page', 1) 
    page_obj = paginator.get_page(page_number) 
    if category_slug:
        category = get_object_or_404(Category, category_slug=category_slug)
        all_news = all_news.filter(category=category)
        paginator = Paginator(all_news, 5)  
        page_obj = paginator.get_page(page_number)

    return render(request, 'news/list.html', {
        'page_obj': page_obj,  
        'categories': categories,
        'category': category,
        'all_news':all_news,
    })



@login_required
def news_detail(request, id):
    latest_news = News.published.prefetch_related('attachments').all()[:3]
    news = get_object_or_404(News, id=id, status=News.Status.PUBLISHED)
    comments = news.comments.filter(active=True)
    form = CommentForm()
    user_key = f"user:{request.user.id}" if request.user.is_authenticated else f"anon:{request.session.session_key}"

   
    news_views_key = f"news:{id}:views"

  
    r.sadd(news_views_key, user_key)

    
    views = r.scard(news_views_key)

    return render(request, 'news/detail.html', {'news': news, 'comments': comments, 'form': form,'latest_news':latest_news,'views':views})

@require_POST
@login_required
def news_comment(request, news_id):
    news = get_object_or_404(News, id=news_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.news = news
        comment.author = request.user
        comment.save()
        return redirect('news:news_detail', id=news.id)
    return render(request, 'news/detail.html', {'news': news, 'form': form})