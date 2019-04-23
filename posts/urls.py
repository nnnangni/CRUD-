from django.urls import path
# 현재폴더(urls.py가 있는 폴더)->posts에 있는 views.py의 파일을 가지고와서 
# 그 안에 list를 실행
from . import views
# app_name => 앱이 여러개로 분리되는 것을 대비해서 적어줌.
app_name = 'posts'

urlpatterns = [
    # name => 변수 안에 이름을 정해줘서 나중에 바꾸게 쉽게끔
    path('', views.list, name="list"),
    path('create/', views.create, name="create"),
    path('<int:id>/delete', views.delete, name="delete"),
    path('<int:id>/update', views.update, name="update"),
    path('<int:id>/comment_new', views.comment_new, name="comment_new"),
    path('<int:id>/comment/<int:comment_id>/delete', views.comment_delete, name="comment_delete"),
    ]