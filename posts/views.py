from django.shortcuts import render, redirect
from .forms import FacebookForm, CommentForm
from .models import Facebook, Comment

# Create your views here.
def list(request):
    posts = Facebook.objects.all()
    comment_form = CommentForm()
    return render(request, 'posts/list.html', {"posts":posts, "comment_form":comment_form})
    
def create(request):
    if request.method == "POST":
        form = FacebookForm(request.POST)
        if form.is_valid():
            form.save()
            # 서버 최상단의 posts로 가려면 /posts/ 앞에 / 필요
            return redirect("/posts/")
    else:
        form = FacebookForm()
        # form.save()
        return render(request, 'posts/create.html', {"form":form})

def delete(request, id):
    post = Facebook.objects.get(id=id)
    post.delete()
    return redirect("posts:list")

def update(request, id):
    post = Facebook.objects.get(id=id)
    if request.method == "POST":
        form = FacebookForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
        
    else:
        # 인스턴스라는 항목에 넣어주기 위해
        form = FacebookForm(instance=post)
        return render(request, 'posts/update.html', {"form":form})
    # form.save()
    
def comment_new(request,id): # 사실 POST방식은 필요하지 않습니다,,
    # 어디에 속해있는 정보를 달기
    facebook = Facebook.objects.get(id=id)
    if request.method == 'POST':
        # 여기서 commentForm이 하는 일은?
        # 사용자가 입력 할 수 있도록 만들어줌 + (데이터를 입력하면) 입력한 데이터를 받아야됨.
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # 정보를 저장해야되는데 그 전에 id값도 필요하니까 잠시 멈춰봐!
            comment = comment_form.save(commit=False)
            # 어떤 게시물에 속해있는지에 대한 정보가 fb이 가지고있음.
            comment.facebook = facebook
            comment.save()
            return redirect('posts:list')
            # 위와 같은 문장이지만, 또 posts를 모두 가져와야되는 코드+가 필요
            # return render(request, "posts/list.html",{'posts':posts})
            
def comment_delete(request, id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('posts:list')