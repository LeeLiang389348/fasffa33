from django.contrib import admin
from django.urls import path
from crime import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_crimes, name="home"),
    path('contact/', views.contact_view, name='contact')
]
