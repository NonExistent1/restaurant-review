"""
Jordyn Kuhn
CIS 218
2-28-2024
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Review, Restaurant

class ReviewTests(TestCase):
    """Review Tests"""

    @classmethod
    def setUpTestData(cls):
        """set up test data"""
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="test123"
        )

        cls.restaurant = Restaurant.objects.create(
            name="testrestaurant"
        )

        cls.review = Review.objects.create(
            restaurant=cls.restaurant,
            author=cls.user,
            body="testbody",
            rating=5
        )

    """
    Test Models
    
    """
    def test_restaurant_model(self):
        """Test restaurant model"""
        self.assertEqual(self.restaurant.name, "testrestaurant")
        self.assertEqual(str(self.restaurant), "testrestaurant")
        self.assertEqual(self.restaurant.get_absolute_url(), "/restaurant/1/")

    def test_review_model(self):
        """test review model"""
        self.assertEqual(self.review.restaurant.name, "testrestaurant")
        self.assertEqual(self.review.author.username, "testuser")
        self.assertEqual(self.review.body, "testbody")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(str(self.review), "testbody")
        self.assertEqual(self.review.get_absolute_url(), "/review/1/")

    """
    Test URLs
    """

    def test_url_exists_at_correct_location_restaurant_listview(self):
        """Test url exists at correct location restaurant listview"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_restaurant_detailview(self):
        """test url exists at correct location restaurant detail view"""
        response = self.client.get("/restaurant/1/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_review_detailview(self):
        """test url exists at correct location review detailview"""
        response = self.client.get("/review/1/")
        self.assertEqual(response.status_code, 200)

    """
    Test Views
    """

    def test_restaurant_listview(self):
        """test restaurant list view"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testrestaurant")
        self.assertTemplateUsed(response, "home.html")

    def test_restaurant_detailview(self):
        """test restaurant detail view"""
        response = self.client.get(reverse("restaurant_detail", kwargs={"pk":self.restaurant.pk}))
        self.assertEqual(response.status_code, 200)
        noresponse = self.client.get("/restaurant/1000000/")
        self.assertEqual(noresponse.status_code, 404)
        self.assertContains(response, "testrestaurant")
        self.assertTemplateUsed(response, "restaurant_detail.html")

    def test_review_detailview(self):
        """test review detail view"""
        response = self.client.get(reverse("review_detail", kwargs={"pk":self.review.pk}))
        self.assertEqual(response.status_code, 200)
        noresponse = self.client.get("/review/1000000/")
        self.assertEqual(noresponse.status_code, 404)
        self.assertContains(response, "testbody")
        self.assertTemplateUsed(response, "review_detail.html")
        

    def test_review_createview(self):
        """test review create view"""
        response = self.client.post(
            reverse("review_new"),
            {
                "restaurant":self.restaurant.name,
                "author":self.user.id,
                "body":"New body",
                "rating":4
            }                
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.last().rating, 4)
        self.assertEqual(Review.objects.last().body, "New body")
    
    def test_review_updateview(self):
        """test review update view"""
        response = self.client.post(
            reverse("review_edit", args="1"),
            {
                "rating": 3,
                "body": "updated body",
                "author":self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.last().rating, 3)
        self.assertEqual(Review.objects.last().body, "updated body")
        self.assertEqual(Review.objects.last().restaurant, "testrestaurant")

    def test_review_deleteview(self):
        """test review delete view"""
        response = self.client.post(reverse("review_delete", args="1"))
        self.assertEqual(response.status_code, 302)
         


    
