from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name = "post_list"),
    path('author/<name>',views.get_author,name = "author"),
    path('post_details/<int:id>',views.post_details,name = "post_details"),
    path('post_category/<name>',views.post_category,name = "post_category"),
    path('login',views.user_login,name = "login"),
    path('logout',views.user_logout,name = "logout"),
    path('post_create',views.post_create,name = "post_create"),
    path('post_update/<int:id>',views.post_update,name = "post_update"),
    path('delete/<int:id>',views.post_delete,name = "post_delete"),
    path('profile',views.profile,name = "profile"),
    path('signup',views.signup,name = "signup"),
]
