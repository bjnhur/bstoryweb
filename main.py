#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import datetime
from google.appengine.api import mail

class MainHandler(webapp2.RequestHandler):
    def get(self):
        temp_value = self.request.get("temp")
        expires_date = datetime.datetime.utcnow() + datetime.timedelta(365)
        expires_str = expires_date.strftime("%d %b %Y %H:%M:%S GMT")        
        self.response.write('Hello world!')
        sender_address = "bjnhur@gmail.com" # just example, should change
        user_address = "bjnhur@gmail.com" # fix address, for general usage, should change the code and address.
        subject = "Current Temp is %s" % temp_value
        body = """
smsMail
%s
""" % expires_str
        mail.send_mail(sender_address, user_address, subject, body)
        self.response.write('Done')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)




