#!/usr/bin/env python

import re

prog = re.compile(r"(\[)(.*)(\])")
result = prog.search("yyy[xxx]yyy")
print(result)
print(result.group(2))
