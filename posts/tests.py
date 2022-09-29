from django.test import TestCase
from .models import Post
from django.urls import reverse

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

    def test_url_exist_at_correct_location(self):
        res = self.client.get("/")
        # check if it was fetched successfully
        self.assertEqual(res.status_code, 200)
        # self.asserEqual checks if the first arg is equal to the second arg

    def test_url_available_by_name(self):
        res = self.client.get(reverse("home"))
        self.assertEqual(res.status_code, 200)

    def test_template_name_correct(self):
        res = self.client.get(reverse("home"))
        # checks for the template rendered on that route
        self.assertTemplateUsed(res, "home.html")
    
    def test_tempate_content(self):
        res = self.client.get(reverse("home"))
        self.assertContains(res, "Message board homepage")
