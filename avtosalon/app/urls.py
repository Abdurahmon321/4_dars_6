from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.bosh_sahifa, name="bosh_sahifa"),
    path('avtomobillar/', views.avtomobillar, name="avtomobillar"),
    path('kontaktlar/', views.kontaktlar, name="kontaktlar"),
    path('add/', views.add_car, name="add_car"),
    path("car_d/<int:pk>", views.car_detail, name="car_detail"),
    path("car_update/", views.car_update_page, name="car_update_page"),
    path("car_delete/", views.car_delete_page, name="car_delete_page"),
    path("car_update/<int:pk>", views.car_update, name="car_update"),
    path("car_delete/<int:pk>", views.car_delete, name="car_delete"),
    path("category_add/", views.category_create, name="category_add"),
    path("category_detail/", views.category_d, name="category_d"),
    path("category_update/", views.category_d, name="category_d"),
    path("category_update/<int:pk>/", views.category_update, name="category_update"),
    path("category_delete/", views.category_delete_page, name="category_delete_page"),
    path("category_delete/<int:pk>/", views.category_delete, name="category_delete"),
    path("color_detail/", views.color_d, name="category_d"),
    path("color_update/", views.color_d, name="category_d"),
    path("color_update/<int:pk>/", views.color_update, name="category_update"),
    path("color_delete/", views.color_delete_page, name="category_delete_page"),
    path("color_delete/<int:pk>/", views.color_delete, name="category_delete"),
    path("color_add/", views.color_create, name="color_add"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
