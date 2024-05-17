from django.shortcuts import render,get_object_or_404
from .cart import Cart
from core.models import package
from django.http import JsonResponse


def cart_summary(request):
    cart=Cart(request)
    cart_packages=cart.getpack
    adults_num=cart.getamount
    totals=cart.totals()
    return render(request,'checkout.html',{'cart_package':cart_packages,'adults_num':adults_num,'total':totals})
def cart_add(request):
   
    cart=Cart(request)
    if request.POST.get('action')=='post':
        package_id=int(request.POST.get('package_id'))
        adult_no=int(request.POST.get('package_amount'))
        print(adult_no)
        Package=get_object_or_404(package,id= package_id)
        cart.add(package=Package,quantity=adult_no)

        amount=cart.__len__()


        response=JsonResponse({'amount':amount})
        return response

    






def cart_delete(request):
     cart=Cart(request)
     if request.POST.get('action')=='post':
        package_id=int(request.POST.get('package_id'))
        cart.delete(package=package_id)
        response=JsonResponse({'id':package_id})
        return response
def cart_update(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        package_id=int(request.POST.get('package_id'))
        adult_no=str(request.POST.get('package_amounts'))
        print(adult_no)
        cart.update(package=package_id,quantity=adult_no)
        response=JsonResponse({'amount':adult_no})
        return response
        # return redirect('summary.html')