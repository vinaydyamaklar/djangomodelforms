from django.conf.urls import url
from modelformapp import views

urlpatterns = [
    url(r'^$',views.users,name='users')
]