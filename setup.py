"""
Python Package for Dingtalk Robot
Author: SF-Zhou
Date: 2018-03-15
"""

from setuptools import setup


setup(
    name='dingtalk_robot',
    version='0.0.5',
    description='Python Package for Dingtalk Robot',
    url='https://github.com/SF-Zhou/DingtalkRobot',
    author='SF-Zhou',
    author_email='sfzhou.scut@gmail.com',

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='tools dingtalk robot',
    py_modules=['dingtalk_robot'],
    install_requires=['requests'],
    extras_require={'test': ['pytest']}
)
