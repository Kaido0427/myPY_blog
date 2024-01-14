from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Reaction
from .form import postForm, commentForm, reactForm


# Pour acceder a l'accueil et a toutes les publications.
@login_required
def accueil(request):
    post = Post.objects.all()
    data = {"post": post}
    return render(request, "Posts/index.html", data)


# Enregistrer une nouvelle publication dans la base de données
@login_required
def savePost(request):
    form = postForm()
    if request.method == "POST":
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("/")
    return render(request, "Posts/new_post.html", {"form": form})

 
# views pour acceder a une publication ciblée
@login_required
def showPost(
    request,
    id,
):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    form = commentForm()
    data = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "Posts/onePost.html", data)


# Modifier une publication
@login_required
def updatePost(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = postForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("accueil")
    else:
        form = postForm(instance=post)
        return render(request, "Posts/update_post.html", {"form": form})


# Pour supprimer une publication
@login_required
def deletePost(request, id):
    post = get_object_or_404(Post, id=id)
    comment = Comment.objects.filter(post=post)
    comment.delete()
    post.delete()
    return render(request, "Posts/delete_Post.html")


# ==========================================
# Section des commentaires
# =========================================


@login_required
def createComment(request, id):
    form = commentForm()
    pub = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = commentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = pub
            form.save()
            return redirect("accueil")
        else:
            form = commentForm()
            data = {"form": form}
    return render(request, "Posts/onePost.html", data)


# Pour modifier un commentaire
@login_required
def updateComment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == "POST":
        form = commentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("accueil")
    else:
        form = commentForm(instance=comment)
        return render(request, "comments/update_comment.html", {"form": form})


@login_required
def deleteComment(id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect("accueil")


# ==========================================
# Section des réactions (like|unlike)
# =========================================


@login_required
def reactPost(request, id):
    pub = Post.objects.get(id=id)
    if request.method == "POST":
        form = reactForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = pub
            form.save()
            return redirect("accueil")
    else:
        form = reactForm()
        return render(request, "Posts/index.html", {"form": form})


# definir une fonction pour afficher le nombre total de reaction
