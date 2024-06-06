import requests


class TestRestApi:

    def get_sites(self, lat, long, radius, limit=100):
        session = requests.Session()
        URL = 'https://en.wikipedia.org/w/api.php'
        params = {
            "format": "json",
            "list": "geosearch",
            "gscoord": f"{lat}|{long}",
            "gslimit": f"{limit}",
            "gsradius": f"{radius}",
            "action": "query"
        }
        request = session.get(url=URL, params=params)
        pages = request.json()['query']['geosearch']
        sites = [i['title'] for i in pages]
        return sites

    def test_step1(self, lat, long, radius, text):
        assert text in self.get_sites(lat, long, radius)


class TestSoapApi:
    def zeep_init(self):
        wsdl = 'http://dss.cryptopro.ru/verify/service.svc?wsdl'
        sign = """
        """