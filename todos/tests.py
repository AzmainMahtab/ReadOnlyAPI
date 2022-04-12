from django.test import TestCase
from .models import Todo

# Create your tests here.
class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(tittle='Test', body="sample_body")
    
    def test_tittle_content(self):
        todo = Todo.objects.get(id='1')
        tittle_name=f'{todo.tittle}'
        self.assertEqual(tittle_name, 'Test')
    
    def test_body_content(self):
        todo = Todo.objects.get(id='1')
        tittle_name=f'{todo.body}'
        self.assertEqual(tittle_name, 'sample_body')