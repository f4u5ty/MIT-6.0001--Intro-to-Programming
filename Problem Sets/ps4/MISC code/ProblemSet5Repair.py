# -*- coding: utf-8 -*-
"""
Created on Mon May 16 02:45:17 2022

@author: f4u5t
"""

import feedparser 


d = feedparser.parse("http://feedparser.org/docs/examples/atom10.xml")
d['feed']['title']