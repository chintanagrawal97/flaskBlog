from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(25), index=True)

    def to_json(self):
        tag = {
            'tag': self.tag,
            'posts': url_for('api.get_tag_posts', tag=self.tag, _external=True)
        }
        return tag

    def __repr__(self):
        return '<Tag %r>' % (self.tag)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    tags = db.Column(db.String(64))

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    @property
    def body_to_html(self):
        html = markdown_to_html(self.content)
        return html

    def tag_in_post(self, tag):
        if self.tags.find(',') > -1:
            tags = [i for i in self.tags.split(',')]
            if tag in tags:
                return True
            return False
        else:
            if tag == self.tags:
                return True
            return False


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(6), index=True)

    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def to_json(self):
        category = {
            'category': self.category,
            'post_count': self.posts.count(),
            'posts': url_for('api.get_category_posts', category=self.category, _external=True)
        }
        return category

    def __repr__(self):
        return '<Category %r>' % (self.category)

def init_db():
        db.create_all()

if __name__ == '__main__':
    init_db()