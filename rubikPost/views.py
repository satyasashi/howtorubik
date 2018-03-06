from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Author, Tag, Category, Post
from django.contrib import messages # for Flash Messages
from .forms import ContactForm
from django.core.mail import mail_admins # Feedback form sending Emails



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

def post_by_tag(request, tag_slug):
	''' Shows the post by tags '''
	tag = get_object_or_404(Tag, slug=tag_slug)
	tags= Tag.objects.all()
	posts = get_list_or_404(Post, tags=tag)
	context = {
		'tag': tag,
		'tags':tags,
		'posts': posts
	}
	return render(request, 'rubikPost/post_by_tag.html', context)

def basicCubing(request):
	posts = Post.objects.filter(category__name__icontains="basic").order_by("id")
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

# sidebox
def sidebox(request):
	tags = Tag.objects.all()
	return render(request, 'base.html', {'tags':tags})



# Feedback form view
def contact(request):
	if request.method == "POST":
		f = ContactForm(request.POST)

		if f.is_valid():
			name = f.cleaned_data['name']
			sender = f.cleaned_data['email']
			subject = "You have new Feedback from {}:{}".format(name, sender)
			message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])
			mail_admins(subject, message)

			f.save()
			messages.add_message(request, messages.INFO, "Feedback Submitted")
			return redirect('contact')
	else:
		f = ContactForm()
	return render(request, 'rubikPost/contact.html', {'form':f,})