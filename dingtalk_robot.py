import requests

__version__ = '0.0.3'
__author__ = 'SF-Zhou'
__email__ = 'sfzhou.scut@gmail.com'
__github__ = 'https://github.com/SF-Zhou/DingtalkRobot'
__description__ = 'Python Package for Dingtalk Robot'


class DingtalkRobot:
    BaseUrl = 'https://oapi.dingtalk.com/robot/send?access_token='

    def __init__(self, token: str):
        self.token = token
        self.access_url = self.BaseUrl + token

    def send_text(self, content: str) -> bool:
        message = {
            'msgtype': 'text',
            'text': {
                'content': content
            }
        }

        response = requests.post(url=self.access_url, json=message)
        status = response.json()
        if status['errcode'] != 0:
            raise DingtalkRobot.Error('Error Code: {}, {}'.format(
                status['errcode'],
                status['errmsg']
            ))

        return True

    class Error(ValueError):
        pass
