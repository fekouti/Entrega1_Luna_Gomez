from django.urls import path
from appUsers.views import *

from appUsers import views

urlpatterns = [
    # path('profile/', profile, name="profile"),
    path('profile/', list_posts, name="list_posts"),

]