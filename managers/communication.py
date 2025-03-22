from utills.summary_builder import summarize_portfolio, summarize_order_event
import json

GCP_IP = "35.223.152.70"
GCP_PORT = 10310
AWS_SERVER = "35.223.152.70"
AWS_PORT = 80

class ComminucationManager:
    def __init__(self, qca):
        self.server_url = get_url(GCP_IP, GCP_PORT)
        # self.SERVER_URL = get_url(AWS_SERVER, AWS_PORT)

        self.qca = qca
        self.debug = qca.debug

    def _get_header(self, order_event=None, portfolio=False):
        header = {}
        header["timestamp"] = self.qca.time.strftime("%Y-%m-%d %H:%M:%S")
        if portfolio:
            header["portfolio"] = json.dumps(summarize_portfolio(self.qca.portfolio))
        if order_event:
            header["order_event"] = json.dumps(summarize_order_event(order_event))
        return header

    def _send_request(self, url, header):
        try:
            response = self.qca.download(url, header)
        except Exception as e:
            raise Exception(f"Error fetching from server: {str(e)}")

        if not response:
            self.debug(f"No response from server. {response}")
            raise Exception("No response from server. {response}")

        return json.loads(response)

    def fetch_order(self):
        path = "/order"
        url = self.server_url + path
        header = self._get_header()

        return self._send_request(url, header)

    def report_order_event(self, order_event):
        path = "/report"
        url = self.server_url + path
        header = self._get_header(order_event=order_event, portfolio=True)

        return self._send_request(url, header)

def get_url(ip, port):
    return f"http://{ip}:{port}"