from django.db import models
from django_markdown.models import MarkdownField
from django.urls import reverse

class PostQuerySet(models.QuerySet):
	def publié(self):
		return self.filter(publier=True)

class Post(models.Model):
	titre = models.CharField(max_length=200)
	contenue = models.TextField()
	slug = models.SlugField(max_length=250, unique=True)
	publier = models.BooleanField(default=True)
	créé = models.DateTimeField(auto_now_add=True)
	modifié = models.DateTimeField(auto_now=True)

	objects = PostQuerySet.as_manager()

	def __str__(self):
		return self.titre

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={"slug":self.slug})


	verbose_name='post'
	verbose_name_plural = 'posts'
	ordering = ["-créé"]