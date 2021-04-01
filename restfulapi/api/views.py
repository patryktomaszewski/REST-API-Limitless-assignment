from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WordSerializer
from .models import Word


class WordListView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class WordRetrieveView(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class WordCountView(APIView):
    model = Word

    def get(self, *args, **kwargs):
        qs = self.get_queryset(*args, **kwargs)
        return Response({"count": qs.count()}, status.HTTP_200_OK)

    def get_queryset(self, *args, **kwargs):
        qs = self.model.objects.all()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name=name)
        return qs

class UniqueWordView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Word.objects.values('name').distinct()
    serializer_class = WordSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)