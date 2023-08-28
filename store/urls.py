from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('main/', views.store, name="main"),
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
        
	#path('login_user', views.render, name="login_user"),
	# I can't tell of the significance of this

]