from django.shortcuts import render, redirect
from django.core.mail import send_mail
from app.forms import EmailForm
from .models import *
from django.core.paginator import Paginator

def index(request):from django.shortcuts import render, redirect
from django.core.mail import send_mail
from app.forms import EmailForm
from .models import *
from django.core.paginator import Paginator

def index(request):
    if request.method == 'POST':
        if 'mail' in request.POST:
            form = EmailForm(request.POST)
            mail = request.POST['mail']

            send_mail(
                'Ваша почту одобрена!!!',
                'Поздравляем ваша почта успешно потдверждена.',
                'seogram2022@gmail.com',
                [mail],
                fail_silently=False)

            if form.is_valid():
                form.save()
                return redirect('/')
        
                # redirect('/')
    form = EmailForm()
            
    return render(request,'index.html', context={'form':form})



def about(requset):
    return render(requset, template_name='about.html')

def services(request):
    return render(request, template_name='service.html')

def contact(requets):
    return render(requets, template_name='contact.html')

def blog(request):
    bl = Blog.objects.all()
    bl_paginator = Paginator(bl, 3)
    page_num = request.GET.get('page')
    page = bl_paginator.get_page(page_num)
    context = {
        'bl':bl,
        'page':page,
        'count':bl_paginator.count
    }
    return render(request,'blog.html', context=context)

def blog_details(request):
    return render(request, template_name='blog-details.html')

    if request.method == 'POST':
        if 'mail' in request.POST:
            form = EmailForm(request.POST)
            mail = request.POST['mail']

            send_mail(
                'Ваша почту одобрена!!!',
                'Поздравляем ваша почта успешно потдверждена.',
                'seogram2022@gmail.com',
                [mail],
                fail_silently=False)

            if form.is_valid():
                form.save()
                return redirect('/')
        
                # redirect('/')
    form = EmailForm()
            
    return render(request,'index.html', context={'form':form})



def about(requset):
    return render(requset, template_name='about.html')

def services(request):
    return render(request, template_name='service.html')

def contact(requets):
    return render(requets, template_name='contact.html')

def blog(request):
    bl = Blog.objects.all()
    bl_paginator = Paginator(bl, 3)
    page_num = request.GET.get('page')
    page = bl_paginator.get_page(page_num)
    context = {
        'bl':bl,
        'page':page,
        'count':bl_paginator.count
    }
    return render(request,'blog.html', context=context)

def blog_details(request):
    return render(request, template_name='blog-details.html')
