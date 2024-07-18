from django.db import models


# Create your models here.
class Tool(models.Model):
    title = models.CharField("이름", max_length=24)

    # 예상 개발툴
    kinds = models.CharField("종류", max_length=30, default="")

    # 개발도구 설명
    content = models.CharField("설명", max_length=100)

    def __str__(self):
        return self.title
