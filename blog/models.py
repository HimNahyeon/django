from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 작성자는 나중에


    def __str__(self): #게시판 제목 출력설정
        return f'[{self.pk}]{self.title}'