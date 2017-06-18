#!/usr/bin/python3
import unittest

from src.rest import RestCall


class RestCallTestCase(unittest.TestCase):
    def setUp(self):
        # headers
        self.headers = {
            "Authorization": "key=AIzaSyB1JJL0LnSdkMKy8ZXTz7AVNxNxver0qN8",
            "Content-Type": "application/json"
        }

        # data to send
        self.data = {
            "to": "dTm4uGxgdwU:APA91bFUmvZAAB8ycXgy9_qHR2dswFSK4maQYZxHoI5Oeg5VOUAr77_mBKVAmponeco3JLh58k2tuyEozj-JpoluwzBAgoHCu5aFb1ZFpZLMN6gi5SL5VkrE2s-UoSxZPjDO_eqCSnaR",
            "notification": {
                "body": "YOU LEFT THE CAR OPEN FOR MORE THAN 15 MIN",
                "title": "Warning"
            },
            "data": {
                "MESAGE": "YOU LEFT THE CAR OPEN FOR MORE THAN 15 MIN"
            }
        }

        self.res = RestCall('android.googleapis.com', '/gcm/send', 'POST', self.headers, self.data)

    def runTest(self):
        self.test_send()
        self.test_send_local()

    def test_send(self):
        self.res.send()

    def test_send_local(self):
        res = RestCall('house-net.ddns.net', '/web-api/index.php/test', 'DELETE', self.headers, self.data)
        res.send()

if __name__ == '__main__':
    unittest.main()