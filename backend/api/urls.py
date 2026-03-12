from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.city_list),
    path('cities/<str:pk>/', views.city_detail),
    path('cities/<str:pk>/places/', views.city_places),
    path('cities/<str:pk>/foods/', views.city_foods),
    path('generate-ai-itinerary/', views.generate_itinerary_view),
    path('download-itinerary-pdf/', views.download_pdf_view),
    path('weather/', views.weather_view),
    path('chat/', views.chat_view),
    path('generate-image/', views.generate_image_view),
]
