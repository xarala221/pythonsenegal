from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ("titre", "créé")
	prepopulated_fields = {"slug": ("titre",)}
admin.site.register(Post, PostAdmin)