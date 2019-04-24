from flask import Flask
app = Flask(__name__)

# 一个简单的例子
@app.route('/')
def hello_world():
    return 'Hello, World!'

# 几种不同的类型
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

# 对比有无“/”的区别，projects如果没有加斜杠，Flask会重定向，而
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'