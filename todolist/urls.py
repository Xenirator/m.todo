from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, add_todo, delete_todo




urlpatterns = [
    path('', index, name='home'),
    path('add_todo/', add_todo),
    path('delete_todo/<int:todo_id>/', delete_todo)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)