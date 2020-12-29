from django.test import TestCase
from blog.forms import CommentForm


class TestViews(TestCase):

    def test_view_all_posts(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')


class TestCommentForm(TestCase):

    def test_name_is_required(self):
        form = CommentForm({'name': 'Test name'})
        self.assertFalse(form.is_valid())

    def test_email_is_required(self):
        form = CommentForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_comment_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')
