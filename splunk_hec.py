from splunk_http_event_collector import http_event_collector


def getHecConn(token, host, event_type, event_host, port, secure):

    hec = http_event_collector(
        token,
        host,
        event_type,
        event_host,
        port,
        secure)
    hec_reachable = hec.check_connectivity()

    if not hec_reachable:
        return None

    return hec

# Create a payload to send to splunk
# Assign all common parameters and add data specific events later


def initSplunkPayload(
        index="main",
        host="localhost",
        source="raspberry",
        sourcetype="_json"):
    payload = {}
    payload.update({"index": index})
    payload.update({"sourcetype": sourcetype})
    payload.update({"source": source})
    payload.update({"host": host})

    return payload
