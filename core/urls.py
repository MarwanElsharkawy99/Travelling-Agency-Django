from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('packages/',views.packages,name='packs'),
    path('<int:id>/',views.details,name='details'),
    path('blog/',views.show_blog,name='blog'),
    path('blog:<int:id>/',views.blog_details,name='blogs'),
    path('contact/',views.contact,name='contact'),
    path('costumepackage/',views.customepackage,name='costume'),
    path('search/',views.search,name='search'),
    # path('nav/',views.navbar,name='nav'),
    path('about/',views.about,name='about'),
    path('whatsapp/',views.whatsapp,name='whatsapp'),


    
     
    
]