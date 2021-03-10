from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    url(r'^api/monuments$', views.monuments_list),
    url(r'^api/monuments/(?P<pk>[0-9]+)$', views.monuments_detail),
    url(r'^api/localFood$', views.localFoodList),
    url(r'^api/localFood/(?P<pk>[0-9]+)$', views.localFoodDetail)
]