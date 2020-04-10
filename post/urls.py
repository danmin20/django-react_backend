from django.urls import path
from .views import PostVeiwSet

post_list = PostVeiwSet.as_view({"get": "list", "post": "create"})

post_detail = PostVeiwSet.as_view(
    {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
)

urlpatterns = [
    path("posts/", post_list, name="post-list"),
    path("posts/<int:pk>/", post_detail, name="post-detail"),
]
