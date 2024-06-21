# -*- coding:utf-8 -*-
"""
 @author: huang
 @date: 2024-05-21
 @File: utils.py
 @Description: 
"""
import hashlib

def gen_sign(body, secret_key):
    return hashlib.md5((body + "." + secret_key).encode('utf-8')).hexdigest()