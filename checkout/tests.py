from django.test import TestCase
from checkout.forms import OrderForm
""" Testing full name, email adress,
and post code are required/ adress2 not required """


class TestOrderForm(TestCase):

    def test_full_name_is_required(self):
        form = OrderForm({'full_name': 'Test name'})
        self.assertFalse(form.is_valid())

    def test_email_address_is_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_street_address2_is_not_required(self):
        form = OrderForm({'full_name': 'Test Name'
                          'email:' 'Test email'
                          'street_address1:' 'Test Address'
                          'town_or_city:' 'Test Town or City'
                          'postcode:' 'Test Postcode'
                          'phone_number:' 'Phone Number',
                          'county': 'Test County'})
        self.assertFalse(form.is_valid())
