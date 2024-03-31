from django.urls import path
from .views import (all_posts, posts_by_category, post_detail, post_create, post_update, post_delete, category_detail,
                    category_create, category_update, category_delete)


urlpatterns = [
    path('', all_posts, name='index'),
    path('category/<int:category_id>/', posts_by_category, name='bolim'),
    path('detail/<int:pk>/', post_detail, name='post_detail'),
    path('add/', post_create, name='post_create'),
    path('update/<int:pk>/', post_update, name='post_update'),
    path('delete/<int:pk>/', post_delete, name='post_delete'),
    path('category_add/', category_create, name="category_create"),
    path('category_detail/<int:pk>/', category_detail, name="category_detail"),
    path('category_update/<int:pk>/', category_update, name="category_update"),
    path('category_delete/<int:pk>/', category_delete, name="category_delete"),
]

