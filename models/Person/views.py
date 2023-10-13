from django.shortcuts import render
from .models import Student, Teacher
from django.views.generic import ListView
from .models import Product, DiscountedProduct

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class DiscountedProductListView(ListView):
    model = DiscountedProduct
    template_name = 'discounted_product_list.html'
    context_object_name = 'discounted_products'
