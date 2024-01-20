from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    
class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE) # 1:N 관계일 경우, N이 되는 쪽에 ForeignKey를 해줘야 함. to와 on_delete는 필수고 to에는 1의 클래스 이름을 넣자.cc 
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)