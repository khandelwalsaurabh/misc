import phonenumbers
from phonenumbers import timezone,geocoder

#This is a sample code to try out the phonenumbers package and the various classes it provides
#Beginning in Python

phoneNumber = phonenumbers.parse("+447448615069")
timeZone = timezone.time_zones_for_number(phoneNumber)
print(timeZone)
GeoCoder=geocoder.description_for_number(phoneNumber,"en")
print(GeoCoder)
valid=phonenumbers.is_valid_number(phoneNumber)
print(valid)
possible=phonenumbers.is_possible_number(phoneNumber)
print(possible)
