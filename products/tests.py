from django.test import TestCase
from products.forms import ProductForm


class TestProductForm(TestCase):

    def test_product_name_is_required(self):
        form = ProductForm({'name': 'Test name'})
        self.assertFalse(form.is_valid())
