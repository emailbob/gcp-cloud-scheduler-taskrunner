#!/usr/bin/env/ python

# Copyright 2018 Google Inc. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

    # http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Example on how to executes task based on the type of payload
"""
import time
import os
import sys
import base64

payload = base64.b64decode(sys.argv[1])
print "payload:", payload

# First word ends with .py
if payload.split()[0].endswith('.py'):
    print "Run python script"
    cmd = "python -u %s" % payload

# First word ends with .sh
if payload.split()[0].endswith('.sh'):
    print "Run the shell script"
    cmd = "sh %s" % payload

# Starts with http
if payload.startswith('http'):
    print "Run curl"
    cmd = "curl %s" % payload

try:
    print cmd
    os.system(cmd)
except:
    pass

sys.exit(0)