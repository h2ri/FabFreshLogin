from django.http import HttpResponse
from django.contrib.auth import login
from social.apps.django_app.utils import psa
from .tools import get_access_token
from .models import UserDetails
from .serializers import UserDetailsSerializer
import json
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# When we send a third party access token to that view
# as a GET request with access_token parameter,
# python social auth communicate with
# the third party and request the user info to register or
# sign in the user. Magic. Yeah.


class profileApiView(APIView):
    def post(self,request, *args, **kw):
        serializer = UserDetailsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def index(request):
    placeOrder()
    return HttpResponse("ttesting")

@psa('social:complete')
def register_by_access_token(request, backend):
 
    token = request.GET.get('access_token')
    number = request.GET.get('number')
    email = request.GET.get('email')

    # here comes the magic
    user = request.backend.do_auth(token)
    UserProfile.objects.all()

    if user:
        login(request, user)
        # that function will return our own
        # OAuth2 token as JSON
        # Normally, we wouldn't necessarily return a new token, but you get the idea

        return get_access_token(user)
    else:
        # If there was an error... you decide what you do here
        return HttpResponse("error")

class PlaceOrderShipment(APIView):
    def post(self,request, *args, **kw):
        payload = {
        "pickup": {
            "user": {
            "name": "Samsung store",
            "phone_no": "08056190907",
            "email": "samsung@gmail.com",
            "type": "merchant",
            "external_id": "BLR-NAT-123",
            "full_address": {
                "address": "Shop no 51,5th block",
                "locality": {
                    "name": "Koramangala"
                },
                "sub_locality": {
                    "name": "5th block"
                },
                "city": {
                    "name": "Bangalore"
                },
                "geo": {
                    "latitude": "12.935322",
                    "longitude": "77.618754"
                }
            }
        }
    },
    "drop": {
        "user": {
            "name": "Joe",
            "phone_no": "9656190907",
            "email": "joe@gmail.com",
            "external_id": "MND-756",
            "type": "customer",
            "full_address": {
                "address": "apartments, 6th block",
                "locality": {
                    "name": "Koramangala"
                },
                "sub_locality": {
                    "name": "6th block"
                },
                "city": {
                    "name": "Bangalore"
                },
                "geo": {
                    "latitude": "12.943834",
                    "longitude": "77.623928"
                }
            }
        }
    },
    "order_details": {
        "order_id": "last2091020",
        "order_value": "255.0",
        "amount_to_be_collected": "234.45",
        "order_type": {
            "name": "Cash On Delivery"
        },
        "order_items": [
            {
                "quantity": 1,
                "price": 120,
                "item": {
                    "name": "Samsung screen Guard"
                }
            },
            {
                "quantity": 1,
                "price": 535,
                "item": {
                    "name": "Samsung charger"
                }
            }
        ]
    },
    "created_at": "2015-05-05 01:50",
    "callback_url": "callback/url"
    }


        url = 'http://128.199.241.199/v1/orders/serviceability'
        headers = {'Authorization' : 'Bearer 4RaJAmtaOEfHJu1dkyWIUVGmckcTizGXyyxPFIgy' , 'Content-Type' : 'application/json'}
        r = requests.post(url, json.dumps(payload), headers=headers)

        response = Response(r.json(),status=status.HTTP_200_OK)
        return response



