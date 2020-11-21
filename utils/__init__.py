import random
import string

import configs
from models.URL.models import URL


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def create_random_short_link(short_link=None, length=10):
    while not short_link:
        short_link = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
        if URL.objects.filter(short_addr=short_link):
            continue
        return short_link
    if URL.objects.filter(short_addr=short_link):
        return None
    return short_link
