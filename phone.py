from datetime import datetime,timedelta
from twilio.rest import Client


ACCOUNT_SID='AC3448b9ad8815eeda41b237ec92c666ea'
AUTH_TOKEN='a5a3f680aec5503b7a7169c3841e869b'


client = Client(ACCOUNT_SID, AUTH_TOKEN)

for call in client.calls.list():
    print
    "From: " + call.from_formatted + " To: " + call.to_formatted

