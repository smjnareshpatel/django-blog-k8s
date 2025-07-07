from django.test import TestCase
from .models import Blog  # Ensure your Blog model is imported

class BlogModelTest(TestCase):
    def test_blog_creation(self):
        blog = Blog.objects.create(title="Test Title", content="Test Content")
        self.assertEqual(blog.title, "Test Title")
        self.assertEqual(blog.content, "Test Content")
