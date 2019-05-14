from django.test import TestCase
from .models import Image, Location, Category
# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.img1=Image(image="x.jpg",image_name="scenery",image_description="an image test")

    def test_instance(self):
        self.assertTrue(isinstance(self.img1,Image))

class LocationTestClass(TestCase):
    def setUp(self):
        self.loc1=Location(location="Mombasa")

    def test_instance(self):
        self.assertTrue(isinstance(self.loc1,Location))

class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat1=Category(category="food")

    def test_instance(self):
        self.assertTrue(isinstance(self.cat1,Category))
