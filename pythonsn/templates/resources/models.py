from django.db import models

Book = "Livre"
Video = "Vidéo"
Article = "Article"


class Utility(models.Model):
    TYPE = (
        (Book, Book),
        (Video, Video),
        (Article, Article),
    )
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    resource_type = models.CharField(max_length=50, choices=TYPE, default=Book)
    link = models.URLField(null=True, blank=True)
    img_url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "resourcies"

    def __str__(self):
        return self.title
