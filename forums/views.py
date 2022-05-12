from rest_framework.response import Response
from rest_framework import (
    filters,
    status,
)
from rest_framework.generics import (
    CreateAPIView,
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
from .filters import MonthlyMostLikedFilter


class QuestionListCreateView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filter_backends = [filters.SearchFilter, MonthlyMostLikedFilter]
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


class QuestionLikeToggleView(CreateAPIView):
    queryset = Question.objects.all()

    def post(self, request, *args, **kwargs):
        user = request.user
        question = self.get_object()
        if question.likes.filter(id=user.id).exists():
            question.likes.remove(user)
            data = {
                'msg': 'like'
            }
            status_code = status.HTTP_204_NO_CONTENT
        else:
            question.likes.add(user)
            data = {
                'msg': 'unlike'
            }
            status_code = status.HTTP_201_CREATED

        return Response(data=data, status=status_code)
