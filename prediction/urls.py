from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict,name='predictions.predict'),
    path('predict/',views.predict,name='predictions.predict'),
    path('predict/predicted_price/', views.predicted_price, name='predictions.predicted_price'),
]