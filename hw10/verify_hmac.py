import hmac
import hashlib

message = b'Ryan'
secret = b'Drew'

hmac_hash = hmac.new(secret, message, hashlib.sha256).hexdigest()
print("HMAC:", hmac_hash)

received_message = b'Ryan'
received_hmac = hmac_hash

expected_hmac = hmac.new(secret, received_message, hashlib.sha256).hexdigest()

if hmac.compare_digest(received_hmac, expected_hmac):
    print("HMAC verified")
else:
    print("HMAC not verified")