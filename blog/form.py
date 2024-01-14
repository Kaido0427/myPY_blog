from django import forms
from .models import Post, Comment, Reaction


class postForm(forms.ModelForm):
    titre = forms.CharField(
        label="Titre de la publication",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    contenu = forms.CharField(
        label="Contenu de la publication",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
            }
        ),
    )

    image = forms.FileField(
        label="Choisir une image",
        widget=forms.FileInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Post
        fields = [
            "titre",
            "contenu",
            "image",
        ]


class commentForm(forms.ModelForm):
    contenu = forms.CharField(
        label="Commentaire",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = [
            "contenu",
        ]


class reactForm(forms.ModelForm):
    reaction_Type = forms.CharField(
        widget=forms.CharField(),
    )

    class Meta:
        model = Reaction
        fields = [
            "reaction_Type",
        ]
