import requests
import json
import random
import sys
import getopt
from pprint import pprint
import meraki_security_config as config

# Configuration values
MERAKI_API_KEY = config.merakiapikey
MERAKI_ORG = config.merakiorg
MERAKI_URL = config.merakiurl
SECURITY_POSTURE = config.security_posture
MERAKI_SESSION = requests.Session()

def enable_vlans(network):
    pprint("Enable VLANS")
    try:
        vlans_enabled = MERAKI_SESSION.put(
            "https://" + MERAKI_URL + "/networks/" + network + "/vlansEnabledState",
            headers={
                "X-Cisco-Meraki-API-Key": MERAKI_API_KEY
            },
            json=SECURITY_POSTURE["vlan_enabled"])
        # Deserialize response text (str) to Python Dictionary object so
        # we can work with it
        vlans_enabled = json.loads(vlans_enabled.text)
        pprint("VLANS_ENABLED: ")
        pprint(vlans_enabled)
    except Exception as e:
        pprint(e)

def create_vlans(network):
    pprint("Create VLANS")
    try:
        for vlan in SECURITY_POSTURE["vlans"]:
            create_vlans = MERAKI_SESSION.post(
                "https://" + MERAKI_URL + "/networks/" + network + "/vlans",
                headers={
                    "X-Cisco-Meraki-API-Key": MERAKI_API_KEY
                },
                json=vlan)
            # Deserialize response text (str) to Python Dictionary object so
            # we can work with it
            create_vlans = json.loads(create_vlans.text)
            pprint("CREATE_VLANS: ")
            pprint(create_vlans)
    except Exception as e:
        pprint(e)

def set_content_filtering(network):
    pprint("Set Content Filtering")
    try:
        set_content_filtering = MERAKI_SESSION.put(
            "https://" + MERAKI_URL + "/networks/" + network + "/contentFiltering",
            headers={
                "X-Cisco-Meraki-API-Key": MERAKI_API_KEY
            },
            json=SECURITY_POSTURE["content_filtering"])
        # Deserialize response text (str) to Python Dictionary object so
        # we can work with it
        set_content_filtering = json.loads(set_content_filtering.text)
        pprint("set_content_filtering: ")
        pprint(set_content_filtering)
    except Exception as e:
        pprint(e)

def set_group_policies(network):
    pprint("Set Group Policies")
    try:
        for policy in SECURITY_POSTURE["group_policies"]:
            set_group_policy = MERAKI_SESSION.post(
                "https://" + MERAKI_URL + "/networks/" + network + "/groupPolicies",
                headers={
                    "X-Cisco-Meraki-API-Key": MERAKI_API_KEY
                },
                json=policy)
            # Deserialize response text (str) to Python Dictionary object so
            # we can work with it
            set_group_policy = json.loads(set_group_policy.text)
            pprint("SET_GROUP_POLICY: ")
            pprint(set_group_policy)
    except Exception as e:
        pprint(e)

def getnetworklist():
    pprint("get networks")
    try:
        # MISSION TODO
        networks = MERAKI_SESSION.get(
            "https://" + MERAKI_URL + "/organizations/" + MERAKI_ORG +"/networks",
            headers={
                "X-Cisco-Meraki-API-Key": MERAKI_API_KEY
            })
        # Deserialize response text (str) to Python Dictionary object so
        # we can work with it
        networks = json.loads(networks.text)
        pprint("Networks: ")
        pprint(networks)
        return networks
    except Exception as e:
        pprint(e)
        return ""
    
    return "No Networks Found"

def apply_security_posture():
    try:
        networks = getnetworklist()
        for network in networks:
            enable_vlans(network["id"])
            create_vlans(network["id"])
            set_content_filtering(network["id"])
            set_group_policies(network["id"])
    except Exception as e:
        pprint(e)



if __name__ == "__main__":
    apply_security_posture()
   
