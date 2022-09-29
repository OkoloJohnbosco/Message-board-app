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

    # 2
    def test_url_exist_at_correct_location(self):
        res = self.client.get("/")
        # check if it was fetched successfully
        self.assertEqual(res.status_code, 200)
        # self.asserEqual checks if the first arg is equal to the second arg

    # 3
    def test_url_available_by_name(self):
        res = self.client.get(reverse("home"))
        self.assertEqual(res.status_code, 200)

    # 4
    def test_template_name_correct(self):
        res = self.client.get(reverse("home"))
        # checks for the template rendered on that route
        self.assertTemplateUsed(res, "home.html")

    # 5
    def test_tempate_content(self):
        res = self.client.get(reverse("home"))
        self.assertContains(res, "This is a test")

    # We can combine all the test above (from 2-5)  to one test
    def test_homepage(self):
        res = self.client.get(reverse("home"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "home.html")
        self.assertContains(res, "This is a test")
