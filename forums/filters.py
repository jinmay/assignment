from django.db.models import Count, Window
from django.db.models.functions import TruncMonth

from rest_framework.filters import BaseFilterBackend


class MonthlyMostLikedFilter(BaseFilterBackend):
    pass
    # queryset.annotate(
    #     month=TruncMonth('created_at'),
    #     likes_count=Count('likes')
    # )
