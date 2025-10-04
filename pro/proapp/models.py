from django.db import models

# Create your models here.
class NewCotegory(models.Model):
    cotegory_name = models.CharField(max_length=64)
    cotegory_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cotegory_name

class News(models.Model):
    new_name = models.CharField(max_length=256)
    new_description = models.TextField()
    new_cotegory = models.ForeignKey(NewCotegory, on_delete=models.CASCADE)
    news_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.new_name