from rest_framework import serializers as s

from .models import Question


class QuestionSerializer(s.ModelSerializer):
    owner = s.HiddenField(default=s.CurrentUserDefault())

    class Meta:
        model = Question
        fields = (
            'title',
            'body',
            'owner',
        )
