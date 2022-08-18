from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('api', views.BookList.as_view())
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns = format_suffix_patterns(urlpatterns)
