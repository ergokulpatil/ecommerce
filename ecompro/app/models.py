from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES=(
    ('Maharashtra','Maharashtra'),
    ('Goa','Goa'),
    ('Bihar','Bihar'),
)


class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=200)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),

)


class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=200)
    category= models.CharField(choices=CATEGORY_CHOICES,max_length=10)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price



STATUS_CHOICES =(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('on the way','on the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),

)


class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS_CHOICES,max_length=29,default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

