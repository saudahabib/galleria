from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('^sports/$',views.sports_category,name = 'sports'),
    url('^search$',views.search_results,name = 'search_results'),
    url(r'^article/(\d+)', views.single_photo, name='article')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
