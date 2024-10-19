from django.shortcuts import render
from django.core.paginator import Paginator
from task.models import *




# Create your views here.

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'paginator': paginator,
               'page_number': page_number, 'page_obj': page_obj}
    return render(request, 'index.html', {'page_obj': page_obj})
