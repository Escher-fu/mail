# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 15:48:14 2018

@author: CCC
"""

from email.mime.text import MIMEText
from email.header import Header

# 书写邮件内容
content = """

            <meta>您好！</meta>

            <p></p>

            <meta>很高兴和你见面:)。</meta>

        """
# 书写邮件主题
subject = 'python email test'


def get_mail_message():
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    return(msg)
