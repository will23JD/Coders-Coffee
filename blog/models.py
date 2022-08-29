from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """ Blog Model """
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ribbit_discussion")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='like_blog', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """ Comment Model """
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(User, max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
