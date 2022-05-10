import json
import pytest

from rest_framework.test import APIClient


def get_json_response(res):
    return json.loads(res.content)


@pytest.mark.django_db
def test_question_listcreateview_should_return_question_list(question1, user1):
    client = APIClient()
    client.force_authenticate(user1)

    res = client.get('/questions/')
    assert res.status_code == 200

    content = get_json_response(res)
    assert len(content) == 1

    assert content[0]['title'] == question1.title
    assert content[0]['body'] == question1.body


@pytest.mark.django_db
def test_question_listcreateview_should_return_empty(user1):
    client = APIClient()
    client.force_authenticate(user1)

    res = client.get('/questions/')
    assert res.status_code == 200

    content = get_json_response(res)
    assert len(content) == 0


@pytest.mark.django_db
def test_quest_listcreateview_create_new_question(user1):
    client = APIClient()
    client.force_authenticate(user1)

    data = {
        'title': 'new question #1',
        'body': 'new body #1',
    }
    res = client.post('/questions/', data=data)
    assert res.status_code == 201


@pytest.mark.django_db
def test_quest_listcreateview_should_redirect_for_login():
    client = APIClient()

    data = {
        'title': 'new question #1',
        'body': 'new body #1',
    }
    res = client.post('/questions/', data=data)
    assert res.status_code == 302
