from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

        # 필드 레이블과 도움말 설정
        labels = {
            "username": "사용자 이름",
            "password1": "비밀번호",
            "password2": "비밀번호 확인",
        }
        help_texts = {
            "username": None,
        }
