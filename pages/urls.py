from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('about-us/',views.about,name='about'),
	path('contact-us/',views.contact,name='contact'),
	path('content',views.content,name='content'), 
	path('wordofthanks',views.lastpage,name='lastpage')   
]
