"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('google-dorking')


class GoogleDorking(object):
    def __init__(self, config, *args, **kwargs):
        self.api_key = config.get('api_key')
        url = config.get('server_url').strip('/')
        if not url.startswith('https://') and not url.startswith('http://'):
            self.url = 'https://{0}/customsearch/v1'.format(url)
        else:
            self.url = url + '/customsearch/v1'
        self.verify_ssl = config.get('verify_ssl')

    def make_rest_call(self, url, method, data=None, params=None):
        try:
            url = self.url + url + '?key={0}'.format(self.api_key)
            headers = {
                'Content-Type': 'application/json'
            }
            logger.debug("Endpoint {0}".format(url))
            response = requests.request(method, url, data=data, params=params, headers=headers, verify=self.verify_ssl)
            logger.debug("response_content {0}:{1}".format(response.status_code, response.content))
            if response.ok or response.status_code == 204:
                logger.info('Successfully got response for url {0}'.format(url))
                if 'json' in str(response.headers):
                    return response.json()
                else:
                    return response
            elif response.status_code == 404:
                return response
            else:
                logger.error("{0}".format(response.status_code))
                raise ConnectorError("{0}:{1}".format(response.status_code, response.text))
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError(
                'The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid Credentials')
        except Exception as err:
            raise ConnectorError(str(err))


def custom_search(config, params):
    try:
        gd = GoogleDorking(config)
        endpoint = ''
        additional_fields = params.pop('additional_fields')
        if additional_fields:
            params.update(additional_fields)
        query_params = {k: v for k, v in params.items() if v is not None and v != ''}
        response = gd.make_rest_call(endpoint, 'GET', params=query_params)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def check_health(config):
    try:
        response = custom_search(config, params={'cx': '017576662512468239146:omuauf_lfve', 'q': 'lectures', 'num': 1})
        if response:
            return True
    except Exception as err:
        logger.info(str(err))
        raise ConnectorError(str(err))


operations = {
    'custom_search': custom_search
}
