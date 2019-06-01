from django.test import TestCase
from .models import Hitter
from django.contrib import admin 
from .admin import HitterAdmin
class HitterTest(TestCase):
    def test_hitter_model_should_have_email_field(self):
        hitter = Hitter.objects.create(
            email='patthraphorn@prontomarketing.com'
        )
        self.assertEqual(hitter.email, 'patthraphorn@prontomarketing.com')

class HitterAdminTest(TestCase):
    def test_hitter_should_be_registed_to_admin(self):
        self.assertIsInstance(
	    admin.site._registry[Hitter],
	    HitterAdmin
	)