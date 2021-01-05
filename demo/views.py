from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Record
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):

    return render(request, 'demo/index.html')


@csrf_exempt
def get_new_record(request):

    record = Record.objects.filter(is_processed=False).first()
    if record is not None:
        json = record.json

        record.is_processed = True
        record.save()

        return JsonResponse(json, safe=False)
    else:
        return HttpResponse(status=200)

@csrf_exempt
def get_records(request):

    records = Record.objects.all().order_by('-id')
    json = []

    if records is not None:

        for record in records:
            json.append(record.json)

        return JsonResponse(json, safe=False)
    else:
        return HttpResponse(status=200)


@csrf_exempt
def add_record(request):

    data = json.loads(request.body)
    data_type = data.get('data_type', None)

    if data_type == "alpr_group":
        # print("saving json")
        record_instance = Record()
        record_instance.json = data
        record_instance.save()

    return HttpResponse(status=202)