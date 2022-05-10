from rest_framework.generics import ListCreateAPIView

from .models import (
    Question,
)
from .serializers import (
    QuestionSerializer,
)


class QuestionListCreateView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
