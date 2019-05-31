#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: weakscan洞库
referer: unknow
author: Lucifer
description: 包含所有.洞类型，封装成一个模块
'''
from .Weak_SSH_Scan import Weak_SSH_Scan
from .Weak_FTP_Scan import Weak_FTP_Scan

# 扫描FTP和SSH
# 以两种形式扫描SSH和FTP：
# 已知用户扫描密码
# 已知密码扫描用户