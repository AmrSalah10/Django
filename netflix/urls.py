from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index , name='index'),
    path('create', views.CreateMovie , name='create'),
    path('show/<str:name>', views.ShowMovie , name='show'),
    path('update/<int:id>', views.EditMovie , name='update'),
    path('delete/<int:id>', views.DeleteMovie , name='delete'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)