from django.conf.urls import include, url
from django.contrib import admin
from .views import home

urlpatterns = [
    # Examples:
    # url(r'^$', 'taskbuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home, name='home')
    #url(r'^admin/', include(admin.site.urls)),
]
