import unittest

from msg91.services.otp_service import OTPService

class TestCampaignService(unittest.TestCase):
    otp_service = OTPService()

    response = otp_service.verify_token('your_authkey', 'your_token')

    print(response)

if __name__ == '__main__':
    unittest.main()


# run the test : python3 -m unittest tests.test_campaign_service