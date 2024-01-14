from django.urls import path
from . import views

urlpatterns = [
    # Posts_URLs
    path("", views.accueil, name="accueil"),
    path("newpost/", views.savePost, name="newPost"),
    path("showpost/<int:id>", views.showPost, name="showPost"),
    path("updatepost/<int:id>", views.updatePost, name="updatePost"),
    path("deletepost/<int:id>", views.deletePost, name="deletePost"),
    # ==================================================================
    # comments_URLs
    path("createcom/<int:id>", views.createComment, name="newComment"),
    path("updatecomment/<int:id>", views.updateComment, name="updateComment"),
    path("deletecomment/<int:id>", views.deleteComment, name="deleteComment"),
]
