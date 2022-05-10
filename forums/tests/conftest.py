import pytest

from django.contrib.auth import get_user_model

from forums.models import Question


User = get_user_model()


@pytest.fixture
def user1():
    user = User.objects.create_user(**{
        'username': 'user1',
        'password': 'secret',
        'first_name': '길동',
        'last_name': '홍',
    })
    return user


@pytest.fixture
def user2():
    user = User.objects.create_user(**{
        'username': 'user2',
        'password': 'secret',
        'first_name': '나다',
        'last_name': '가',
    })
    return user


@pytest.fixture
def question1(user1):
    q = Question.objects.create(
        title='question #1',
        body='body #1',
        owner=user1
    )
    return q


@pytest.fixture
def question2(user1):
    q = Question.objects.create(
        title='question #2',
        body='body #2',
        owner=user1
    )
    return q
