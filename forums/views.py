from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework.generics import ListCreateAPIView

from .models import (
    Question,
)
from .serializers import (
    QuestionSerializer,
)


@method_decorator(login_required, name='post')
class QuestionListCreateView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
