import json

from ..models import AgentSession


def json_to_db(json_file_path):

    with open(json_file_path) as json_file:
        data = json.load(json_file)
        print(len(data))

        session_list = [
            AgentSession(
                agentId=json_entry["contact"]["id"],
                callStartTime=json_entry["callStartTime"],
                callEndTime=json_entry["callEndTime"],
            )
            for json_entry in data
        ]

        AgentSession.objects.bulk_create(session_list)

        print("done loading data")

