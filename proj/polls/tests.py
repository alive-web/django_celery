from django.test import TestCase
from utils import my_func


class UtilsTests(TestCase):

    def test_my_func(self):
        self.assertEqual(my_func(), 'cool')
