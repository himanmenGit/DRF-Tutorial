from django.contrib.auth.models import User

from .permissions import IsOwnerOrReadOnly
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippet': reverse('snippet-list', request=request, format=format)
    })


class SnippetViewSet(viewsets.ModelViewSet):
    """
    이 뷰셋은 list와 create, retrieve, update, destory 기능을 자동으로 지원 합니다.
    여기에 highlight 기능의 코드만 추가로 작성 했습니다
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    이 뷰셋은 list와 detail 기능을 자동으로 지원합니다.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
