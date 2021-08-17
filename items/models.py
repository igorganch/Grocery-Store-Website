from django.db import models
from django.contrib.auth.models import User 


class Item(models.Model):
    CATEGORY_CHOICES = [('meats','meats'),('bakery','bakery'),('produce','produce'),('dairy','dairy'),('other','other')]
    name = models.CharField(max_length=25, blank=False)
    image = models.ImageField(blank = True , null = True )
    supplier = models.CharField(max_length=30, blank = False )
    price = models.DecimalField(max_digits= 6, decimal_places=2,  blank = False)
    dateAdded = models.DateTimeField()
    category = models.CharField( max_length=20, choices=CATEGORY_CHOICES, default= 'other')
    def __str__(self):
        return self.supplier + " - " +  self.name





class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	device = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		if self.name:
			name = self.name
		else:
			name = self.device
		return str(name)




class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 


class OrderItem(models.Model):
	item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.item.price * self.quantity
		return total
