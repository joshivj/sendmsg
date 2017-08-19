# import the Twilio client from the dependency
from twilio.rest import Client

# put your twilio credentials here
account_sid = "{{your_account_sid}}" # get it from https://www.twilio.com/console/phone-numbers/runtime/test-credentials
auth_token = "{{your_authentication_code}}"

client = Client(account_sid, auth_token)

media_url = "https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg"

response = client.messages.create(
    to= "{{enter_your_twillio_account_phone_number}}", #https://www.twilio.com/console/phone-numbers/verified
    from_= "+15005550006", #+15005550006 will be used for trial account.
    body= "Hello, how you doing ?",
    media_url= media_url # if you need to attach multimedia to your message, else remove this parameter.
    )