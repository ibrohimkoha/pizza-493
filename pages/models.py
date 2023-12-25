from django.db import models

# Create your models here.
class  ScrollModel(models.Model):
    image = models.ImageField(upload_to='scroll')
    discount = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=50)
    desctription = models.TextField(null=True)

    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'scroll'
        verbose_name_plural = 'scrolls'

class ImageModel(models.Model):
    image = models.ImageField(upload_to='rasm')
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

class BurgerModel(models.Model):
    image = models.ImageField(upload_to='burger')
    title = models.CharField(max_length=50)
    desctription = models.TextField()
    price = models.FloatField()
    
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'burger'
        verbose_name_plural = 'burgers'

class PizzaModel(models.Model):
    image = models.ImageField(upload_to='pizza')
    title = models.CharField(max_length=50)
    desctription = models.TextField()
    price = models.FloatField()
    
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'pizza'
        verbose_name_plural = 'pizzas'

class SaladModel(models.Model):
    image = models.ImageField(upload_to='salad')
    title = models.CharField(max_length=50)
    desctription = models.TextField()
    price = models.FloatField()
    
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'salad'
        verbose_name_plural = 'salads'

class FricesModel(models.Model):
    image = models.ImageField(upload_to='frices')
    title = models.CharField(max_length=50)
    desctription = models.TextField()
    price = models.FloatField()
    
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'frices'
        verbose_name_plural = 'frices'

class DrinksModel(models.Model):
    image = models.ImageField(upload_to='drinks')
    title = models.CharField(max_length=50)
    desctription = models.TextField()
    price = models.FloatField()
    
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'drinks'
        verbose_name_plural = 'drinks'

class UserModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.CharField(max_length=15)
    time = models.CharField(max_length=10)
    message = models.TextField()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
        
        
        