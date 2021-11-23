import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# import Classes.Document as Document
# import Classes.Query as Query

@csrf_exempt
def search(request):
    # indexReader
    query = request.POST.get("searchTerm")
    # TODO return value
    # If true
    res = {"success": True,
           "docs": [
               {
                   "title": "A 31-year-old woman",
                   "description": "A 31-year-old woman with no previous medical problems comes \
                        to the emergency room with a history of 2 weeks of joint pain \
                        and fatigue. ",
                   "docId": "1",
                   "highlight": ["woman", "previous"]},
               {
                   "title": "the emergency room",
                   "description": "to the emergency room with a history of 2 weeks of joint pain \
                            and fatigue. ",
                   "docId": "2",
                   "highlight": ["emergency", "room"]}

           ]
           }
    # else
    # res = {"success":False}
    return JsonResponse(res)


@csrf_exempt
def getdoc(request):
    query = request.POST.get("docid")
    # TODO return value
    # If true
    doc = {"title": "emergency room",
           "contents": ["A 31-year-old woman with no previous medical problems comes \
                        to the emergency room with a history of 2 weeks of joint pain \
                        and fatigue.",
                        "called if the Promise is rejected. This function has one argument, \
                        the rejection reason. If it is not a function, it is internally replaced with a \
                          function (it throws an error it received as argument)"
                        ]
           }
    return JsonResponse(doc)

