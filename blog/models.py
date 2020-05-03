from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]
    
    def pub_date_pretty(self):
        return self.publication_date.strftime('%b %e %Y')