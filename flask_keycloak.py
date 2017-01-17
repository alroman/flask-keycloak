import requests
from flask import current_app

"""
    Keycloak API/add user
    
    Requires: http://docs.python-requests.org/en/master/
    
"""
class KeyCloak(object):
    
    def __init__(self, config):
        self.config = config
        
    def add_user(self, user):
        
        url = "/admin/realms/{0}/users".format(self.config['keycloak_realm'])
        payload = self._user_obj(user)
        headers = {'Authorization': 'bearer ' + self._get_token()}
        response = requests.post(config['keycloak_api'] + url, data=payload, headers=headers)
        # Degbug
        print(response)
        
    def _get_token(self):
        url = "realms/master/protocol/openid-connect/token"
        payload = {
            "client_id": "admin-cli", 
            "username", self.config['keycloak_user'], 
            "password": self.config['keycloak_pass'], 
            "grant_type": "password"
        }
        r = requests.post(config['keycloak_api'] + url, data=payload)
        
        body = r.json()
        return body['access_token']
        
    def _user_obj(self, user):
        patient_id = user['patient_id']
        clinician = user['clinician']
        
        # Create unique KC username w/ known password 
        name = _username_from_params(patiend_id, clinician)
        
        user = {
            "username": name,
            "email": name + "." + clinician,
            "firstName": patient_id,
            "lastName": clinician
        }
        
        return user
        
    def _username_from_params(self, id, email):
        # @todo: need scheme to create unique usernames
        pass
        
    