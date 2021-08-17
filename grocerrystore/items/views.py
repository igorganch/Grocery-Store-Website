
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import Http404


from .models import *
from .forms import cartForm, checkoutForm


def products_everything(req):
    print("Im in this shit")
    temp = Item.objects.all()
    return render(req, "products.html" , {
        "items" : temp,

    })

def products_category(req,category_):
    temp = Item.objects.filter(category = category_ )

           
    return render(req, "products.html", {
        'items' : temp,   
     })

def checkout(req):
    print("in chckout")
    try: 
        customer = req.user.customer
    except:
        device = req.COOKIES['device']
        customer= Customer.objects.get_or_create(device = device)
        customer = Customer.objects.get(device = device)
    
    cart = Order.objects.get_or_create(customer = customer, complete = False)
    cart = Order.objects.get(customer = customer, complete = False)

    return render( req , 'checkout.html',{ 
    'cart' : cart,})


def home(req):
    temp = Item.objects.all()
    items_ = temp[0:6]
    return render(req, "home.html", {
        'items' : items_,
    })



def item_detail(req, item_id):

    print("in here")
    try: 
        temp = Item.objects.get( id = item_id)
    except Item.DoesNotExist:
        raise Http404("Item not found ")

    return render(req, 'item_detail.html', {
        'item' : temp,
    })


## CART METHODS 
def cart_add(req, item_id):
    item = Item.objects.get( id = item_id)           
    
    if req.method =='POST':
        
        form = cartForm(req.POST)
        if form.is_valid():
            
            print("inside POST ")
            try:  
                print("inside try ")
                customer = req.user.customer
            except:
                device = req.COOKIES['device']
                customer= Customer.objects.get_or_create(device = device)
                customer = Customer.objects.get(device = device)
    
        cart = Order.objects.get_or_create(customer = customer, complete = False)
        cart = Order.objects.get(customer = customer, complete = False)
        
        orderItem = OrderItem.objects.get_or_create(order=cart, item = item)

        orderItem[0].quantity = form['quantity'].value()
        orderItem[0].save()
        
        return HttpResponse(200)


def cart_clear(req):
    print("-----------------------------------------")
    print("-----------------------------------------")
    print("DSIFGHSDIOHFODSAHFOLSAHFOLSAHOLFHD IN HGERE")
    print("-----------------------------------------")

    try:
        customer = req.user.customer
    except:
         device = req.COOKIES['device']
         customer= Customer.objects.get_or_create(device = device)
         customer = Customer.objects.get(device = device)

    cart = Order.objects.get(customer = customer, complete = False)
    items = OrderItem.objects.filter(order = cart).delete()
    return redirect("/cart/cart-detail/")
    

def cart_remove(req, item_id):

    try:
        customer = req.user.customer
    except:
         device = req.COOKIES['device']
         customer= Customer.objects.get_or_create(device = device)
         customer = Customer.objects.get(device = device)

    cart = Order.objects.get(customer = customer, complete = False)

    query = Item.objects.get( id = item_id) 
    item = OrderItem.objects.get(order = cart, item = query)
    item.delete()

    return HttpResponse(200)

def cart_increment(req, item_id):

    try:
        customer = req.user.customer
    except:
         device = req.COOKIES['device']
         customer= Customer.objects.get_or_create(device = device)
         customer = Customer.objects.get(device = device)

    cart = Order.objects.get(customer = customer, complete = False)
    print("-----------------------------------------")
    print("-----------------------------------------")
    print("DSIFGHSDIOHFODSAHFOLSAHFOLSAHOLFHD IN HGERE")
    print("-----------------------------------------")

    query = Item.objects.get( id = item_id) 
    item = OrderItem.objects.get(order = cart, item = query)
    item.quantity = item.quantity + 1
    item.save()
    return HttpResponse(200)



def cart_decrement(req, item_id):
    try:
        customer = req.user.customer
    except:
         device = req.COOKIES['device']
         customer= Customer.objects.get_or_create(device = device)
         customer = Customer.objects.get(device = device)

    cart = Order.objects.get(customer = customer, complete = False)
    print("-----------------------------------------")
    print("-----------------------------------------")
    print("DSIFGHSDIOHFODSAHFOLSAHFOLSAHOLFHD IN HGERE")
    print("-----------------------------------------")

    query = Item.objects.get( id = item_id) 
    item = OrderItem.objects.get(order = cart, item = query)
    item.quantity = item.quantity - 1
    print(item.quantity)
    if item.quantity == 0:
        print("inside remove ")
        item.delete()
    else:     
        item.save()
    return HttpResponse(200)

def cart_detail(req):
    try: 
        customer = req.user.customer
    except:
        device = req.COOKIES['device']
        customer= Customer.objects.get_or_create(device = device)
        customer = Customer.objects.get(device = device)
    
    cart = Order.objects.get_or_create(customer = customer,  complete = False)
    cart = Order.objects.get(customer = customer,  complete = False)

    return render( req , 'cart.html',{ 
    'cart' : cart,})


def orders(req):
    orders = Order.objects.filter(complete = True)
    print(orders)
    return render( req , 'orders.html',{ 
            'orders' : orders,})

def checkout_complete(req):
    if req.method =='POST':
        form = checkoutForm(req.POST)
        if form.is_valid():
            print("name - " + form['name'].value() + "email  - " + form['email'].value())
            try: 
                customer = req.user.customer
            except:
                device = req.COOKIES['device']
                customer= Customer.objects.get_or_create(device = device)
                customer = Customer.objects.get(device = device)
            customer.name = form['name'].value() 
            customer.email =  form['email'].value()
            customer.save()


            cart = Order.objects.get(customer = customer, complete = False)
            cart.complete = True 
            cart.save()
            print(cart.customer.name)
            return redirect("/orders/")



