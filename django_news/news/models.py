from django.db import models
    
class Tag(models.Model):
    tag_name = models.CharField(max_length = 15)
    
    def __str__(self) -> str:
        return f'{self.id}. {self.tag_name}'
    
# Create your models here.
class News(models.Model):
    header = models.CharField(max_length = 255)
    text = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    tags = models.ManyToManyField(Tag, null = True)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)
    
    def __str__(self) -> str:
        return f'{self.id}. {self.header}'
    
    def dict(self) -> dict:
        return {
            'id': self.id,
            'header': self.header,
            'image': self.image.url,
            'text': self.text,
            'tags': list([tag.tag_name for tag in self.tags.all()]) if self.tags.exists else [],
            'likes': self.likes,
            'dislikes': self.dislikes,
            'views': self.views,
        }