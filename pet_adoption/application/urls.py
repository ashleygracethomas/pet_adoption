from django.urls import path
from . import views



from django.conf.urls.static import static
from django.conf import settings
from application import views

urlpatterns= [
    path("",views.home,name="Home"),
    path("about/",views.about,name="About"),
    path("contactus/",views.contactus,name="Contactus"),
    path('signup/',views.signupPage,name='signup'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),


    
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# catalog/urls.py


