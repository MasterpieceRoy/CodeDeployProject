# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase


class LogInTest(TestCase):
    print("The users present are ")
    user = User.objects.all()
    for i in user:
        print(i)
    print("-------------------------------------------------------------")

    def setUp(self):
        self.credentials = {
            'username': 'John',
            'password': 'zxcvbnml'}
        print("Register Test Case is running \n")
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
        print("Login Test Case is running \n")

    def test_logout(self):
        response = self.client.get('/logout/')
        print("Log out Test Case is running \n")
