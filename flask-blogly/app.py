from flask import Flask, redirect, render_template, request, flash, url_for
from models import db, connect_db, User, Post  # Ensure Post model is imported
from flask_debugtoolbar import DebugToolbarExtension

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False  # Log SQL queries for debugging
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['DEBUG_TB_ENABLED'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Connect the app with the database
connect_db(app)
toolbar = DebugToolbarExtension(app)

# Ensure tables are created when the app starts
with app.app_context():
    db.create_all()

@app.route('/')
def home_page():
    """Redirect to the user listing."""
    return redirect(url_for('list_users'))

@app.route('/users')
def list_users():
    """Show the list of users."""
    users = User.query.all()
    return render_template('user_list.html', users=users)

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    """Show user details along with their posts."""
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(user_id=user_id).all()
    print(f"Posts for user {user_id}: {posts}")  # Debugging print
    return render_template('user_detail.html', user=user, posts=posts)

@app.route('/users/new', methods=["GET", "POST"])
def new_user():
    """Show form to create a new user or handle form submission."""
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        image_url = request.form.get('image_url') or None

        user = User(first_name=first_name, last_name=last_name, image_url=image_url)
        db.session.add(user)
        db.session.commit()
        flash(f"User {first_name} {last_name} added!")

        return redirect(url_for('list_users'))

    return render_template('new_user.html')

@app.route('/users/<int:user_id>/edit', methods=["GET", "POST"])
def edit_user(user_id):
    """Show form to edit a user and handle form submission."""
    user = User.query.get_or_404(user_id)

    if request.method == "POST":
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.image_url = request.form['image_url']

        db.session.commit()
        flash(f"User {user.first_name} {user.last_name} updated!")
        return redirect(url_for('user_detail', user_id=user.id))

    return render_template('edit_user.html', user=user)

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Delete a user."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f"User {user.first_name} {user.last_name} deleted!")
    return redirect(url_for('list_users'))

@app.route('/users/<int:user_id>/posts/new', methods=["GET", "POST"])
def new_post(user_id):
    """Show form to add a new post and handle submission."""
    user = User.query.get_or_404(user_id)

    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']

        new_post = Post(title=title, content=content, user_id=user.id)
        db.session.add(new_post)
        db.session.commit()
        flash(f"Post '{title}' added!")

        return redirect(url_for('user_detail', user_id=user.id))

    return render_template('new_post.html', user=user)

@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    """Show details of a single post."""
    post = Post.query.get_or_404(post_id)

    # Debug: Print the post to confirm it's fetched correctly
    print(f"Viewing post: {post}")

    return render_template('post_detail.html', post=post)


@app.route('/posts/<int:post_id>/edit', methods=["GET", "POST"])
def edit_post(post_id):
    """Show form to edit a post and handle form submission."""
    post = Post.query.get_or_404(post_id)

    if request.method == "POST":
        post.title = request.form['title']
        post.content = request.form['content']

        db.session.commit()
        flash(f"Post '{post.title}' updated!")
        return redirect(url_for('post_detail', post_id=post.id))

    return render_template('edit_post.html', post=post)

@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """Delete a post and redirect to the user detail page."""
    post = Post.query.get_or_404(post_id)
    user_id = post.user_id  # Save user_id before deletion
    db.session.delete(post)
    db.session.commit()
    flash(f"Post '{post.title}' deleted successfully!")
    return redirect(url_for('user_detail', user_id=user_id))


