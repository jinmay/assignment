from rest_framework import filters
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import (
    Question,
    Comment,
)
from .serializers import (
    QuestionSerializer,
    CommentSerializer,
)


class QuestionListCreateView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']


class QuestionView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def perform_destroy(self, instance):
        instance.check_permission(self.request.user)
        super().perform_destroy(instance)


class CommentListCreateView(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        question_id = self.kwargs.get('pk')
        qs = Comment.objects.filter(question_id=question_id)
        return qs

    def perform_create(self, serializer):
        owner = self.request.user
        question_id = self.kwargs.get('pk')
        data = {
            'owner': owner,
            'question_id': question_id,
        }
        serializer.save(**data)
