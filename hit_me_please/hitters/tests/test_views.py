from django.test import TestCase
from django.http import HttpResponse

from ..models import Hitter

class LandingPageViewTest(TestCase):
    def test_view_should_have_form_with_email_field_and_submit_button(self):
        response = self.client.get("/")
	
        expected = '<form action="." method="post">'
        self.assertContains(response,expected,status_code=200)
        expected = '<input type="hidden" name="csrfmiddlewaretoken"'
        self.assertContains(response,expected,status_code=200)
        expected = '<input type="email" name="email">'
        self.assertContains(response,expected,status_code=200)
        expected = '<button type="submit">Submit</button>'
        self.assertContains(response,expected,status_code=200)

    def test_view_should_save_email_whem_submit_form(self):
        data = {
	    'email' : 'patthraphorn@prontomarketing.com'
	}
        response = self.client.post('/',data=data)
        self.assertEqual(response.status_code,200)
        count = Hitter.objects.filter(email='patthraphorn@prontomarketing.com').count()
        self.assertEqual(count,1)
