from rest_framework.test import APITestCase
from .models import Tweet
from users.models import User

class TweetsTest(APITestCase):

    URL = "/api/v1/tweets/"
    USERNAME = "test_user"
    PASSWORD = "test_password"
    PAYLOAD = "test tweet"

    def setUp(self):
        self.user = User.objects.create_user(self.USERNAME)
        self.user.set_password(self.PASSWORD)
        self.user.save()
        Tweet.objects.create(user=self.user, payload=self.PAYLOAD)

    def test_get_tweets(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200, f"Expected 200, but got {response.status_code}")
        data = response.json()
        self.assertIsInstance(data, list, f"Expected list, but got {type(data)}")
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['payload'], self.PAYLOAD)
        self.assertEqual(data[0]['user']["username"], self.user.username)

    def test_post_tweet(self):
        PAYLOAD = "new tweet"
        self.client.force_login(self.user)
        response = self.client.post(self.URL, data={"payload": PAYLOAD}, user=self.user)
        self.assertEqual(response.status_code, 200, f"Expected 200, but got {response.status_code}")
        data = response.json()
        self.assertEqual(data['payload'], PAYLOAD)
        self.assertEqual(data['user']["username"], self.user.username)


class TweetDetailTest(APITestCase):

    URL = "/api/v1/tweets/1/"
    USERNAME = "test_user"
    PASSWORD = "test_password"
    PAYLOAD = "test tweet"

    def setUp(self):
        user = User.objects.create_user(self.USERNAME)
        user.set_password(self.PASSWORD)
        user.save()
        self.user = user
        tweet = Tweet.objects.create(user=user, payload=self.PAYLOAD)
        test_user = User.objects.create_user("test_user2")
        test_user.set_password("test_password2")
        test_user.save()
        self.test_user = test_user

    def test_tweet_not_found(self):
        response = self.client.get("/api/v1/tweets/2/")
        self.assertEqual(response.status_code, 404, f"Expected 404, but got {response.status_code}")

    def test_get_tweet(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200, f"Expected 200, but got {response.status_code}")
        data = response.json()
        self.assertEqual(data['payload'], self.PAYLOAD)
        self.assertEqual(data['user']["username"], self.user.username)

    def test_put_tweet(self):
        PAYLOAD = "new tweet"
        response = self.client.put(self.URL, data={"payload": PAYLOAD}, user=self.user)
        self.assertEqual(response.status_code, 403, f"Expected 403, but got {response.status_code}")

        self.client.force_login(self.user)
        response = self.client.put(self.URL, data={"payload": PAYLOAD}, user=self.user)
        self.assertEqual(response.status_code, 200, f"Expected 200, but got {response.status_code}")
        data = response.json()
        self.assertEqual(data['payload'], PAYLOAD)
        self.assertEqual(data['user']["username"], self.user.username)

        self.client.force_login(self.test_user)
        response = self.client.put(self.URL, data={"payload": PAYLOAD}, user=self.test_user)
        self.assertEqual(response.status_code, 403, f"Expected 403, but got {response.status_code}")

    def test_delete_tweet(self):
        response = self.client.delete(self.URL)
        self.assertEqual(response.status_code, 403, f"Expected 403, but got {response.status_code}")

        self.client.force_login(self.test_user)
        response = self.client.delete(self.URL)
        self.assertEqual(response.status_code, 403, f"Expected 403, but got {response.status_code}")

        self.client.force_login(self.user)
        response = self.client.delete(self.URL)
        self.assertEqual(response.status_code, 204, f"Expected 204, but got {response.status_code}")





