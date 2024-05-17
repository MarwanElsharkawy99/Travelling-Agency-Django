from core.models import package


class Cart():
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get('session_key')
        if 'session_key' not in request.session:
            cart=self.session['session_key']={}
        self.cart=cart

    
    def add(self,package,quantity):
        package_id=str(package.id)
        package_quantity=str(quantity)
        if package_id in self.cart:
            pass
        else:
            self.cart[package_id]=int(package_quantity)


        self.session.modified=True

    def __len__(self):
        return len(self.cart)
    
    def getpack(self):
        package_ids=self.cart.keys()
        packages=package.objects.filter(id__in=package_ids)
        return packages
    
    def getamount(self):
        amount=self.cart
        return amount
    
    def update(self,package,quantity):
            package_id=str(package)
            adult_num=str(quantity) 

            our_cart=self.cart
            our_cart[package_id]=adult_num
            self.session.modified= True
            thing =self.cart
            return thing
    

    def delete(self,package):
        package_id=str(package)
        if package_id in self.cart:
            del self.cart[package_id]
            self.session.modified=True



    def totals(self):
        package_id=self.cart.keys()
        packages=package.objects.filter(id__in=package_id)
        number=self.cart
        cart_total=0
        for key,value in number.items():
            key=int(key)
            for i in packages:
                if i.id == key:
                    cart_total=cart_total+(i.price*int(value))



        return cart_total
            


