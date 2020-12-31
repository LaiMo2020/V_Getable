from django.test import TestCase
from products.forms import ProductForm


class TestProductForm(TestCase):

    def test_product_name_is_required(self):
        form = ProductForm({'name': 'Test name'})
        self.assertFalse(form.is_valid())


class TestViews(TestCase):

    def test_view_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
