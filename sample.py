#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

data = json.load(open("yome.json"))

for yome in data["entries"]:

  print(u"<li>{0} : <strong>{1}</strong> ({2})</li>".format(yome["origin"], yome["name"], ", ".join(yome["element"])))
