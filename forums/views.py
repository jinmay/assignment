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
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def perform_destroy(self, instance):
        instance.check_permission(self.request.user)
        super().perform_destroy(instance)
