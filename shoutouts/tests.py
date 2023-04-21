from django.contrib.auth.models import User
from .models import Milestone
from rest_framework import status
from rest_framework.test import APITestCase


class MilestoneListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username="user", password="pass")

    def test_can_list_milestones(self):
        user = User.objects.get(username="user")
        Milestone.objects.create(owner=user, title="century")
        response = self.client.get("/milestones/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_logged_in_user_can_post(self):
        self.client.login(username="user", password="pass")
        response = self.client.post("/milestones/", {"title": "century"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)
