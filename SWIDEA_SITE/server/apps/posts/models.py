from django.db import models
from apps.devtools.models import Tool


# Create your models here.
class Post(models.Model):
    title = models.CharField("제목", max_length=24)
    # 이미지
    photo = models.ImageField("이미지", blank=True, upload_to="posts/%Y%m%d")
    # 아이디어 설명
    content = models.CharField("설명", max_length=100)
    # 아이디어 관심도
    interest = models.IntegerField("관심도", default=0)
    # 예상 개발툴
    tools = models.ForeignKey(
        Tool,
        on_delete=models.CASCADE,
        null=True,
    )
    # 찜하기
    marked = models.BooleanField("즐겨찾기", default=False, null=True)
    # 생성 시각, 수정 시각
    created_date = models.DateTimeField(
        "작성일",
        auto_created=True,
        auto_now_add=True,
        null=True,
    )
    updated_date = models.DateTimeField(
        "수정일",
        auto_created=True,
        auto_now=True,
        null=True,
    )

    marked = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title
