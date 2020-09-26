from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogapp/', include('blogapp.urls')),
    path('accountapp/', include('accountapp.urls')),
    path('mountainapp/', include('mountainapp.urls')),
    path('', blogapp.views.index, name='index'), #메인화면
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)