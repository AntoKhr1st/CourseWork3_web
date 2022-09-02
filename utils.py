import json

from flask import jsonify

path_posts = 'data/posts.json'
path_comments = './data/comments.json'
path_bookmarks = './data/bookmarks.json'  # не реализовано


# получает данные из файла
def load_data_all(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# нужно реализовать проверку отсутствия файла
def get_posts_all():
    posts = load_data_all(path_posts)
    return posts


def get_posts_by_user(user_name):
    # получаем список постов path_posts по имени пользователя
    posts = load_data_all(path_posts)
    posts_by_user = []
    user_name_list = []  # переменная нужна для вызова ошибки
    for post in posts:
        user_name_list.append(post['poster_name'])
    for post in posts:
        if post['poster_name'].lower() == user_name.lower():
            posts_by_user.append(post)
    if user_name not in user_name_list:  # проверяет корректность имени пользователя
        raise ValueError("пользователя или постов нет")
    else:
        return posts_by_user


def search_for_posts(query):
    posts = load_data_all(path_posts)
    posts_with_query = []
    # проверка на вхождение строки query в post["content"]
    for post in posts:
        if query.lower() in post["content"].lower():
            posts_with_query.append(post)
    return posts_with_query


def get_comments_by_post_id(post_id):
    # получаем список комментов из path_comments
    comments = load_data_all(path_comments)
    posts = posts = load_data_all(path_posts)
    comms_by_post_id = []
    post_id_list = []  # переменная нужна для вызова ошибки
    for post in posts:
        post_id_list.append(post['pk'])
    for com in comments:
        if com["post_id"] == post_id:
            comms_by_post_id.append(com)
    if post_id not in post_id_list:
        raise ValueError('некорректный post_id')
    else:
        return comms_by_post_id


def get_post_by_pk(pk):
    posts = load_data_all(path_posts)
    posts_pk_list = []  # переменная нужна для вызова ошибки
    for post in posts:
        posts_pk_list.append(post['pk'])
    for post in posts:
        if post['pk'] == pk:
            return post
        if pk not in posts_pk_list:
            raise ValueError('некорректный pk')  # возвращает ошибку если пост не найден
