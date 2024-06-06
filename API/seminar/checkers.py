import yaml
from zeep import Client, Settings

with open('config.yaml') as f:
    data = yaml.safe_load(f)
wsdl = data['wsdl']


def check_text(text):
    settings = Settings(strict=False)
    client = Client(wsdl, settings=settings)
    response = client.service.checkText(text)
    return response[0]['s']

