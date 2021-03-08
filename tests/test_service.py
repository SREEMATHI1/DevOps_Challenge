import unittest
import web_service
from flask import json

def test_test():
    assert web_service.test() == "Works!"
