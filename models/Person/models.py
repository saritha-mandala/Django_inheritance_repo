from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
class Student(Person):
    student_id = models.CharField(max_length=10)
    grade_level = models.PositiveIntegerField()

class Teacher(Person):
    employee_id = models.CharField(max_length=10)
    subject_taught = models.CharField(max_length=30)

class DiscountedProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(discounted=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class DiscountedProduct(Product):
    discounted = models.BooleanField(default=True)

    objects = DiscountedProductManager()

    class Meta:
        proxy = True

    def get_discounted_price(self):
        return self.price * 0.9  # Apply a 10% discount
