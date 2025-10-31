from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class ProductFeature(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام ویژگی ')
    value = models.CharField(max_length=255, verbose_name='مقدار ویژگی ')

    def __str__(self):
        return f"{self.name}: {self.value}"


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE , verbose_name='دسته بندی')
    name = models.CharField(max_length=255, verbose_name='نام ')
    slug = models.SlugField(max_length=255, verbose_name='اسلاگ ')
    description = models.TextField(max_length=3500, blank=True, verbose_name='توضیحات ')
    price = models.PositiveIntegerField( default =0, verbose_name='قیمت ')
    adventory = models.PositiveIntegerField(verbose_name='موجودی ', default =0)
    off = models.PositiveIntegerField(verbose_name='تخفیف ', default =0)
    new_price = models.PositiveIntegerField(verbose_name='قیمت جدید ', default =0)
    productfeature = models.ManyToManyField(ProductFeature, blank=True, related_name='f_products', verbose_name='ویژگی های محصول ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد ')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی ')
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def __str__(self):
        return self.name



class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="محصول")
    file = models.ImageField(upload_to="product_images/%Y/%m/%d/")
    title = models.CharField(max_length=250, verbose_name="عنوان", null=True, blank=True)
    description = models.TextField(verbose_name="توضیحات", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
        verbose_name = "تصویر"
        verbose_name_plural = "تصویر ها"

