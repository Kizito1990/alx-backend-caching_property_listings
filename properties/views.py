# properties/views.py
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Property

@cache_page(60 * 15)  # cache for 15 minutes
def property_list(request):
    properties = Property.objects.all().values("id", "title", "description", "price", "location")
    return JsonResponse({
        "data": list(properties)
    })

