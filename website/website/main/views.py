import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Printer


shutdown = False


def home(request):
    if request.method == "POST":
        if request.POST.get("pause-print") == "yes":
            global shutdown
            shutdown = True

    return render(request, 'main/home.html')


@csrf_exempt
def api(request):
    if request.method == "GET":
        obj = Printer.objects.get(pk=1)

        response = {
            "printer": [{
                "printer_name": obj.printer_name,
                "printer_status": obj.printer_status,
                "printer_progress": obj.printer_progress,
                "temperature": {
                    "t0": {
                        "actual": obj.t0_temp_actual,
                        "set": obj.t0_temp_set
                    },
                    "bed": {
                        "actual": obj.bed_temp_actual,
                        "set": obj.bed_temp_set
                    }
                }
            }]
        }
        return JsonResponse(response)

    elif request.method == "POST":
        if request.headers.get("key") != "eaac1b4422a5bc41e20c059c10caf9569bbd61755ad603403eb61c2c2b934590":
            return HttpResponse("Error", status=500)

        global shutdown
        body = json.loads(request.body)
        obj = Printer.objects.get(pk=1)

        obj.printer_status = body["printer"][0]["printer_status"]
        obj.printer_progress = body["printer"][0]["printer_progress"]
        obj.t0_temp_actual = body["printer"][0]["temperature"]["t0"]["actual"]
        obj.t0_temp_set = body["printer"][0]["temperature"]["t0"]["set"]
        obj.bed_temp_actual = body["printer"][0]["temperature"]["bed"]["actual"]
        obj.bed_temp_set = body["printer"][0]["temperature"]["bed"]["set"]
        obj.save()

        if shutdown:
            shutdown = False
            return HttpResponse(status=418)

        return HttpResponse(status=200)

    return HttpResponse("Error", status=500)

# eaac1b4422a5bc41e20c059c10caf9569bbd61755ad603403eb61c2c2b934590
# Kai Mortsiefer, 1520266, Uni Wuppertal, Bachelor Thesis 2022
# SHA3-256 hashed
