from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^sports/$',views.sports_category,name = 'sports'),

]
