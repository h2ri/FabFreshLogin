from django.http import HttpResponse
from django.contrib.auth import login
from social.apps.django_app.utils import psa
from .tools import get_access_token
import json
import requests

from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from .serializers import UserSerializer,UserInfoSerializer
from .models import UserInfo
from rest_framework import viewsets
from .permission import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #http_method_names = ['get', 'put', 'head' ,'patch']
    permission_classes = [permissions.IsAuthenticated,TokenHasReadWriteScope]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)

class UserInfoViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    #queryset = UserInfo.objects.all()
    permission_classes = [permissions.IsAuthenticated,TokenHasReadWriteScope]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserInfo.objects.all()
        else:
            return UserInfo.objects.filter(owner=self.request.user.id)

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(owner=self.request.user)



@psa('social:complete')
def register_by_access_token(request, backend):

    token = request.GET.get('access_token')
    number = request.GET.get('number')
    email = request.GET.get('email')

    try:
        user = request.backend.do_auth(token)
        if user:
            login(request, user)
            if email:
                u = User.objects.get(id = user.id)
                u.email = email
                u.save()
            return get_access_token(user)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return HttpResponse("Error",status=status.HTTP_404_NOT_FOUND)


class CheckAvailabilityApiView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self,request, *args, **kw):
        payload1 = request.data
        url = 'http://128.199.241.199/v1/orders/serviceability'
        headers = {'Authorization' : 'Bearer 4RaJAmtaOEfHJu1dkyWIUVGmckcTizGXyyxPFIgy' , 'Content-Type' : 'application/json'}
        r = requests.post(url, json.dumps(payload1), headers=headers)
        response = Response(r.json(),status=status.HTTP_200_OK)
        return response

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


