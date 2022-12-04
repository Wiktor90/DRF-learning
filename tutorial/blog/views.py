from rest_framework import viewsets
from rest_framework import generics

from blog.models import Author
from blog.serializers import AuthorSerializer


class AuthorViewSet(
    generics.ListCreateAPIView,
    generics.RetrieveUpdateAPIView,
    viewsets.GenericViewSet,
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Widok:

# AUTHOR
# GET /author - autor list + coment_count / post_count - ile czego pisal
# albo serwis w widoku albo method field w serializerze ?
# GET /author/<int:pk> - to samo tylko details view
# POST /author/<int:pk> - required tylko email

# POST
# /author/<int:pk>/post - wszystkie posty per autor. Dodac licznik komentarzy "comments"
# /author/<int:pk>/post/<post_pk> - konkretny post danego autora. Dodac licznik komentarzy "comments"
# *zcustomizowac get_object() w widoku
# /recent/post - wyswietla 5 ostatnich postow. Dodac tu "recent_comments" - 2 najnowsze komentarze posta

# COMMENTS
# /comment - wszystkie komentarz - post wyswietlac po tytule i autora po name.
# /author/<int:pk>/comment - wszystkie komenty per autor. wyswietlanie jak wyzej



# wszyscy autorzy CRUD / lookup - PK / + ile kazdy autor napisal postow i ile komentarzy
# Wszystkie Posty  - w liscie widok info z posta plus 2 ostatnie komenty
# widok indiwidualnego posta - z wszystkimi komentarzami.