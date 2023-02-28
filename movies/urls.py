from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_id>', views.movie_detail, name='detail'),
    path('review/<int:movie_id>/create', views.create_review, name='create_review'),
    path('review/<int:review_id>/update', views.update_review, name='update_review'),
    path('review/<int:review_id>/delete', views.delete_review, name='delete_review'),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)