from django import forms
# 현재 경로의 models에서 모델을 가져옴
from .models import Facebook, Comment

# Model Form (모델 폼)
class FacebookForm(forms.ModelForm):
	class Meta:
		model = Facebook
		fields = '__all__'
# 		fields = ['title', 'content'] # '__all__' 설정시 전체 필드 추가

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment',]
		