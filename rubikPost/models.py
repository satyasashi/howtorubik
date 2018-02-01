from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField


from django.utils.text import slugify

# Signals. Does a task Before saving something and after saving (Pre_save & Post_save)
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator


# Create your models here.
class Author(models.Model):
	name 			=	models.CharField(max_length=100, unique=True)
	email			=	models.EmailField(unique=True)
	active			=	models.BooleanField(default=False)
	created_on 		=	models.DateTimeField(auto_now_add=True)
	last_logged_in	=	models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Category(models.Model):
	name 	=	models.CharField(max_length=100, unique=True)
	slug 	=	models.SlugField(max_length=100, unique=True)
	author 	=	models.ForeignKey(Author)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('post_by_category', args=[self.slug])

class Tag(models.Model):
	name 	=	models.CharField(max_length=100, unique=True)
	slug 	=	models.SlugField(max_length=100, unique=True)
	author 	=	models.ForeignKey(Author)


	def __str__(self):
		return self.name

	def get_absolute_urL(self):
		return reverse('post_by_tag', args=[self.id, self.slug])


class Post(models.Model):
	title 		=	models.CharField(max_length=150)
	slug 		=	models.SlugField(unique=True, help_text="Slug will be generated automatically.")
	content 	=	RichTextField()
	pub_date	=	models.DateTimeField(auto_now_add=True)
	updated_on	=	models.DateTimeField(auto_now=True)
	author 		=	models.ForeignKey(Author)
	category 	=	models.ForeignKey(Category)
	tags 		=	models.ManyToManyField(Tag)

	def get_absolute_url(self):
		return reverse('post_detail', args=[self.id, self.slug])

	def __str__(self):
		return self.title

	# overriding the Model's save() method to create 'slug' when Saved/Updated
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)