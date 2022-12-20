
from .import views
from django.urls import path



#app_name='home'
urlpatterns = [
    path('newsletter', views.newsletter, name="newsletter"),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('contact/', views.contact_form, name='contact'),
    path('policy/', views.policy, name='policy'),
    path('site.html',views.site, name='site'),
    path('aboutme.html',views.aboutme,name='aboutme'),
    path('subscribe/', views.subscribe, name='subscribe'),
   
]