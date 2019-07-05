
from django.contrib import admin
from django.urls import path
from  .view import topic,customer,byCountry
from django.conf.urls import  url


urlpatterns = [
url(r'^topic', topic, name='topic'),
url(r'^ceramica', customer, name='ceramica'),
url(r'^bycountry', byCountry, name='byCountry'),
]
