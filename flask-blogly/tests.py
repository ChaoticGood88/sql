import unittest
from app import app, db
from models import User, Post

class BloglyTestCase(unittest.TestCase):
    """Tests for Blogly routes."""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests."""
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_blogly'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for easier testing
        cls.client = app.test_client()

        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests."""
        with app.app_context():
            db.drop_all()

    def setUp(self):
        """Run before every individual test."""
        with app.app_context():
            user = User(first_name="Test", last_name="User", image_url=None)
            db.session.add(user)
            db.session.commit()
            self.user_id = user.id

            # Create a sample post for testing
            post = Post(title="Test Post", content="Test content", user_id=self.user_id)
            db.session.add(post)
            db.session.commit()
            self.post_id = post.id

    def tearDown(self):
        """Run after every individual test."""
        with app.app_context():
            db.session.rollback()
            Post.query.delete()
            User.query.delete()
            db.session.commit()

    def test_list_users(self):
        """Test GET /users route."""
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test User", response.data)

    def test_add_user(self):
        """Test POST /users/new route."""
        response = self.client.post("/users/new", data={
            "first_name": "New",
            "last_name": "User",
            "image_url": ""
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"New User", response.data)

    def test_user_detail(self):
        """Test GET /users/<user_id> route."""
        response = self.client.get(f"/users/{self.user_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test User", response.data)

    def test_edit_user(self):
        """Test POST /users/<user_id>/edit route."""
        response = self.client.post(f"/users/{self.user_id}/edit", data={
            "first_name": "Updated",
            "last_name": "User",
            "image_url": ""
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Updated User", response.data)

    def test_add_post(self):
        """Test POST /users/<user_id>/posts/new route."""
        response = self.client.post(f"/users/{self.user_id}/posts/new", data={
            "title": "New Post",
            "content": "This is a new post."
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"New Post", response.data)

    def test_post_detail(self):
        """Test GET /posts/<post_id> route."""
        response = self.client.get(f"/posts/{self.post_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Post", response.data)

    def test_edit_post(self):
        """Test POST /posts/<post_id>/edit route."""
        response = self.client.post(f"/posts/{self.post_id}/edit", data={
            "title": "Updated Post",
            "content": "Updated content."
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Updated Post", response.data)

    def test_delete_post(self):
        """Test POST /posts/<post_id>/delete route."""
        # Make POST request to delete the post
        response = self.client.post(f"/posts/{self.post_id}/delete", follow_redirects=True)
    
        # Ensure the status code is 200
        self.assertEqual(response.status_code, 200)
    
        # Check that the post title is not in the list of posts (after deletion)
        self.assertNotIn(b'<a href="/posts/', response.data)  # Post links should no longer be present
    
        # Confirm the flash message appears correctly
        self.assertIn(b"deleted successfully", response.data)

if __name__ == "__main__":
    unittest.main()