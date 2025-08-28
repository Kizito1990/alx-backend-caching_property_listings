# properties/utils.py
from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Fetch all properties with low-level caching.
    Cached in Redis for 1 hour (3600 seconds).
    """
    properties = cache.get("all_properties")

    if properties is None:
        properties = list(Property.objects.all().values("id", "title", "description", "price", "location"))
        cache.set("all_properties", properties, 3600)  # cache for 1 hour

    return properties
