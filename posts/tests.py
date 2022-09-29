from django.test import TestCase
from .models import Post

# Create your tests here.
# To run our test > python manage.py test
# Note only fxns beginning with test* will be run


class PostTests(TestCase):
    # This below is a decorator for class methods
    @classmethod
    def setUpTestData(cls):
        # This creates a single post in our test post table
        cls.post = Post.objects.create(text="This is a test")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test")
