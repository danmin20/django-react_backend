from django.urls import path, include
from .views import PostVeiwSet, PostVeiwSet, RegistrationAPI, LoginAPI, UserAPI

post_list = PostVeiwSet.as_view({"get": "list", "post": "create"})

post_detail = PostVeiwSet.as_view(
    {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
)

urlpatterns = [
    path("posts/", post_list, name="post-list"),
    path("posts/<int:pk>/", post_detail, name="post-detail"),
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/users/", UserAPI.as_view()),
]
