import unittest
from dingtalk_robot import DingtalkRobot


class MyTestCase(unittest.TestCase):
    valid_token = 'e2bfbac46ed921563dcd852ae65b3adc7797db997ea6c2cc75843b74e4365842'
    invalid_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    def test_send_text(self):
        dingtalk_robot = DingtalkRobot(token=self.valid_token)
        success = dingtalk_robot.send_text('Send text to Dingding')
        self.assertTrue(success)

    def test_send_text_to_invalid_token(self):
        dingtalk_robot = DingtalkRobot(token=self.invalid_token)
        error_here = False

        try:
            dingtalk_robot.send_text('Send text to Dingding')
        except dingtalk_robot.Error as e:
            error_here = True

        self.assertTrue(error_here)


if __name__ == '__main__':
    unittest.main()
