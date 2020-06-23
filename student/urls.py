from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from products import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view() ,name='home'),
    path('products/', include('products.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
