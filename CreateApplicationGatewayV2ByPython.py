#
from azure.mgmt.network import NetworkManagementClient

from azure.identity import ClientSecretCredential
from azure.identity import DefaultAzureCredential
from azure.identity import AzureAuthorityHosts

from azure.mgmt.resource import ResourceManagementClient
from msrestazure.azure_cloud import AZURE_CHINA_CLOUD

# AZURE_TENANT_ID: with your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: with your Azure Active Directory Application Client ID
# AZURE_CLIENT_SECRET: with your Azure Active Directory Application Secret
# AZURE_SUBSCRIPTION_ID: with your Azure Subscription Id
AZURE_TENANT_ID = "xxxxxxxxxxxx"
AZURE_CLIENT_ID = "f0489ca4-21f8-4d73-a91a-6f6735cf1b55"
AZURE_CLIENT_SECRET = "xxxxxxxxxxx."
AZURE_SUBSCRIPTION_ID = "c1fe03e6-ff80-4d91-824d-ba495a000792"

# "kkVk42P5rdkItzjdle8NVjE~0x8__s8B9."
# "8ab2b4ae-0eee-4ef8-b5c2-b5d2e7c78ef9"
credential = ClientSecretCredential(
    authority=AZURE_CHINA_CLOUD.endpoints.active_directory,
    tenant_id=AZURE_TENANT_ID,
    client_id=AZURE_CLIENT_ID,
    client_secret=AZURE_CLIENT_SECRET
)

nmclient = NetworkManagementClient(credential,
                                   AZURE_SUBSCRIPTION_ID,
                                   base_url=AZURE_CHINA_CLOUD.endpoints.resource_manager,
                                   credential_scopes=[AZURE_CHINA_CLOUD.endpoints.resource_manager + "/.default"]
                                   )

app_gw = nmclient.application_gateways.get("cn3rg", "cn3gwtest")
print(app_gw)
print("===========================================")
'''
# Create Application Gateway V2
# 
print('Create Application Gateway Standard V2')
GROUP_NAME = "cn3rg"
APPLICATION_GATEWAY_NAME = "createbypy"
SUBNET_ID = "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/virtualNetworks/CN3-Vnet/subnets/appgwsubnet02".format(
    AZURE_SUBSCRIPTION_ID, GROUP_NAME)
PUBLICIP_ID = "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/publicIPAddresses/pyappgwIP".format(
    AZURE_SUBSCRIPTION_ID, GROUP_NAME)
appgateway_id = "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/applicationGateways/{}".format(
    AZURE_SUBSCRIPTION_ID, GROUP_NAME, APPLICATION_GATEWAY_NAME)
LOCATION = "ChinaNorth3"
appgateway_frontip_name = "appGatewayFrontendIP"
appgateway_frontport_name = "appGatewayFrontendPort"
appgateway_http_listener_name = "appGatewayHttpListener"
appgateway_backend_pool_name = "appGatewayBackendPool"
appgateway_httpsettings_name = "appGatewayBackendHttpSettings"
async_ag_creation = nmclient.application_gateways.begin_create_or_update(
    GROUP_NAME,
    APPLICATION_GATEWAY_NAME,
    {
        'location': LOCATION,
        "autoscaleConfiguration": {
            "maxCapacity": 2,
            "minCapacity": 0
        },
        "sku": {
            "family": "Generation_1",
            "name": "Standard_v2",
            "tier": "Standard_v2"
        },
        "gateway_ip_configurations": [{
            "name": "appGatewayIpConfig",
            "subnet": {
                "id": SUBNET_ID
            }
        }],
        "frontend_ip_configurations": [{
            "name": appgateway_frontip_name,
            "publicIPAddress": {
                "id": PUBLICIP_ID
            }
        }],
        "frontend_ports": [{
            "name": appgateway_frontport_name,
            "port": 80
        }],
        "backend_address_pools": [{
            "name": appgateway_backend_pool_name,
            "backend_addresses": [{
                "ip_address": "10.0.0.4"
            }, {
                "ip_address": "10.0.0.5"
            }]
        }],
        "backend_http_settings_collection": [{
            "name": appgateway_httpsettings_name,
            "port": 80,
            "protocol": "Http",
            "cookie_based_affinity": "Enabled"
        }],
        "http_listeners": [{
            "name": appgateway_http_listener_name,
            "frontend_ip_configuration": {
                "id": appgateway_id + "/frontendIPConfigurations/" + appgateway_frontip_name
            },
            "frontend_port": {
                "id": appgateway_id + '/frontendPorts/' + appgateway_frontport_name
            },
            "protocol": "Http",
            "ssl_certificate": None
        }],
        "request_routing_rules": [{
            "name": "rule1",
            "rule_type": "Basic",
            "priority": 20,
            "http_listener": {
                "id": appgateway_id + '/httpListeners/' + appgateway_http_listener_name
            },
            "backend_address_pool": {
                "id": appgateway_id + '/backendAddressPools/' + appgateway_backend_pool_name
            },
            "backend_http_settings": {
                "id": appgateway_id + '/backendHttpSettingsCollection/' + appgateway_httpsettings_name
            }
        }]
    }
)
application_gateway = async_ag_creation.result()
print(application_gateway)

# Delete Resource group and everything in it

print("\n\n")
'''
