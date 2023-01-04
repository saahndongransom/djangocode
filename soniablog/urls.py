
from .import views
from django.urls import path , include




#app_name = 'home'

urlpatterns = [

    path("habiba",views.habiba,name="habiba"),
    path('footer.html',views.footer,name='footer'),
    path("newsletter", views.newsletter, name="newsletter"),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('contact/', views.contact_form, name='contact'),
    path('policy/', views.policy, name='policy'),
    path('newhatchtech.html',views.site, name='newhatchtech'),
    path('aboutme.html',views.aboutme,name='aboutme'),
    path('subscribe', views.subscribe, name='subscribe_newsletter'),
    path('comments/', include('django_comments_xtd.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('home1/', views.home1, name="home1"),
    path('feli.html',views.feli,name='feli'),
    path('paypal_return/', views.paypal_return,name='paypal-return'),
    path('paypal-cancel/', views.paypal_cancel,name='paypal-cancel'),
    #path('users/', include('users.urls')),
    #path('',views.home1, name='home1'),
    

 
    #path('process-payment/', views.process_payment, name='process_payment'),
    
   
]