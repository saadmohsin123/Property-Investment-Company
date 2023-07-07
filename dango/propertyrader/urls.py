
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import index
from . import views

urlpatterns = [
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('blogs/', views.blogs, name="blogs"),
    path('investment/plan/', views.investment_plan, name="investment_plan"),
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('accounts/', include('accounts.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

