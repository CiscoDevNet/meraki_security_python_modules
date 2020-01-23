merakiapikey = "<api key>"
merakiorg = "<org id>"
merakiurl = "api.meraki.com/api/v0"
security_posture = {
  "vlan_enabled": {
    "enabled": True
    },
  "vlans" : [
      {
        "id": 2,
        "name": "VLAN2",
        "applianceIp": "192.168.2.1",
        "subnet": "192.168.2.0/24",
        "fixedIpAssignments": {},
        "reservedIpRanges": [],
        "dnsNameservers": "upstream_dns",
        "dhcpHandling": "Run a DHCP server",
        "dhcpLeaseTime": "1 day",
        "dhcpBootOptionsEnabled": False,
        "dhcpOptions": []
    },
    {
        "id": 3,
        "name": "VLAN2",
        "applianceIp": "192.168.3.1",
        "subnet": "192.168.3.0/24",
        "fixedIpAssignments": {},
        "reservedIpRanges": [],
        "dnsNameservers": "upstream_dns",
        "dhcpHandling": "Run a DHCP server",
        "dhcpLeaseTime": "1 day",
        "dhcpBootOptionsEnabled": False,
        "dhcpOptions": []
    }
  ],
  "content_filtering" : {
    "allowedUrlPatterns": [
      "http://www.example.org",
      "http://help.com.au"
    ],
    "blockedUrlPatterns": [
      "http://www.example.com",
      "http://www.betting.com"
    ],
    "blockedUrlCategories": [
      "meraki:contentFiltering/category/1"
    ],
    "urlCategoryListSize": "topSites"
  },
  "malware_settings":{
    "mode": "enabled",
    "allowedUrls": [
      {
        "url": "example.org",
        "comment": "allow example.org"
      },
      {
        "url": "help.com.au",
        "comment": "allow help.com.au"
      }
    ],
    "allowedFiles": [
      {
        "sha256": "e82c5f7d75004727e1f3b94426b9a11c8bc4c312a9170ac9a73abace40aef503",
        "comment": "allow ZIP file"
      }
    ]
  },
  "fire_walled_services":{
      "service": "ICMP",
      "access": "restricted",
      "allowedIps": [
          "123.123.123.1"
      ]
  },
  "l7_firewall_rules":{
      "rules": [
          {
              "policy": "deny",
              "type": "application",
              "value": {
                  "id": "meraki:layer7/application/67",
                  "name": "Xbox LIVE"
              }
          },
          {
              "policy": "deny",
              "type": "applicationCategory",
              "value": {
                  "id": "meraki:layer7/category/2",
                  "name": "Blogging"
              }
          },
          {
              "policy": "deny",
              "type": "host",
              "value": "google.com"
          },
          {
              "policy": "deny",
              "type": "port",
              "value": "23"
          },
          {
              "policy": "deny",
              "type": "ipRange",
              "value": "10.11.12.00/24"
          },
          {
              "policy": "deny",
              "type": "ipRange",
              "value": "10.11.12.00/24:5555"
          },
          {
              "policy": "deny",
              "type": "blacklistedCountries",
              "value": [
                  "AX",
                  "CA"
              ]
          },
          {
              "policy": "deny",
              "type": "whitelistedCountries",
              "value": [
                  "US"
              ]
          }
      ]
  },
  "l3_firewall_rules":{
    "rules": [
      {
        "comment": "Allow TCP traffic to subnet with HTTP servers.",
        "policy": "allow",
        "protocol": "tcp",
        "destPort": 443,
        "destCidr": "192.168.1.0/24",
        "srcPort": "Any",
        "srcCidr": "Any",
        "syslogEnabled": False
      }
    ]
  },
  "group_policies":[
    {
      "name": "No video streaming",
      "scheduling": {
        "enabled": True,
        "monday": {
          "active": True,
          "from": "9:00",
          "to": "17:00"
        },
        "tuesday": {
          "active": True,
          "from": "9:00",
          "to": "17:00"
        },
        "wednesday": {
          "active": True,
          "from": "9:00",
          "to": "17:00"
        },
        "thursday": {
          "active": True,
          "from": "9:00",
          "to": "17:00"
        },
        "friday": {
          "active": True,
          "from": "9:00",
          "to": "17:00"
        },
        "saturday": {
          "active": False,
          "from": "0:00",
          "to": "24:00"
        },
        "sunday": {
          "active": False,
          "from": "0:00",
          "to": "24:00"
        }
      },
      "bandwidth": {
        "settings": "custom",
        "bandwidthLimits": {
          "limitUp": 1000000,
          "limitDown": 1000000
        }
      },
      "firewallAndTrafficShaping": {
        "settings": "custom",
        "trafficShapingRules": [
          {
            "definitions": [
              {
                "type": "host",
                "value": "google.com"
              },
              {
                "type": "port",
                "value": "9090"
              },
              {
                "type": "ipRange",
                "value": "192.1.0.0"
              },
              {
                "type": "ipRange",
                "value": "192.1.0.0/16"
              },
              {
                "type": "ipRange",
                "value": "10.1.0.0/16:80"
              },
              {
                "type": "localNet",
                "value": "192.168.0.0/16"
              },
              {
                "type": "applicationCategory",
                "value": {
                  "id": "meraki:layer7/category/2",
                  "name": "Blogging"
                }
              },
              {
                "type": "application",
                "value": {
                  "id": "meraki:layer7/application/133",
                  "name": "Battle.net"
                }
              }
            ],
            "perClientBandwidthLimits": {
              "settings": "custom",
              "bandwidthLimits": {
                "limitUp": 1000000,
                "limitDown": 1000000
              }
            },
            "dscpTagValue": None,
            "pcpTagValue": None
          }
        ],
        "l3FirewallRules": [
          {
            "comment": "Allow TCP traffic to subnet with HTTP servers.",
            "policy": "allow",
            "protocol": "tcp",
            "destPort": 443,
            "destCidr": "192.168.1.0/24"
          }
        ],
        "l7FirewallRules": [
            {
              "policy": "deny",
              "type": "application",
              "value": {
                "id": "meraki:layer7/application/67",
                "name": "Xbox LIVE"
              }
            },
            {
              "policy": "deny",
              "type": "applicationCategory",
              "value": {
                "id": "meraki:layer7/category/2",
                "name": "Blogging"
              }
            },
            {
              "policy": "deny",
              "type": "host",
              "value": "google.com"
            },
            {
              "policy": "deny",
              "type": "port",
              "value": "23"
            },
            {
              "policy": "deny",
              "type": "ipRange",
              "value": "10.11.12.00/24"
            },
            {
              "policy": "deny",
              "type": "ipRange",
              "value": "10.11.12.00/24:5555"
            }
          ]
      },
      "splashAuthSettings": "bypass",
      "vlanTagging": {
        "settings": "custom",
        "vlanId": "1"
      },
      "bonjourForwarding": {
        "settings": "custom",
        "rules": [
          {
            "description": "A simple bonjour rule",
            "vlanId": "1",
            "services": [
              "All Services"
            ]
          }
        ]
      }
    }
  ],
  "switch_ports":{
    "name": "My switch port",
    "tags": "tag1 tag2",
    "enabled": False
  }
}
