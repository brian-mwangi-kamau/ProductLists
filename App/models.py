from django.db import models
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class AdminUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=True)


# Models for products and listing
class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='products/')
    description = models.TextField()
    brand = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    specs = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} - Product'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    
# product_description_template = """
# Description:
#  - Brand: {brand}
#  - Year: {year}
#  - Graphics" {graphics}
#  - Operating System: {OS}
#  - Display: {display}
#  - RAM: {ram}
#  - Storage: {storage}
#  - Color: {color}
 
#  Price: {price}
#  """

# product = Product.objects.create(
#     name="Dell laptop",
#     photo="", # the url to the photo should be here
#     description=product_description_template.format(
#         brand="Dell",
#         year=2019,
#         graphics="NVIDIA GeForce RTX 3060",
#         OS="Windows 10 Pro",
#         display="15.6\" FULL HD IPS",
#         ram="16GB DDR4",
#         storage="512GB NVMe SSD",
#         color="Black",
#         price="Ksh.94,600"
#     ),
#     brand="Dell",
#     year=2019,
#     specs="Intel Core i7, 16GB RAM, 512GB SSD, NVIDIA RTX 3060",
#     price=94600,
#     color="Black"
# )


# # Retrieve products by ID
# product = Product.objects.get(pk=46) # Retrieve a product by the primary ID
# product_id = product.id # Access the product's ID
