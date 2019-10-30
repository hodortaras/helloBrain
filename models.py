from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name='Категория'
        ordering = ['name']


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Брэнд')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Бренды'
        verbose_name='Брэнд'
        ordering = ['name']


def image_name(instance, filename):
    filename = instance.slug + '.' +filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд')
    title = models.CharField(max_length=120, verbose_name='Товар')
    slug = models.SlugField()
    image = models.ImageField(upload_to=image_name)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits = 9, decimal_places = 2, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    avaliable = models.BooleanField(default = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name='Товар'
        ordering = ['-price']
