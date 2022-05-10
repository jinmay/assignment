from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import (
    Question,
)
from .serializers import (
    QuestionSerializer,
)


class QuestionListCreateView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionView(RetrieveUpdateDestroyAPIView):
    pass