import json
import pandas as pd
from datetime import datetime, timedelta

from ..models import AgentSession, ActiveAgentsPerHour
from django.db import connection


def json_to_db(json_file_path):
    with open(json_file_path) as json_file:
        data = json.load(json_file)

        session_list = [
            AgentSession(
                agentId=json_entry["contact"]["id"],
                callStartTime=json_entry["callStartTime"],
                callEndTime=json_entry["callEndTime"],
            )
            for json_entry in data
        ]

        AgentSession.objects.bulk_create(session_list)


def create_active_agent_table():
    query = "SELECT * FROM graph_agentsession"
    cursor = connection.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()
    expanded_time_data = []

    for row in rows:
        start_time = datetime(row[3].year, row[3].month, row[3].day, row[3].hour)
        end_time = datetime(row[2].year, row[2].month, row[2].day, row[2].hour)

        while start_time <= end_time:
            expanded_time_data.append([row[1], start_time])
            start_time += timedelta(hours=1)

    df_data = pd.DataFrame(expanded_time_data, columns=["Agent_Id", "Time"])
    df_active_agents_per_hour = df_data.groupby(['Time']).nunique()

    active_agents_per_hour_list = [
        ActiveAgentsPerHour(
            time=row[0].to_pydatetime(),
            count=row[1],
        )
        for row in df_active_agents_per_hour.itertuples()
    ]

    ActiveAgentsPerHour.objects.bulk_create(active_agents_per_hour_list)

    print("Done writing active agent table")

