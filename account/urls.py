
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^search/',views.search_results,name='search'),
    url(r'^upload_image/',views.upload,name='upload'),
    url(r'^edit/',views.edit,name='edit'),
    url(r'^settings/',views.settings_func,name='settings'),
    url(r'^comment/',views.new_comment,name='comment'),
    url(r'^view_profile/',views.view_your_profile,name='yourprofile'),
    # url(r'^follow/',views.views.profile,name='profile'),
    url(r'^like/',views.like,name='like')
    ,]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
