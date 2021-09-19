from django.http import JsonResponse
from django.db import connection
from django.shortcuts import render


def dashboard(request):
    query = "SELECT * FROM graph_agentsession LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(query)

    return render(request, 'dashboard.html')


def draw_graph(request):
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

    query = """ SELECT time, count(*) as active_count FROM (
        SELECT strftime('%Y-%m-%d %H', callStartTime) as time FROM graph_agentsession UNION ALL 
        SELECT strftime('%Y-%m-%d %H', callEndTime) as time FROM graph_agentsession)
        {} GROUP BY time 
    """.format(filter_range)

    cursor = connection.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        labels.append(row[0])
        data.append(row[1])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })