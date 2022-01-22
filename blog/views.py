from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
# Create your views here.
def homeBlog(request):
    allPost=Post.objects.all()
    context={"allpost":allPost}
    return render(request,"blog/homeBlog.html",context)
def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    post.views=post.views+1
    post.save()
    comments=BlogComment.objects.filter(post=post)
    context={"Post":post,"comment":comments,"user":request.user}
    return render(request,"blog/blogPost.html",context)
def postComment(request):
    if request.method=="POST":
        comment = request.POST.get('comment')
        user =request.user
        postsno=request.POST.get('postSno')
        post=Post.objects.get(sno=postsno)
        Comments=BlogComment(comment=comment,user=user,post=post)
        Comments.save()
        messages.success(request, "Your comment has been posted successfully")
    return redirect('/blog/{post.slug}')