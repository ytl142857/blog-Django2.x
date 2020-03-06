from django.db import models
from django.contrib.auth.models import User
from read_statistics.models import ReadNumExpandMethod
from mdeditor.fields import MDTextField


# Blog type
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.type_name


# Blog article
class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = MDTextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Blog: %s>' % self.title

    class Meta:
        ordering = ['-create_time']

