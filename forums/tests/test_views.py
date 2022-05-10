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
    assert content[0]['owner'] == question1.owner.username


@pytest.mark.django_db
def test_question_listcreateview_should_return_two_question(question1, question2, user1):
    client = APIClient()
    client.force_authenticate(user1)

    res = client.get('/questions/')
    assert res.status_code == 200

    content = get_json_response(res)
    assert len(content) == 2

    assert content[0]['title'] == question1.title
    assert content[0]['body'] == question1.body
    assert content[0]['owner'] == question1.owner.username

    assert content[1]['title'] == question2.title
    assert content[1]['body'] == question2.body
    assert content[1]['owner'] == question2.owner.username


@pytest.mark.django_db
def test_question_listcreateview_should_return_question_by_title_search(question1, question2, user1):
    client = APIClient()
    client.force_authenticate(user1)

    data = {
        'search': '#2'
    }
    res = client.get('/questions/', data=data)
    assert res.status_code == 200

    content = get_json_response(res)
    assert len(content) == 1

    assert content[0]['title'] == question2.title
    assert content[0]['body'] == question2.body
    assert content[0]['owner'] == question2.owner.username


@pytest.mark.django_db
def test_question_listcreateview_should_return_question_by_body_search(question1, question2, user1):
    client = APIClient()
    client.force_authenticate(user1)

    data = {
        'search': '#2'
    }
    res = client.get('/questions/', data=data)
    assert res.status_code == 200

    content = get_json_response(res)
    assert len(content) == 1

    assert content[0]['title'] == question2.title
    assert content[0]['body'] == question2.body
    assert content[0]['owner'] == question2.owner.username


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

    content = get_json_response(res)
    assert content['title'] == 'new question #1'
    assert content['body'] == 'new body #1'
    assert content['owner'] == user1.username


# @pytest.mark.django_db
# def test_quest_listcreateview_should_redirect_for_login():
#     client = APIClient()
#
#     data = {
#         'title': 'new question #1',
#         'body': 'new body #1',
#     }
#     res = client.post('/questions/', data=data)
#     assert res.status_code == 302


@pytest.mark.django_db
def test_question_retrieveview_should_return_one_question(user1, question1):
    client = APIClient()
    client.force_authenticate(user1)

    res = client.get(f'/questions/{question1.id}')
    assert res.status_code == 200

    content = get_json_response(res)
    assert content['title'] == question1.title
    assert content['body'] == question1.body
    assert content['owner'] == question1.owner.username


@pytest.mark.django_db
def test_question_updateview_should_update_title(user1, question1):
    client = APIClient()
    client.force_authenticate(user1)

    data = {
        'title': 'updated title'
    }
    res = client.patch(f'/questions/{question1.id}', data=data)
    assert res.status_code == 200

    content = get_json_response(res)
    assert content['title'] == 'updated title'
    assert content['body'] == question1.body
    assert content['owner'] == question1.owner.username


@pytest.mark.django_db
def test_question_updateview_should_update_body(user1, question1):
    client = APIClient()
    client.force_authenticate(user1)

    data = {
        'body': 'updated body'
    }
    res = client.patch(f'/questions/{question1.id}', data=data)
    assert res.status_code == 200

    content = get_json_response(res)
    assert content['title'] == question1.title
    assert content['body'] == 'updated body'
    assert content['owner'] == question1.owner.username


@pytest.mark.django_db
def test_question_updateview_should_delete_question(user1, question1):
    client = APIClient()
    client.force_authenticate(user1)

    res = client.delete(f'/questions/{question1.id}')
    assert res.status_code == 204


@pytest.mark.django_db
def test_question_updateview_should_prevent_update_from_different_user(user2, question1):
    client = APIClient()
    client.force_authenticate(user2)

    data = {
        'title': 'updated title'
    }
    res = client.patch(f'/questions/{question1.id}', data=data)
    assert res.status_code == 403


@pytest.mark.django_db
def test_question_updateview_should_prevent_delete_from_different_user(user2, question1):
    client = APIClient()
    client.force_authenticate(user2)

    res = client.delete(f'/questions/{question1.id}')
    assert res.status_code == 403


@pytest.mark.django_db
def test_comment_listcreate_view_should_return_zero_comment_list(user2, question1):
    client = APIClient()
    client.force_authenticate(user2)

    res = client.get(f'/questions/{question1.id}/comments')
    assert res.status_code == 200

    content = get_json_response(res)
    assert len(content) == 0


@pytest.mark.django_db
def test_comment_listcreate_view_should_return_comment_list(user2, question1, comment1):
    client = APIClient()
    client.force_authenticate(user2)

    res = client.get(f'/questions/{question1.id}/comments')
    assert res.status_code == 200

    content = get_json_response(res)
    assert len(content) == 1
    assert content[0]['body'] == comment1.body
    assert content[0]['owner'] == comment1.owner.username


@pytest.mark.django_db
def test_comment_listcreate_view_should_create_comment(user2, question1):
    client = APIClient()
    client.force_authenticate(user2)

    data = {
        'body': 'new comment body',
    }
    res = client.post(f'/questions/{question1.id}/comments', data=data)
    assert res.status_code == 201

    content = get_json_response(res)
    assert content['body'] == 'new comment body'
    assert content['owner'] == user2.username
