#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import yaml
import urllib

url_prefix = 'https://review.openstack.org/#/dashboard/?'
html_template = '<meta http-equiv="refresh" content="0; URL=%s"'


def generate_review_dash():
    stream = open('trove-dash.yaml', 'r')
    conf = yaml.load(stream)[0]['Dashboard']
    url = url_prefix + urllib.urlencode(conf).replace('%2C', '%252C')
    with open("reviews.htm", "w") as html_file:
        html_file.write(html_template % url)

if __name__ == '__main__':
    generate_review_dash()
