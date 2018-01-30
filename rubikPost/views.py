from django.shortcuts import render, get_object_or_404
from .models import Author, Tag, Category, Post

# Create your views here.

def post_list(request):
	'''Shows List of posts in Database'''
	posts = Post.objects.all()
	tags = Tag.objects.all()
	return render(request, 'rubikPost/post_list.html', {'posts':posts, 'tags': tags})

def post_detail(request, pk, post_slug):
	'''Shows the particular post'''
	#post = Post.objects.get(pk=pk)
	post = get_object_or_404(Post, pk=pk)
	tags = Tag.objects.all()
	return render(request, 'rubikPost/post_detail.html', {'post': post, 'tags':tags,})


def basicCubing(request):
	posts = Post.objects.filter(category__name__icontains="basic")
	tags = Tag.objects.all()
	return render(request, 'rubikPost/basic_three.html', {'posts':posts, 'tags':tags,})

def advancedCubing(request):
	posts = Post.objects.filter(category__name__icontains="advance")
	tags = Tag.objects.all()
	return render(request, 'rubikPost/advance_three.html', {'posts':posts, 'tags':tags,})

def basicVideos(request):
	'''shows list of video tutorials'''
	tags = Tag.objects.all()
	return render(request, 'rubikPost/basic_videos.html', {'tags':tags})

def advancedVideos(request):
	'''shows list of video tutorials'''
	tags = Tag.objects.all()
	return render(request, 'rubikPost/advanced_videos.html', {'tags':tags})


def about(request):
	''' Shows about me '''
	return render(request, 'rubikPost/about.html')

