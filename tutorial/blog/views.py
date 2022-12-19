from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response

from blog.models import Author, Post
from blog.serializers import AuthorSerializer, PostDetailsSerializer
from blog.serializers import PostSerializer


class AuthorViewSet(
    generics.ListCreateAPIView,
    generics.RetrieveUpdateAPIView,
    viewsets.GenericViewSet,
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PostView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = PostSerializer

    def get_queryset(self):
        author_pk = self.kwargs["author_pk"]
        return Post.objects.filter(
            author=author_pk
        ).order_by("-created_at").select_related("author").prefetch_related("comments")

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": "author not found"}
            )
        return super(PostView, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PostDetailsSerializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        author_pk = self.kwargs["author_pk"]
        author = Author.objects.get(pk=author_pk)
        serializer.save(author=author)

class RecentPostView(generics.ListAPIView, viewsets.GenericViewSet):
    # Display 5 last Post with recent 2 comments
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all().order_by("-created_at").select_related("author").prefetch_related("comments")[:5]
        return queryset

# Widok:

# AUTHOR
# [+] GET /author - autor list + coment_count / post_count - ile czego pisal
# [+] method field lub property na modelu
# [+] GET /author/<int:pk> - to samo tylko details view
# [+] POST /author/<int:pk> - required tylko email

# POST
# [+] GET /author/<int:pk>/post - wszystkie posty per autor. Dodac licznik komentarzy "comments"
# [+] GET /author/<int:pk>/post/<post_pk> - konkretny post danego autora. Dodac licznik komentarzy "comments"
# [+] przey GET datal:
# zcustomizowac retreive() w widoku. Inny serializer do widoku postu bo ma wyswietlac komenty.

# [+] /recent/post - wyswietla 5 ostatnich postow. Dodac tu "recent_comments" - 2 najnowsze komentarze posta

# COMMENTS
# /comment - wszystkie komentarz - post wyswietlac po tytule i autora po name.
# /author/<int:pk>/comment - wszystkie komenty per autor. wyswietlanie jak wyzej



# wszyscy autorzy CRUD / lookup - PK / + ile kazdy autor napisal postow i ile komentarzy
# Wszystkie Posty  - w liscie widok info z posta plus 2 ostatnie komenty
# widok indiwidualnego posta - z wszystkimi komentarzami.