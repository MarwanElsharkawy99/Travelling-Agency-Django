from django.urls import path
from . import views
urlpatterns = [
    path('summary/',views.cart_summary,name='summary'),
    path('add/',views.cart_add,name='add'),
    path('delete/',views.cart_delete,name='delete'),
    path('update/',views.cart_update,name='update'),
    
]