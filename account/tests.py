from django.test import TestCase
from .models import Profile,Image,Comment




# Create your tests here.

class ImageTestClass(TestCase):
    '''
    set up method
    '''
def setUp(self):
   self.user = User.objects.create_user('fanny')
   self.user.save()

def test_instance(Self):
    self.image.save()
    self.assertTrue(isinstance(self.Image.Image))

def test_save_method(self):
    self.image.save_image()
    images=Image.objects.all()
    self.assertTrue(len(images)>0)



