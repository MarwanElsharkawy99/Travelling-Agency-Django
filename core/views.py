from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from core.models import  Day, package,blog
from .form import ContactForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def index(request):
    
    current_user=request.user
    pack=package.objects.all()[:3]

    return render(request, 'index.html',{'pack':pack,'user':current_user}
       
    )
    
def packages(request):
    
    packags=package.objects.all()
    
    return render(request,'shop.html',{'packages':packags})
    
    
    
def show_blog(request):
    blogs=blog.objects.all()
    return render(request,"blog.html",{'blog_item':blogs})


def details(request,id):
    package_details=get_object_or_404(package,pk=id)
    
    days = package_details.day.all()
    hotels=package_details.hotel.all()
    return render(request,'packages.html',{"pack_item":package_details,'day':days,'hotels':hotels})

def blog_details(request,id):
    blog_details=get_object_or_404(blog,pk=id)
    
    return render(request,'blog_details.html',{"blog_item":blog_details})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            print(name)

            # html = render_to_string('contact/emails/contactform.html', {
            #     'name': name,
            #     'email': email,
            #     'content': content
            # })

            send_mail(name, content, email, ['marwanelsharkawy99@gmail.com'])

            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form
    })


def customepackage(request):
    return render(request,'customPackages.html')

def search(request):
     if request.method=="POST":
        searched =  request.POST['searching']
        results=package.objects.filter(name__contains=searched)
        return render(request,'search.html',{'searched':searched,'results':results})
     else:
         return render(request,'search.html',{})
         


# def navbar(request):
#     return render(request,'navbar.html')

def about(request):
    return render(request,'about.html')

def whatsapp(request):
    return render(request,'whatsapp')