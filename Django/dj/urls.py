from django.urls import path,include
from . import views

#localhost:8000/dj
urlpatterns = [
    path('', views.all_dj,name='all_dj'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_stores/',views.chai_store_view, name='chai_store_view'),
]
