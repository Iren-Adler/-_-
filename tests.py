from django.test import TestCase
from django.test import Client
from core import models

class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.animal = models.Animal.objects.create(
            name='Кабан',
            type='mammal',
            population=15,
            is_rare=True
        )

    def test_index(self):
        response = self.client.get('/index/')
        self.assertEquals(response.status_code, 200)

    def test_detail_animal(self):
        response = self.client.get(f'/animal/{self.animal.id}/')
        self.assertEquals(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEquals(response.status_code, 302)
