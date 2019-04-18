from django.shortcuts import render, redirect
from .forms import FacebookForm
from .models import Facebook

# Create your views here.
def list(request):
    posts = Facebook.objects.all()
    return render(request, 'posts/list.html', {"posts":posts})
    
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
    if request.method == "POST":
        pass
    else:
        post = Facebook.objects.get(id=id)
        # 인스턴스라는 항목에 넣어주기 위해
        form = FacebookForm(instance=post)
        return render(request, 'posts/update.html', {"form":form})
    # form.save()
    
    
    