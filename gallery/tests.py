from django.test import TestCase
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Test Category')

class ImageTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        image_content = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        self.image = Image.objects.create(
            title='Test Image',
            image=image_content,
            age_limit=18,
            created_date=datetime.date.today()
        )
        self.image.categories.add(self.category)

    def test_image_creation(self):
        self.assertEqual(self.image.title, 'Test Image')
        self.assertEqual(self.image.age_limit, 18)
        self.assertEqual(self.image.created_date, datetime.date.today())
        self.assertIn(self.category, self.image.categories.all())
