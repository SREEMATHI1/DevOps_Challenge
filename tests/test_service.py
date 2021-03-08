import unittest
import hello
from flask import json

def test_test():
    assert hello.test() == "Works!"
