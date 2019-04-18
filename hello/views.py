from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.db import connection

# pylint: disable=E1101

def index(request):
    send = {"Welcome":"Hey! head to ifsc or search"}
    return JsonResponse(send, status=200)

def validate_ifsc(ifsc_code):
    if len(ifsc_code) > 5 and len(ifsc_code) < 70:
        return True
    return False

@csrf_exempt
def ifscFetch(request, ifsc):
    if request.method == "GET":
        send = {}
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from bank_branches WHERE ifsc='{}'".format(ifsc))
            row = cursor.fetchone()
        if row:
            send["ifsc_code"] = row[0]
            send["bank_id"] = row[1]
            send["branch"] = row[2]
            send["city"] = row[3]
            send["district"] = row[4]
            send["state"] = row[5]
            send["bank_name"] = row[6]
        else:
            send["msg"] = "IFSC code is not linked with any bank on the database"
        return JsonResponse(send, status=200)

@csrf_exempt
def branchFetch(request):
    if request.method == "GET":
        send = {}
        if request.GET.get('name'):
            name = request.GET.get('name').strip()
        else:
            send["msg"] += "Please send name as argument, "
            return JsonResponse(send, status=200)
        if request.GET.get('city'):
            city = request.GET.get('city').strip()
        else:
            send["msg"] += "Please send city as argument"
            return JsonResponse(send, status=200)
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from bank_branches WHERE bank_name='{0}' and city='{1}'".format(name, city))
            rows = cursor.fetchall()
        details = []
        if rows:
            for row in rows:
                info = {}
                info["ifsc_code"] = row[0]
                info["bank_id"] = row[1]
                info["branch"] = row[2]
                info["city"] = row[3]
                info["district"] = row[4]
                info["state"] = row[5]
                info["bank_name"] = row[6]
                details.append(info)
        else:
            send["msg"] = "Bank name and city is not linked with any bank on the database"
        send["details"] = details
        send["banks_count"] = len(details)
        return JsonResponse(send, status=200)

@csrf_exempt
def credits(request):
    send = {"credits":"Fyle Team, Arun"}
    return JsonResponse(send, status=200)
        