from .views import home,about, contact, test, newsletter, password_reset_request
from django.urls import path
app_name='myApp'
urlpatterns = [
    path('', home, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('test', test, name='test'),
    path('newsletter', newsletter, name='newsletter'),
    path("password_reset", password_reset_request, name="password_reset")
]