class CheckAvailabilityApiView(APIView):

    def post(self,request, *args, **kw):
        payload = {
        "pickup": {
            "user": {
            "name": "Samsung store",
            "phone_no": "08056190907",
            "email": "samsung@gmail.com",
            "type": "merchant",
            "external_id": "BLR-NAT-123",
            "full_address": {
                "address": "Shop no 51,5th block",
                "locality": {
                    "name": "Koramangala"
                },
                "sub_locality": {
                    "name": "5th block"
                },
                "city": {
                    "name": "Bangalore"
                },
                "geo": {
                    "latitude": "12.935322",
                    "longitude": "77.618754"
                }
            }
        }
    },
    "drop": {
        "user": {
            "name": "Joe",
            "phone_no": "9656190907",
            "email": "joe@gmail.com",
            "external_id": "MND-756",
            "type": "customer",
            "full_address": {
                "address": "apartments, 6th block",
                "locality": {
                    "name": "Koramangala"
                },
                "sub_locality": {
                    "name": "6th block"
                },
                "city": {
                    "name": "Bangalore"
                },
                "geo": {
                    "latitude": "12.943834",
                    "longitude": "77.623928"
                }
            }
        }
    },
    "order_details": {
        "order_id": "last2091020",
        "order_value": "255.0",
        "amount_to_be_collected": "234.45",
        "order_type": {
            "name": "Cash On Delivery"
        },
        "order_items": [
            {
                "quantity": 1,
                "price": 120,
                "item": {
                    "name": "Samsung screen Guard"
                }
            },
            {
                "quantity": 1,
                "price": 535,
                "item": {
                    "name": "Samsung charger"
                }
            }
        ]
    },
    "created_at": "2015-05-05 01:50",
    "callback_url": "callback/url"
    }


        url = 'http://128.199.241.199/v1/orders/serviceability'
        headers = {'Authorization' : 'Bearer 4RaJAmtaOEfHJu1dkyWIUVGmckcTizGXyyxPFIgy' , 'Content-Type' : 'application/json'}
        r = requests.post(url, json.dumps(payload), headers=headers)

        response = Response(r.json(),status=status.HTTP_200_OK)
        return response



def placeOrder():
    payload = {
    "pickup": {
        "user": {
            "name": "Samsung store",
            "phone_no": "08056190907",
            "email": "samsung@gmail.com",
            "type": "merchant",
            "external_id": "BLR-NAT-123",
            "full_address": {
                "address": "Shop no 51,5th block",
                "locality": {
                    "name": "Koramangala"
                },
                "sub_locality": {
                    "name": "5th block"
                },
                "city": {
                    "name": "Bangalore"
                },
                "geo": {
                    "latitude": "12.935322",
                    "longitude": "77.618754"
                }
            }
        }
    },
    "drop": {
        "user": {
            "name": "Joe",
            "phone_no": "9656190907",
            "email": "joe@gmail.com",
            "external_id": "MND-756",
            "type": "customer",
            "full_address": {
                "address": "apartments, 6th block",
                "locality": {
                    "name": "Koramangala"
                },
                "sub_locality": {
                    "name": "6th block"
                },
                "city": {
                    "name": "Bangalore"
                },
                "geo": {
                    "latitude": "12.943834",
                    "longitude": "77.623928"
                }
            }
        }
    },
    "order_details": {
        "order_id": "last2091020",
        "order_value": "255.0",
        "amount_to_be_collected": "234.45",
        "order_type": {
            "name": "Cash On Delivery"
        },
        "order_items": [
            {
                "quantity": 1,
                "price": 120,
                "item": {
                    "name": "Samsung screen Guard"
                }
            },
            {
                "quantity": 1,
                "price": 535,
                "item": {
                    "name": "Samsung charger"
                }
            }
        ]
    },
    "created_at": "2015-05-05 01:50",
    "callback_url": "callback/url"
    }


    #to ship
    '''url = 'http://128.199.241.199/v1/orders/ship'
    headers = {'Authorization' : 'Bearer 4RaJAmtaOEfHJu1dkyWIUVGmckcTizGXyyxPFIgy'}
    r = requests.post(url, json.dumps(payload),headers=headers)
    '''
    #to check ServiceAvailability
    url = 'http://128.199.241.199/v1/orders/serviceability'
    headers = {'Authorization' : 'Bearer 4RaJAmtaOEfHJu1dkyWIUVGmckcTizGXyyxPFIgy' , 'Content-Type' : 'application/json'}
    r = requests.post(url, json.dumps(payload), headers=headers)
    print(r.text)
    print(r.json())

    #to track order
    '''url = 'http://128.199.241.199/v1/orders/475e24b4/track'
    r = requests.get(url);
    print(r.text)'''
