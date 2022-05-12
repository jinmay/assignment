from django.urls import path

from . import views


urlpatterns = [
    path('', views.QuestionListCreateView.as_view()),
    path('<int:pk>', views.QuestionView.as_view()),
    path('<int:pk>/comments', views.CommentListCreateView.as_view()),
    path('<int:pk>/likes', views.QuestionLikeToggleView.as_view()),
]
