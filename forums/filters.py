from rest_framework.filters import BaseFilterBackend


class MonthlyMostLikedFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        pass