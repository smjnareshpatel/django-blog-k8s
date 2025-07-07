from rest_framework.test import APITestCase
from rest_framework import status
from blog.models import Blog

class TestBlogAPI(APITestCase):
    def setUp(self):
        self.blog_data = {
            "title": "First Blog",
            "content": "This is the content of the first blog."
        }
        self.blog = Blog.objects.create(**self.blog_data)

    def test_create_blog(self):
        data = {
            "title": "New Blog",
            "content": "New blog content."
        }
        response = self.client.post("/api/blogs/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 2)
        self.assertEqual(response.data["title"], data["title"])

    def test_list_blogs(self):
        response = self.client.get("/api/blogs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_blog(self):
        response = self.client.get(f"/api/blogs/{self.blog.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.blog.title)

    def test_update_blog(self):
        updated_data = {
            "title": "Updated Blog",
            "content": "Updated content."
        }
        response = self.client.put(f"/api/blogs/{self.blog.id}/", updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.title, "Updated Blog")

    def test_delete_blog(self):
        response = self.client.delete(f"/api/blogs/{self.blog.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Blog.objects.count(), 0)
