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


import os
import urllib

import yaml

url_prefix = 'https://review.openstack.org/#/dashboard/?'
html_template = (
    '<meta http-equiv="Cache-Control" '
    'content="no-cache, no-store, must-revalidate" /> '
    '<meta http-equiv="Pragma" content="no-cache" /> '
    '<meta http-equiv="Expires" content="0" /> '
    '<meta http-equiv="refresh" content="0; URL=%s">')


def generate_review_dash(filename):
    stream = open(filename, 'r')

    yaml_data = yaml.load(stream)
    conf = yaml_data[0]['Dashboard']
    desc = yaml_data[1]['Description']
    url = url_prefix + urllib.urlencode(conf).replace('%2C', '%252C')

    title = os.path.splitext(filename)[0]
    dashname = title + ".htm"

    with open(dashname, "w") as html_file:
        html_file.write(html_template % url)

    return title, desc


def list_to_html_table(list):
    yield '<table style="width:300px">'
    for sublist in list:
        yield '  <tr> <td>'
        yield '    </td><td>'.join(sublist)
        yield '  </td></tr>'
    yield '</table>'


def generate_review_dashes():
    table = []
    for filename in os.listdir("./"):
        if filename.endswith(".yaml"):
            title, desc = generate_review_dash(filename)
            href = '<a href="%s.htm">%s</a>' % (title, title)
            table.append([href, desc])
    with open("index.htm", "w") as index_file:
        index_file.write('\n'.join(list_to_html_table(table)))


if __name__ == '__main__':
    generate_review_dashes()
