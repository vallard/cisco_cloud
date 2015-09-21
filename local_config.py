'''
    Site specific configuration details for an implementation.
    Used to store server info, authentication keys, base urls, etc

    Update with your relevant information before running CLI scripts OR using the xxxd_library.py modules
'''

__author__ = 'hapresto'

# UCS Director Access Info  -  Update for your install
ucsdserver = "ucsd.local.intra"
ucsd_key = "XXXXXX"

# ICF Director Access Info  -  Update for your Install
# The ICFD Key can be found by clicking on the top right corner of the ICF web interface
# by clicking on the name of the logged in user (e.g.: admin) and then selecting the 'Advanced'
# tab.  From there you can copy the key value and put it below. 
#icfdserver = "icfd.local.intra"
#icfd_key = "XXXXXXXX"
icfdserver = "198.18.134.44"
icfd_key = "74F5DAF33CCC4FC19DDAB94B36BE8694"

# This information should stay the same for all users
url = "http://%s/app/api/rest?"
getstring = "formatType=json&opName=%s"
parameter_lead = "&opData="
headers = {"X-Cloupia-Request-Key":" "}

