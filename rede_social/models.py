from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  # Adicione este campo
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"

class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'friend')

    def __str__(self):
        return f"{self.user.username} - {self.friend.username}"
    
STATUS = {
    'SENDED':'SENDED',
    'REJECTED':'REJECTED',
    'APPROVED':'APPROVED'
}

import uuid
class Invite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    accept_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

# class ChatRoom(models.Model):
#     name = models.CharField(max_length=255)
#     user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#     user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')

# ChatRoom.objects.filter('user_1euser_2')

# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#     reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

# Message.objects.filter()