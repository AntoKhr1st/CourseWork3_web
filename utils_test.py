import pytest

from utils import get_posts_all, get_posts_by_user, search_for_posts, get_comments_by_post_id, \
    get_post_by_pk


def test_get_posts_all():
    assert type(get_posts_all()) == list


##########

def test_get_posts_by_user1():
    assert len(get_posts_by_user('leo')) == 2


def test_get_posts_by_user2():
    assert len(get_posts_by_user('hank')) == 2


def test_get_posts_by_user3():
    assert type(get_posts_by_user('leo')) == list


def test_get_posts_by_user4():
    with pytest.raises(ValueError):
        get_posts_by_user('petya')


##########

def test_search_for_posts1():
    assert type(search_for_posts('кот')) == list


def test_search_for_posts2():
    assert search_for_posts('приветики') == []


###########
def test_get_comments_by_post_id1():
    assert type(get_comments_by_post_id(1)) == list


def test_get_comments_by_post_id_ValueError():
    with pytest.raises(ValueError):
        get_comments_by_post_id(111)


#######

def test_get_post_by_pk1():
    assert type(get_post_by_pk(1)) == dict


def test_get_post_by_pk_error():
    with pytest.raises(ValueError):
        get_post_by_pk(222)
