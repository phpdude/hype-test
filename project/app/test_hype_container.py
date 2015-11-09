# -*- coding: utf-8 -*-

"""Tests app app
A different sequencer is used for each test as the readings are not idempotent.
"""

import pytest

import app
from model import db
import json
from threading import Thread

@pytest.fixture
def client(request):
    test_client = app.app.test_client()
    db.execute("TRUNCATE TABLE lbs2.location CASCADE")
    db.execute("TRUNCATE TABLE lbs2.object2user CASCADE")
    db.execute("TRUNCATE TABLE lbs2.objects CASCADE")
    db.execute("TRUNCATE TABLE lbs2.settings CASCADE")
    db.execute("TRUNCATE TABLE lbs2.providers CASCADE")
    db.execute("TRUNCATE TABLE lbs2.users CASCADE")
    db.commit()
    return test_client


def test_create_users(client):
    
    for i in range(0,10):
        user = {
            "login": "user" + str(i),
            "password": "pass" + str(i),
            "name": "user" + str(i)
        }
        set_response = client.post("/users",
                                   data=json.dumps(user),
                                   headers={"content-type":"application/json"})
                                   
        resp = client.get("/users/"+json.loads(set_response.data)["nid"])
        name =  json.loads(resp.data)['name']
        assert(name == "user" + str(i))
        

def test_create_providers(client):
    
    for i in range(0,2):
        prov = {
            "name": "provider" + str(i)
        }
        set_response = client.post("/providers",
                                   data=json.dumps(prov),
                                   headers={"content-type":"application/json"})
        resp = client.get("/providers/"+json.loads(set_response.data)["nid"])
        name =  json.loads(resp.data)['name']
        assert(name == "provider" + str(i))
        
def test_create_objects(client):
    
    for i in range(20,23):
        user = {
            "login": "user-a" + str(i),
            "password": "pass-a" + str(i),
            "name": "user-a" + str(i)
        }
        user_resp = client.post("/users",
                                   data=json.dumps(user),
                                   headers={"content-type":"application/json"})
        
        user_id = json.loads(user_resp.data)["nid"]
        
        prov = {
            "name": "provider" + str(i)
        }
        prov_resp = client.post("/providers",
                                   data=json.dumps(prov),
                                   headers={"content-type":"application/json"})
        
        prov_id = json.loads(prov_resp.data)["nid"]
        
        for v in range(0,3):
            vehicle = {
                "name": "vehicle" + str(i) + str(v),
                "provider_id": prov_id,
                "active": True,
                "users1" : user_id
                
            }
            veh_resp = client.post("/vehicles",
                                       data=json.dumps(vehicle),
                                       headers={"content-type":"application/json"})

            veh_get_resp = client.get("/vehicles/"+json.loads(veh_resp.data)["nid"])
            name =  json.loads(veh_get_resp.data)['name']
            assert(name == "vehicle" + str(i) + str(v))





