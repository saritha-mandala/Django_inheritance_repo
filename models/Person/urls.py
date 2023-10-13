from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('discounted-products/', views.DiscountedProductListView.as_view(), name='discounted-product-list'),
]

