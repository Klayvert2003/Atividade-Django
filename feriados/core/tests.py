from django.test import TestCase

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    
    def test_200(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_texto(self):
        self.assertContains(self.resp, 'natal')
        
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'natal.html')

class Tiradentes(TestCase):
    def setUp(self):
        self.resp = self.client.get('/tiradentes')
    
    def test_200(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_texto(self):
        self.assertContains(self.resp, 'tiradentes')
        
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'tiradentes.html')
        
        
        
        
        
        
        
        
        
        
        