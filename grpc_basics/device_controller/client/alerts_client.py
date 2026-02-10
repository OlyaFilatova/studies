class AlertsClient:
    def __init__(self, stub):
        self.stub = stub

    def subscribe_alerts(self, device_id):
        for alert in self.stub.SubscribeAlerts(device_id):
            yield alert
