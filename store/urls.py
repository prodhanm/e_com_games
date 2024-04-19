from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('cart/add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/remove/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('cart/delete/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('thanks_page/', views.thanks_page, name='thanks_page'),
    path('account/created/', views.signupView, name='signup'),
    path('account/signin/', views.signinView, name='signin'),
    path('account/signout/', views.signoutView, name='signout'),
]