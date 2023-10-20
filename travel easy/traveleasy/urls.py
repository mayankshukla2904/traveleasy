from django.conf.urls import url, include
from django.contrib import admin
import api.views as views
from traveleasy.settings import DEBUG

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if not DEBUG:
    urlpatterns.append(url(r'^$', views.view_home, name='redirectWebsite'))
    urlpatterns.append(url(r'^.*/$', views.view_404, name='redirect404'))
