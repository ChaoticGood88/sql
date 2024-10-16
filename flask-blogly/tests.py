import unittest
from app import app, db
from models import User

class BloglyTestCase(unittest.TestCase):
    """Tests for Blogly routes."""

    @classmethod
    def setUpClass(cls):
        """Run once before any tests."""
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

    def tearDown(self):
        """Run after every individual test."""
        with app.app_context():
            db.session.rollback()
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

if __name__ == "__main__":
    unittest.main()
