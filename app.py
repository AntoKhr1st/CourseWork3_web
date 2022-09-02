import json
from json import JSONDecodeError

from flask import Flask, request, render_template, jsonify

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

import logging

app = Flask(__name__)
logging.basicConfig(filename='api.log', level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


@app.route('/')
def all_posts_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_id>')
def posts_by_post_id_page(post_id):
    try:
        post = get_post_by_pk(post_id)
        comments = get_comments_by_post_id(post_id)
        return render_template('post.html', post=post, comments=comments)
    except FileNotFoundError:
        return 'файл с постами не найден'
    except JSONDecodeError:
        return 'проблема с json файлом'


@app.route('/search/')
def search_post_page():
    # пришлось добавить name = 's' в html
    try:
        search_query = request.args.get('s')
        posts = search_for_posts(search_query)
        return render_template('search.html', posts=posts)
    except FileNotFoundError:
        return 'файл с постами не найден'
    except JSONDecodeError:
        return 'проблема с json файлом'


@app.route('/users/<username>')
def posts_by_user_name_page(username):
    try:
        posts = get_posts_by_user(username)
        return render_template('user-feed.html', posts=posts, username=username)
    except FileNotFoundError:
        return 'файл с постами не найден'
    except JSONDecodeError:
        return 'проблема с json файлом'


@app.route('/api/posts')
def api_posts_endpoint():
    logging.info('выполнен запрос всех постов')
    return jsonify(get_posts_all())


@app.route('/api/posts/<int:post_id>')
def api_posts_by_id_endpoint(post_id):
    post = get_post_by_pk(post_id)
    logging.info(f'выполнен запрос поста {post_id}', )
    return jsonify(post)


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.errorhandler(500)
def page_500_error(error):
    return 'Internal Server Error', 500


app.run(port=5001)
