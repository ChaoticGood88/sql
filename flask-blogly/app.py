from flask import Flask, redirect, render_template, request, flash, url_for
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['DEBUG_TB_ENABLED'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
toolbar = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Redirect to user listing."""
    return redirect('/users')

@app.route('/users')
def list_users():
    """Show list of users."""
    users = User.query.all()
    return render_template('user_list.html', users=users)

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    """Show details of a specific user."""
    user = User.query.get_or_404(user_id)
    return render_template('user_detail.html', user=user)

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

@app.route('/users/new', methods=["GET", "POST"])
def new_user():
    """Show form to create a new user or handle form submission."""
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        image_url = request.form['image_url'] or None

        # Create and add the new user
        user = User(first_name=first_name, last_name=last_name, image_url=image_url)
        db.session.add(user)
        db.session.commit()
        flash(f"User {first_name} {last_name} added!")

        return redirect(url_for('list_users'))

    return render_template('new_user.html')

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Delete a user."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f"User {user.first_name} {user.last_name} deleted!")
    return redirect(url_for('list_users'))


    if request.method == "POST":
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.image_url = request.form['image_url']

        db.session.commit()
        flash(f"User {user.first_name} {user.last_name} updated!")
        return redirect(url_for('user_detail', user_id=user.id))

    return render_template('edit_user.html', user=user)





