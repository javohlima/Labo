from django.contrib import admin
from django.urls import path, include
from labs import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('labs.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
