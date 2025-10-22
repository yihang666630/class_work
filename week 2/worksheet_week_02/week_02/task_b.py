"""
@author: Yihang Yu
Leeds ID: 201913006
The code is my own work. 
"""

import re
title = input ("enter the title of the book:")
sw = ["a", "the"]
slug_temp_1 =  re.sub("[^A-Za-z0-9]+", " ", title).strip()
slug_temp_2 = '-'.join([word for word in slug_temp_1.split() if word not in sw]).lower()
slug = slug_temp_2[:25]
print (f"Slug = {slug}")