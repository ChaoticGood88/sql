from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """User model for Blogly."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.Text, nullable=False, default='https://via.placeholder.com/150')

    # One-to-many relationship: User -> Posts
    posts = db.relationship('Post', backref='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.id} {self.first_name} {self.last_name}>"

class Post(db.Model):
    """Post model for Blogly."""

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Foreign key to link the post to a user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"<Post {self.id} {self.title} {self.created_at}>"

def connect_db(app):
    """Connect this database to the provided Flask app."""
    db.app = app
    db.init_app(app)



