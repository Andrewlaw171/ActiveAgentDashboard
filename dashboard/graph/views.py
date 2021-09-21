import pandas as pd

from datetime import timedelta, datetime
from django.http import JsonResponse
from django.db import connection
from django.shortcuts import render

from .utils.batch_load_json import create_active_agent_table, json_to_db


def dashboard(request):
    return render(request, 'dashboard.html')


def draw_graph(request):
    # json_to_db("C:/Users/Andrew/Desktop/takehomes/operata/tech_test.json")
    # create_active_agent_table()

    labels = []
    data = []
    from_date = ""
    to_date = ""
    filter_range = ""

    print(request.GET)

    from_date = request.GET['fromDatetime']
    to_date = request.GET['toDatetime']

    if from_date != "" and to_date != "":
        filter_range = "WHERE time >= '{}' AND time <= '{}'".format(from_date[:-3], to_date[:-3])
        filter_range = filter_range.replace('/', '-')
        print(filter_range)

    query = "SELECT * FROM graph_activeagentsperhour " + filter_range
    cursor = connection.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        labels.append(row[2])
        data.append(row[1])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
