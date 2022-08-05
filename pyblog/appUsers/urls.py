from django.urls import path
from appUsers.views import *

from appUsers import views

urlpatterns = [

    path('profile/', list_posts, name="list_posts"),
    path('new_post/', new_post, name="new_post"),
    path('all_users/', list_users, name="list_users"),
    path('register/', register, name="register"),


    path('reviews/', reviews, name="reviews"),
    path('new_review/', new_review, name="new_review"),
    # Path clase nueva 
    # Path form datos clase nueva

]