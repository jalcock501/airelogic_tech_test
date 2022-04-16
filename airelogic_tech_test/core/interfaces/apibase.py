""" API BASE CLASS FILE """
from urllib.parse import urljoin

import requests
import urllib3

from core.interfaces.cli import style
from core.tools.logger import Logger

# disable insecure warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
"""_summary_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
# pylint: disable=R0903
# pylint: disable=W0102

logger = Logger()


class ApiBaseClass:
    """ Base Class for Api's """

    def __init__(self, url, apikey=""):
        self.url = url
        self.apikey = apikey

    def action(self, action, method, data={}):
        """ Generic method for hitting api endpoints """
        response = None

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        if self.apikey:
            headers['Authorization'] = self.apikey

        for key, value in headers.items():
            logger.debug("{}: {}".format(key, "X"*len(value)))

        url = urljoin(self.url, action)

        response = requests.request(
            method,
            url,
            json=data,
            verify=False,
            headers=headers
        )

        return response

    def return_model(self, model):
        """ 
        Returns data model from api call
        I would usually add proper exception handling of failed http requests
        but for purposed of test and personal time "something went wrong!" will have to do
         """
        if self.resp.status_code != 200:
            return False, f"Something went wrong! {style(self.resp.status_code)}"
        else:
            return True, model.parse_obj(self.resp.json())
