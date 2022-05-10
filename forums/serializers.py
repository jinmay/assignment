from rest_framework import serializers as s

from .models import (
    Question,
    Comment,
)


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

    def update(self, instance, validated_data):
        request = self.context['request']
        instance.check_permission(request.user)
        return super().update(instance, validated_data)


class CommentSerializer(s.ModelSerializer):
    owner = s.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'body',
            'owner',
        )
