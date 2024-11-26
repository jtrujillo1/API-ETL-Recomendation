from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser

class UserTests(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin123', role='admin'
        )
        self.user = CustomUser.objects.create_user(
            username='user', email='user@example.com', password='user123', role='user'
        )

    def test_register_user(self):
        data = {"username": "newuser", "email": "newuser@example.com", "password": "password123"}
        response = self.client.post('/api/users/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_users_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get('/api/users/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deactivate_user(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(f'/api/users/users/{self.user.id}/deactivate/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)
