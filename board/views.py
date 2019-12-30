from django.shortcuts import render, redirect, get_object_or_404
from .models import post
from django.core.paginator import Paginator


def posthome(req):
        posts=post.objects.all()
        post_list=post.objects.order_by('-created_at')
        paginator=Paginator(post_list,8)
        page=req.GET.get('page')
        blogs=paginator.get_page(page)
        return render(req,'boardhome.html',{'blogs':blogs,'posts': posts})

def postnew(req):
    return render(req,'postnew.html')

def postcreate(req):
    if req.method=='POST':
        one_memo=post()
        one_memo.title=req.POST['title']    
        one_memo.content=req.POST['content'] 
        one_memo.username=req.POST['username']
        one_memo.nickname=req.POST['nickname']

        if 'image' in req.FILES.keys():
                one_memo.image=req.FILES['image']
        one_memo.save()
    return redirect('/board')

def postedit(req,post_id):
    pot = get_object_or_404(post, pk=post_id)
    return render(req, 'postedit.html', {'post': pot})

def postshow(req,post_id):
    pot = get_object_or_404(post, pk=post_id)
    coments = pot.postcoment_set.all()
    return render(req,'postshow.html',{'post': pot,'coments':coments})

def postdelete(req,post_id):
    pot = get_object_or_404(post, pk=post_id)
    pot.delete()
    return redirect('/board')

def postupdate(req,post_id):
    pot = get_object_or_404(post, pk=post_id)
    pot.title = req.POST['title']
    pot.content = req.POST['content']
    if 'image' in  req.FILES.keys():  
        pot.image=req.FILES.get('image',False)
    pot.save()
    return redirect('/board/show/'+str(post_id))

def commentcreate(req,post_id):
    if (req.method == 'POST'):
        pot = get_object_or_404(post, id=post_id)
        pot.postcoment_set.create(title=req.POST['coment_content'],username=req.POST['username'])
        return redirect('/board/show/'+ str(post_id))

def commentdelete(req,post_id,comment_id):
    pot = get_object_or_404(post, pk=post_id)
    coments = pot.postcoment_set.get(id=comment_id)
    coments.delete()
    return redirect('/board/show/'+ str(post_id))

