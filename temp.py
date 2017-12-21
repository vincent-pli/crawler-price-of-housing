#!/usr/bin/env python
# coding=utf-8

"""
json encode/decode example
"""

from __future__ import unicode_literals

import json


def test_main():
    o = {"price": "8000", "name": "\u5fa1\u7b14\u57ce\u5e02\u5e7f\u573a", "address": "[\u00a0\u57ce\u897f\u00a0\u5927\u5174\u65b0\u533a\u00a0]\u00a0\u7ea2\u5e99\u5761\u5341\u5b57\u5411\u897f300\u7c73\u8def\u5317"}
    assert json.dumps(o)
    r = json.loads(json.dumps(o))
    assert "price" in r
    assert type(r["price"]) is unicode
    print(r["price"])
    print(type(r))

if __name__ == '__main__':
    test_main()
