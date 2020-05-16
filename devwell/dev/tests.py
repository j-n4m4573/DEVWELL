from django.test import TestCase

class ReviewsTests(TestCase):
    def test_review_list_page(self):    
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_review_detail_page(self):  
    response = self.client.get('review/1')
    self.assertEqual(response.status_code, 200)
    
