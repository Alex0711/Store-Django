class Cart:
    def __init__(self, request):
        self.request=request 
        self.session=request.session #acá guardo la sesión
        cart=self.session.get('cart') #busco si en la sesión hay un carro
        if not cart: #si no hay carro
            self.cart=self.session['cart']={} #creo uno vacío 
        else:
            self.cart=cart #sino, aputo a ese carro que ya está creado
    
    def add_to_cart(self, product):
        if(str(product.id) not in self.cart.keys()):
            self.cart[product.id]={
                'product_id':product.id,
                'title':product.title,
                'price':product.price,
                'count':1,
                'image':product.image.url,
            }
        else:
            self.cart[str(product.id)]['count']+=1
            self.cart[str(product.id)]['price']+= product.price
        self.save_cart()

    def save_cart(self):
        self.session['cart']=self.cart #igualo el carro de la sesión con el que tengo creado
        self.session.modified=True  #y lo guardo

    def delete_products(self, product):
        product.id = str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.save_cart()

    def delete_a_product(self, product): 
        """product.id = str(product.id)
        if product.id in self.cart:
            self.cart[product.id]-=1
            self.save_cart()"""
        for key, value in self.cart.items():
            if key == str(product.id):
                value['count']=value['count']-1
                if value['count']<1:
                    self.delete_products(product=product)
                else:
                    self.save_cart()
                break

    def clean_cart(self):
        self.session['cart']={}
        self.session.modified=True