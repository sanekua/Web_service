from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pict')
    files = models.FileField(default='default.txt', upload_to='pdf')

    def __str__(self):
        return f'{self.user.username}Profile'


    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)






# class Prof(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     #image = models.ImageField(default='default.png', upload_to='profile_pict')
#     files = models.FileField(default='default.txt', upload_to='pdf')
#
#     def __str__(self):
#         return f'{self.user.username}Prof'