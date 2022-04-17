from django.shortcuts import render, get_object_or_404
from .models import Blog_post


def all_blogs(request):
    my_posts = Blog_post.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'all_blog_posts':my_posts})

def detail(request, blog_id):
    blog = get_object_or_404(Blog_post, pk = blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})




# def home(request):
#     my_projects = Project.objects.all()
#     return render(request, 'portfolio/home.html', {'projects':my_projects})
