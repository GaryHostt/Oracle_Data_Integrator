
#Documentation located at: https://garyhostt.github.io/OIC_start-stop/
import requests
import oci
import datetime
from datetime import date, time, datetime
import time
import sys

# Custom Signed header request work
#Verify the file location below is where you placed your API key
with open("~oci_api_key.pem") as f:
    private_key = f.read().strip()

api_key = "/".join([
    #in the parenthesis below, input yoru tenancy's root compartment's OCID
    "ocid1.tenancy.oc1..",
    #in the quotes below, input the OCID for the user
    "ocid1.user.oc1..",
    #in these quotes below, paste your API key fingerprint
    "66:ab.."
])
print(api_key)

# Universal signed header request work, leave stuff between here and line 107 alone
import base64
import email.utils
import hashlib
import httpsig_cffi.sign
import requests
import six

class SignedRequestAuth(requests.auth.AuthBase):
    """A requests auth instance that can be reused across requests"""
    generic_headers = [
        "date",
        "(request-target)",
        "host"
    ]
    body_headers = [
        "content-length",
        "content-type",
        "x-content-sha256",
    ]
    required_headers = {
        "get": generic_headers,
        "head": generic_headers,
        "delete": generic_headers,
        "put": generic_headers + body_headers,
        "post": generic_headers + body_headers
    }

    def __init__(self, key_id, private_key):
        # Build a httpsig_cffi.requests_auth.HTTPSignatureAuth for each
        # HTTP method's required headers
        self.signers = {}
        for method, headers in six.iteritems(self.required_headers):
            signer = httpsig_cffi.sign.HeaderSigner(
                key_id=key_id, secret=private_key,
                algorithm="rsa-sha256", headers=headers[:])
            use_host = "host" in headers
            self.signers[method] = (signer, use_host)

    def inject_missing_headers(self, request, sign_body):
        # Inject date, content-type, and host if missing
        request.headers.setdefault(
            "date", email.utils.formatdate(usegmt=True))
        request.headers.setdefault("content-type", "application/json")
        request.headers.setdefault(
            "host", six.moves.urllib.parse.urlparse(request.url).netloc)

        # Requests with a body need to send content-type,
        # content-length, and x-content-sha256
        if sign_body:
            body = request.body or ""
            if "x-content-sha256" not in request.headers:
                m = hashlib.sha256(body.encode("utf-8"))
                base64digest = base64.b64encode(m.digest())
                base64string = base64digest.decode("utf-8")
                request.headers["x-content-sha256"] = base64string
            request.headers.setdefault("content-length", len(body))

    def __call__(self, request):
        verb = request.method.lower()
        # nothing to sign for options
        if verb == "options":
            return request
        signer, use_host = self.signers.get(verb, (None, None))
        if signer is None:
            raise ValueError(
                "Don't know how to sign request verb {}".format(verb))

        # Inject body headers for put/post requests, date for all requests
        sign_body = verb in ["put", "post"]
        self.inject_missing_headers(request, sign_body=sign_body)

        if use_host:
            host = six.moves.urllib.parse.urlparse(request.url).netloc
        else:
            host = None

        signed_headers = signer.sign(
            request.headers, host=host,
            method=request.method, path=request.path_url)
        request.headers.update(signed_headers)
        return request

# API calls in functions

def announcements():
    print("Please input the OCID of the root compartment in your tenancy, and then press enter.")
    ID = input("")
    auth = SignedRequestAuth(api_key, private_key)
    print(auth)
    url = "https://announcements.us-ashburn-1.oraclecloud.com/20180904/announcements?compartmentId=" + ID
    payload  = {}
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, auth = auth, headers=headers, data = payload)
    print(response.text.encode('utf8'))

def start_input():
    print("Please input the OCID of your ODI Instance, and then press enter.")
    ID = input("")
    auth = SignedRequestAuth(api_key, private_key)
    print ("Instance with OCID: " + ID + " is now starting.")
    #print (ID)
    url = "https://iaas.us-ashburn-1.oraclecloud.com/20160918/instances/" + ID + "?action=start"
    payload  = {}
    headers = {
    'Content-Type': 'application/json'
    }
    print(url)
    response = requests.request("POST", url, auth = auth, headers=headers, data = payload)
    print("The response code from the OCI API is below:")
    print(response.status_code)

def stop_input():
    print("Please input the OCID of your ODI Instance, and then press enter.")
    ID = input("")
    auth = SignedRequestAuth(api_key, private_key)
    print ("Instance with OCID: " + ID + " is now stopping.")
    url = "https://iaas.us-ashburn-1.oraclecloud.com/20160918/instances/" + ID + "?action=stop"
    payload  = {}
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, auth=auth, headers=headers, data = payload)
    print("The response code from the OCI API is below:")
    print(response.status_code)

def start_adb():
    print("Please input the OCID of your ADB, and then press enter.")
    ID = input("")
    auth = SignedRequestAuth(api_key, private_key)
    print ("Instance with OCID: " + ID + " is now stopping.")
    url = "https://database.us-ashburn-1.oraclecloud.com/20160918/autonomousDatabases/" + ID + "/actions/start"
    payload  = {}
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, auth=auth, headers=headers, data = payload)
    print("The response code from the OCI API is below:")
    print(response.status_code)

def stop_adb():
    print("Please input the OCID of your ADB, and then press enter.")
    ID = input("")
    auth = SignedRequestAuth(api_key, private_key)
    print ("Instance with OCID: " + ID + " is now stopping.")
    url = "https://database.us-ashburn-1.oraclecloud.com/20160918/autonomousDatabases/" + ID + "/actions/stop"
    payload  = {}
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, auth=auth, headers=headers, data = payload)
    print("The response code from the OCI API is below:")
    print(response.status_code)

# Running the program
i = 0
while True:
    print("Hello user, input 1 and press enter to start your ODI instance, input 2 to stop your instance, and input 3 to see announcements. Press 4 to start ADB and 5 to stop ADB.")
    answer = input("")
    i += 1
    print("You have choosen option " + answer + ".")
    #print(answer)
    if answer == "1":
        print("You have choosen to start the instance.")
        start_input()
    if answer == "2":
        print("You have choosen to stop the instance.")
        stop_input()
    if answer == "3":
        announcements()
    if answer == "5":
        stop_adb()
    if answer == "4":
        start_adb()
    if i == 1:
        print("Thank you for using the OCI API today, good bye.")
        break

