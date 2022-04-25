from abc import abstractmethod
from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django.conf import settings

# User = get_user_model()

class CommonInfo(models.Model):
    # created_at = models.DateField(auto_now_add=True)
    # updated_at = models.DateField(auto_now=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Post(CommonInfo):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(null=True,blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True,blank=False,on_delete=models.SET_NULL)
        
 
   # коли видаляємо користувача, що необхідно зробити з постом?
   # null=False, on_delete=models.CASCADE --> каскадне видалення 
   # null=True, on_delete=models.SET_NULL --> найбільш підходить
   # null=False, on_delete=models.SET_DEFAULT, default = ... --> можно назначити admin, відповідно всі видалені пости користувачів будуть перезначатися адміном
   # null=False, on_delete=models.DO_NOTHING --> нічого не робити
  
    
    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        ordering = ("title", "user", "content")  
        


class Like(CommonInfo):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
        # "Post", null = False, blank =False, on_delete=models.CASCADE)
    user = models.ForeignKey(
                settings.AUTH_USER_MODEL, null = False, blank =False, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
    
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)