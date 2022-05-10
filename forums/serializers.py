from rest_framework import serializers as s

from .models import Question


class QuestionSerializer(s.ModelSerializer):
    owner = s.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Question
        fields = (
            'title',
            'body',
            'owner',
        )

    def create(self, validated_data):
        request = self.context['request']
        validated_data['owner'] = request.user
        return super().create(validated_data)
