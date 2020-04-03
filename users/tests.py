from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve


class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='amir',
            email='amir@yahoo.com',
            password='testpassword',
        )

        self.assertEqual(user.username, 'amir')
        self.assertEqual(user.email, 'amir@yahoo.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@yahoo.com',
            password='adminuserpassword',
        )

        self.assertEqual(admin_user.username, 'adminuser')
        self.assertEqual(admin_user.email, 'adminuser@yahoo.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTest(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self) -> None:
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed('signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'i should not be here')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        #
        # form = self.response.context.get('form')
        # self.assertIsInstance(form, CustomUserCreationForm)
        # self.assertContains(self.response, 'csrfmiddlewaretoken')

    # def test_signup_view(self):
    #     view = resolve('/accounts/signup/')
    #     self.assertEqual(view.func.__name__, SignUp.as_view().__name__)
