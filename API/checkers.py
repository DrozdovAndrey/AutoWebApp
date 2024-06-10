import logging

import yaml
from zeep import Client, Settings

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def check_text(text):
    settings = Settings(strict=False)
    client = Client(data['wsdl'], settings=settings)
    if not client:
        logging.error('Cant init client')
        return None
    try:
        response = client.service.checkText(text)[0]['s']
    except:
        logging.exception('Exception while get response')
        return None
    logging.info(f'Get response {response}')
    return response

