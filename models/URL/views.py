# Create your views here.
import threading
from datetime import datetime

import redis
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import configs
from UrlShortener import settings
from models.URL.models import URL
from models.URL.serializers import URLSerializer
from models.visitor.models import Visitor
from utils import get_client_ip, create_random_short_link


class RedirectView(APIView):

    serializer_class = URLSerializer
    redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)
    queryset = None

    def get(self, request, short_addr):
        address = self.redis_instance.get(short_addr)
        if address:
            threading.Thread(target=self.create_visitor(short_addr=short_addr))
            return Response({'address': address})
        url = URL.objects.filter(short_addr=short_addr)
        if url:
            self.queryset = url
            threading.Thread(target=self.create_visitor())
            self.redis_instance.set(short_addr, url.first().address, configs.REDIS_TIMEOUT)
            serializer = URLSerializer(url.first())
        return Response(serializer.data)

    def create_visitor(self, short_addr=None):
        if not self.queryset:
            self.queryset = URL.objects.filter(short_addr=short_addr)
        device = Visitor.MOBILE if self.request.user_agent.is_mobile else Visitor.DESKTOP
        Visitor.objects.create(url=self.queryset.first(), date=datetime.now(),
                               browser=self.request.user_agent.browser.family.lower(),
                               device=device,
                               ip=get_client_ip(self.request))
        self.queryset = None


class CreateShortLink(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        address = request.data.get('address', None)
        if not address:
            return Response(configs.ADDRESS_NOT_SENT, status=status.HTTP_412_PRECONDITION_FAILED)
        short_link = request.data.get('short_link', None)
        short_link = create_random_short_link(short_link=short_link)
        if not short_link:
            return Response(configs.REPEATITIVE_SHORT_LINK, status=status.HTTP_412_PRECONDITION_FAILED)
        url = URL.objects.create(owner=request.user, address=address, short_addr=short_link)
        return Response(URLSerializer(url).data)