from django.db import models
from django.contrib.auth.models import User 



# Group Model 
class ChatGroup(models.Model):
    group_name = models.CharField(max_length=255 , unique=True)


    def __str__(self):
        return self.group_name 



# Group Messages Model 
class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup,related_name = 'chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"self.author" 
    
    class Meta:
        ordering = ['-created_at']