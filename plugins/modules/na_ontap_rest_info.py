#!/usr/bin/python

# (c) 2020, NetApp, Inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

""" NetApp ONTAP Info using REST APIs """

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = '''
module: na_ontap_rest_info
author: NetApp Ansible Team (@carchi8py) <ng-ansibleteam@netapp.com>
extends_documentation_fragment:
    - netapp.ontap.netapp.na_ontap
short_description: NetApp ONTAP information gatherer using REST APIs
description:
    - This module allows you to gather various information about ONTAP configuration using REST APIs
version_added: 20.5.0
notes:
  - I(security_login_role_config_info) there is no REST equivalent.
  - I(security_login_role_info) there is no REST equivalent.
  - I(security_key_manager_key_info) there is no REST equivalent.
  - I(vserver_motd_info) there is no REST equivalent.
  - I(vserver_login_banner_info) there is no REST equivalent.
  - I(vscan_connection_extended_stats_info) there is no REST equivalent.
  - I(env_sensors_info) there is no REST equivalent.
  - I(fcp_adapter_info) there is no REST equivalent.
  - I(net_dev_discovery_info) there is no REST equivalent.
  - I(net_failover_group_info)  there is no REST equivalent.
  - I(net_firewall_info) there is no REST equivalent.
  - I(ntfs_dacl_info) there is no REST equivalent.
  - I(ntfs_sd_info) there is no REST equivalent.
  - I(role_info) there is not REST equivalent.
  - I(subsys_health_info) there is not REST equivalent.
  - I(volume_move_target_aggr_info) there is not REST equivalent.

options:
    state:
        type: str
        description:
            - deprecated as of 21.1.0.
            - this option was ignored and continues to be ignored.
    gather_subset:
        type: list
        elements: str
        description:
            - When supplied, this argument will restrict the information collected to a given subset.
            - Either the info name or the REST API can be given. Possible values for this argument include
            - aggregate_info or storage/aggregates
            - aggr_efficiency_info
            - application_info or application/applications
            - application_template_info or application/templates
            - autosupport_check_info or support/autosupport/check
            - autosupport_config_info or support/autosupport
            - autosupport_messages_history or support/autosupport/messages
            - broadcast_domains_info or net_port_broadcast_domain_info or network/ethernet/broadcast-domains
            - cifs_home_directory_info or protocols/cifs/home-directory/search-paths
            - cifs_services_info or cifs_options_info or protocols/cifs/services
            - cifs_vserver_security_info
            - cifs_share_info or protocols/cifs/shares
            - clock_info
            - cloud_targets_info or cloud/targets
            - cluster_chassis_info or cluster/chassis
            - cluster_log_forwarding_info or security/audit/destinations
            - cluster_identity_info
            - cluster_jobs_info or cluster/jobs
            - cluster_metrics_info or cluster/metrics
            - cluster_metrocluster_diagnostics or metrocluster_check_info or cluster/metrocluster/diagnostics
            - cluster_node_info or sysconfig_info or cluster/nodes
            - cluster_peer_info or cluster/peers
            - cluster_schedules or job_schedule_cron_info or cluster/schedules
            - cluster_software_download or cluster/software/download
            - cluster_software_history or cluster/software/history
            - cluster_software_packages or cluster/software/packages
            - cluster_switch_info or network/ethernet/switches
            - disk_info or storage/disks
            - event_notification_info or support/ems/destinations
            - event_notification_destination_info or support/ems/destinations
            - export_policy_info or protocols/nfs/export-policies
            - file_directory_security or private/cli/vserver/security/file-directory
            - initiator_groups_info or igroup_info or protocols/san/igroups
            - ip_interfaces_info or net_interface_info or network/ip/interfaces
            - ip_routes_info or net_routes_info or network/ip/routes
            - ip_service_policies or net_interface_service_policy_info or network/ip/service-policies
            - kerberos_realm_info or protocols/nfs/kerberos/realms
            - license_info or cluster/licensing/licenses
            - network_ipspaces_info or net_ipspaces_info or network/ipspaces
            - network_ports_info or  net_port_info or network/ethernet/ports
            - net_vlan_info
            - ntp_server_info or cluster/ntp/servers
            - nvme_info or protocols/nvme/services
            - nvme_interface_info or protocols/nvme/interfaces
            - nvme_subsystem_info or protocols/nvme/subsystems
            - metrocluster_info or cluster/metrocluster
            - metrocluster-node-get-iter or cluster/metrocluster/nodes
            - ontap_system_version or  cluster_image_info or cluster/software
            - san_fc_logins_info or network/fc/logins
            - san_fc_wppn-aliases or fcp_alias_info or network/fc/wwpn-aliases
            - san_fcp_services or fcp_service_info or protocols/san/fcp/services
            - san_iscsi_credentials or protocols/san/iscsi/credentials
            - san_iscsi_services or iscsi_service_info or protocols/san/iscsi/services
            - san_lun_maps or lun_map_info or protocols/san/lun-maps
            - security_login_info or security_login_account_info or security/accounts
            - security_login_rest_role_info or security/roles
            - sis_info
            - sis_policy_info or storage/volume-efficiency-policies
            - snapmirror_destination_info
            - snapmirror_info or snapmirror/relationships
            - snapmirror_policy_info or snapmirror/policies
            - storage_bridge_info or storage/bridges
            - storage_flexcaches_info or storage/flexcache/flexcaches
            - storage_flexcaches_origin_info or storage/flexcache/origins
            - storage_luns_info or lun_info or storage/luns
            - storage_NVMe_namespaces or nvme_namespace_info or storage/namespaces
            - storage_ports_info or storage/ports
            - storage_qos_policies or qos_policy_info or qos_adaptive_policy_info or storage/qos/policies
            - storage_qtrees_config or qtree_info or storage/qtrees
            - storage_quota_reports or quota_report_info or storage/quota/reports
            - storage_quota_policy_rules or storage/quota/rules
            - storage_shelves_config or shelf_info or storage/shelves
            - storage_snapshot_policies or snapshot_policy_info or storage/snapshot-policies
            - support_ems_config or support/ems
            - support_ems_events or support/ems/events
            - support_ems_filters or support/ems/filters
            - svm_dns_config_info or net_dns_info or name-services/dns
            - svm_ldap_config_info or ldap_client or ldap_config or name-services/ldap
            - svm_name_mapping_config_info or name-services/name-mappings
            - svm_nis_config_info or name-services/nis
            - svm_peers_info or vserver_peer_info or svm/peers
            - svm_peer-permissions_info or svm/peer-permissions
            - sys_cluster_alerts or private/support/alerts
            - system_node_info
            - vserver_info or svm/svms
            - vserver_nfs_info or nfs_info or protocols/nfs/services
            - volume_info or storage/volumes
            - volume_space_info
            - vscan_connection_status_all_info or protocols/vscan/server-status
            - vscan_status_info or vscan_info or protocols/vscan
            - Can specify a list of values to include a larger subset.
            - REST APIs are supported with ONTAP 9.6 onwards.
        default: "demo"
    max_records:
        type: int
        description:
            - Maximum number of records returned in a single call.
        default: 1024
    fields:
        type: list
        elements: str
        description:
            - Request specific fields from subset.
               '*' to return all the fields, one or more subsets are allowed.
               '<list of fields>'  to return specified fields, only one subset will be allowed.
            - If the option is not present, return default REST subset of Api Fields for that API.
        version_added: '20.6.0'
    parameters:
        description:
        - Allows for any rest option to be passed in
        type: dict
        version_added: '20.7.0'
    use_python_keys:
        description:
        - If true, I(/) in the returned dictionary keys are translated to I(_).
        - It makes it possible to use a . notation when processing the output.
        - For instance I(ontap_info["svm/svms"]) can be accessed as I(ontap_info.svm_svms).
        type: bool
        default: false
        version_added: '21.9.0'
'''

EXAMPLES = '''
- name: run ONTAP gather facts for vserver info
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      validate_certs: false
      use_rest: Always
      gather_subset:
      - vserver_info

- name: run ONTAP gather facts for aggregate info and volume info
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      validate_certs: false
      use_rest: Always
      gather_subset:
      - aggregate_info
      - volume_info

- name: run ONTAP gather facts for all subsets
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      validate_certs: false
      use_rest: Always
      gather_subset:
      - all

- name: run ONTAP gather facts for aggregate info and volume info with fields section
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      fields:
        - '*'
      validate_certs: false
      use_rest: Always
      gather_subset:
        - aggregate_info
        - volume_info

- name: run ONTAP gather facts for aggregate info with specified fields
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      fields:
        - 'uuid'
        - 'name'
        - 'node'
      validate_certs: false
      use_rest: Always
      gather_subset:
        - aggregate_info
      parameters:
        recommend:
          true

- name: run ONTAP gather facts for volume info with query on name and state
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      validate_certs: false
      gather_subset:
        - volume_info
      parameters:
        name: ansible*
        state: online
- name: run ONTAP gather fact to get DACLs
  netapp.ontap.na_ontap_rest_info:
    hostname: "1.2.3.4"
    username: "testuser"
    password: "test-password"
    https: true
    validate_certs: false
    gather_subset:
        - file_directory_security
    parameters:
      vserver: svm1
      path: /vol1/qtree1
    use_python_keys: true
'''

from ansible.module_utils.basic import AnsibleModule
import ansible_collections.netapp.ontap.plugins.module_utils.netapp as netapp_utils
from ansible_collections.netapp.ontap.plugins.module_utils.netapp_module import NetAppModule
from ansible_collections.netapp.ontap.plugins.module_utils.netapp import OntapRestAPI


class NetAppONTAPGatherInfo(object):
    '''Class with gather info methods'''

    def __init__(self):
        """
        Parse arguments, setup state variables,
        check parameters and ensure request module is installed
        """
        self.argument_spec = netapp_utils.na_ontap_host_argument_spec()
        self.argument_spec.update(dict(
            state=dict(type='str', required=False),
            gather_subset=dict(default=['demo'], type='list', elements='str', required=False),
            max_records=dict(type='int', default=1024, required=False),
            fields=dict(type='list', elements='str', required=False),
            parameters=dict(type='dict', required=False),
            use_python_keys=dict(type='bool', default=False),
        ))

        self.module = AnsibleModule(
            argument_spec=self.argument_spec,
            supports_check_mode=True
        )

        # set up variables
        self.na_helper = NetAppModule()
        self.parameters = self.na_helper.set_parameters(self.module.params)
        self.fields = []

        self.rest_api = OntapRestAPI(self.module)

    def validate_ontap_version(self):
        """
            Method to validate the ONTAP version
        """

        api = 'cluster'
        data = {'fields': ['version']}

        ontap_version, error = self.rest_api.get(api, data)

        if error:
            self.module.fail_json(msg=error)

        return ontap_version

    def get_subset_info(self, gather_subset_info, default_fields=None):
        """
            Gather ONTAP information for the given subset using REST APIs
            Input for REST APIs call : (api, data)
            return gathered_ontap_info
        """

        api = gather_subset_info['api_call']
        if gather_subset_info.pop('post', False):
            self.run_post(gather_subset_info)
        if default_fields:
            total_fields = default_fields + ','.join(self.fields)
            data = {'max_records': self.parameters['max_records'], 'fields': total_fields}
        else:
            data = {'max_records': self.parameters['max_records'], 'fields': self.fields}

        #  Delete the fields record from data if it is a private/cli API call.
        #  The private_cli_fields method handles the fields for API calls using the private/cli endpoint.
        if '/private/cli' in api:
            del data['fields']

        # allow for passing in any additional rest api fields
        if self.parameters.get('parameters'):
            for each in self.parameters['parameters']:
                data[each] = self.parameters['parameters'][each]

        gathered_ontap_info, error = self.rest_api.get(api, data)

        if not error:
            return gathered_ontap_info

        # If the API doesn't exist (using an older system), we don't want to fail the task.
        if int(error.get('code', 0)) == 3 or (
           # if Aggr recommender can't make a recommendation, it will fail with the following error code, don't fail the task.
           int(error.get('code', 0)) == 19726344 and "No recommendation can be made for this cluster" in error.get('message')):
            return error.get('message')

        # Fail the module if error occurs from REST APIs call
        if int(error.get('code', 0)) == 6:
            error = "%s user is not authorized to make %s api call" % (self.parameters.get('username'), api)
        self.module.fail_json(msg=error)

    @staticmethod
    def strip_dacls(response):
        # Use 'DACL - ACE' as a marker for the start of the list of DACLS in the descriptor.
        if 'acls' not in response['records'][0]:
            return None
        if 'DACL - ACEs' not in response['records'][0]['acls']:
            return None
        index = response['records'][0]['acls'].index('DACL - ACEs')
        dacls = response['records'][0]['acls'][(index + 1):]

        dacl_list = []
        if dacls:
            for dacl in dacls:
                # The '-' marker is the start of the DACL, the '-0x' marker is the end of the DACL.
                start_hyphen = dacl.index('-') + 1
                first_hyphen_removed = dacl[start_hyphen:]
                end_hyphen = first_hyphen_removed.index('-0x')
                dacl_dict = {'access_type': dacl[:start_hyphen - 1].strip()}
                dacl_dict['user_or_group'] = first_hyphen_removed[:end_hyphen]
                dacl_list.append(dacl_dict)
        return dacl_list

    def run_post(self, gather_subset_info):
        api = gather_subset_info['api_call']
        post_return, error = self.rest_api.post(api, None)
        if error:
            return None
        dummy, error = self.rest_api.wait_on_job(post_return['job'], increment=5)
        if error:
            # TODO: Handle errors that are not errors
            self.module.fail_json(msg="%s" % error)

    def get_next_records(self, api):
        """
            Gather next set of ONTAP information for the specified api
            Input for REST APIs call : (api, data)
            return gather_subset_info
        """

        data = {}
        gather_subset_info, error = self.rest_api.get(api, data)

        if error:
            self.module.fail_json(msg=error)

        return gather_subset_info

    def private_cli_fields(self, api):
        '''
        The private cli endpoint does not allow '*' to be an entered.
        If fields='*' or fields are not included within the playbook, the API call will be populated to return all possible fields.
        If fields is entered into the playbook the fields entered will be parsed into the API.
        '''
        if api == 'support/autosupport/check':
            if 'fields' not in self.parameters or '*' in self.parameters['fields']:
                fields = '?fields=node,corrective-action,status,error-detail,check-type,check-category'
            else:
                fields = '?fields=' + ','.join(self.parameters.get('fields'))

        if api == 'private/cli/vserver/security/file-directory':
            fields = '?fields=acls'

        return str(fields)

    def convert_subsets(self):
        """
        Convert an info to the REST API
        """
        info_to_rest_mapping = {
            "aggregate_info": "storage/aggregates",
            "aggr_efficiency_info": ['storage/aggregates', 'space.efficiency,name,node'],
            "application_info": "application/applications",
            "application_template_info": "application/templates",
            "autosupport_check_info": "support/autosupport/check",
            "autosupport_config_info": "support/autosupport",
            "autosupport_messages_history": "support/autosupport/messages",
            "broadcast_domains_info": "network/ethernet/broadcast-domains",
            "cifs_home_directory_info": "protocols/cifs/home-directory/search-paths",
            "cifs_options_info": "protocols/cifs/services",
            "cifs_services_info": "protocols/cifs/services",
            "cifs_share_info": "protocols/cifs/shares",
            "cifs_vserver_security_info": ["protocols/cifs/services", "security.encrypt_dc_connection,"
                                                                      "security.kdc_encryption,security.smb_signing,"
                                                                      "security.smb_encryption,"
                                                                      "security.lm_compatibility_level,svm.name"],
            "clock_info": ["cluster/nodes", "date"],
            "cloud_targets_info": "cloud/targets",
            "cluster_chassis_info": "cluster/chassis",
            "cluster_identity_info": ["cluster", "contact,location,name,uuid"],
            "cluster_image_info": "cluster/software",
            "cluster_jobs_info": "cluster/jobs",
            "cluster_log_forwarding_info": "security/audit/destinations",
            "cluster_metrocluster_diagnostics": "cluster/metrocluster/diagnostics",
            "cluster_metrics_info": "cluster/metrics",
            "cluster_node_info": "cluster/nodes",
            "cluster_peer_info": "cluster/peers",
            "cluster_schedules": "cluster/schedules",
            "cluster_software_download": "cluster/software/download",
            "cluster_software_history": "cluster/software/history",
            "cluster_software_packages": "cluster/software/packages",
            "cluster_switch_info": "network/ethernet/switches",
            "disk_info": "storage/disks",
            "event_notification_info": "support/ems/destinations",
            "event_notification_destination_info": "support/ems/destinations",
            "export_policy_info": "protocols/nfs/export-policies",
            "fcp_alias_info": "network/fc/wwpn-aliases",
            "fcp_service_info": "protocols/san/fcp/services",
            "file_directory_security": "private/cli/vserver/security/file-directory",
            "igroup_info": "protocols/san/igroups",
            "initiator_groups_info": "protocols/san/igroups",
            "ip_interfaces_info": "network/ip/interfaces",
            "ip_routes_info": "network/ip/routes",
            "ip_service_policies": "network/ip/service-policies",
            "iscsi_service_info": "protocols/san/iscsi/services",
            "job_schedule_cron_info": "cluster/schedules",
            "kerberos_realm_info": "protocols/nfs/kerberos/realms",
            "ldap_client": "name-services/ldap",
            "ldap_config": "name-services/ldap",
            "license_info": "cluster/licensing/licenses",
            "lun_info": "storage/luns",
            "lun_map_info": "protocols/san/lun-maps",
            "net_dns_info": "name-services/dns",
            "net_interface_info": "network/ip/interfaces",
            "net_interface_service_policy_info": "network/ip/service-policies",
            "net_port_broadcast_domain_info": "network/ethernet/broadcast-domains",
            "net_port_info": "network/ethernet/ports",
            "net_routes_info": "network/ip/routes",
            "net_ipspaces_info": "network/ipspaces",
            "net_vlan_info": ["network/ethernet/ports", "name,node.name,vlan.base_port,vlan.tag"],
            "network_ipspaces_info": "network/ipspaces",
            "network_ports_info": "network/ethernet/ports",
            "nfs_info": "protocols/nfs/services",
            "ntp_server_info": "cluster/ntp/servers",
            "nvme_info": "protocols/nvme/services",
            "nvme_interface_info": "protocols/nvme/interfaces",
            "nvme_namespace_info": "storage/namespaces",
            "nvme_subsystem_info": "protocols/nvme/subsystems",
            "metrocluster_info": "cluster/metrocluster",
            "metrocluster_node_info": "cluster/metrocluster/nodes",
            "metrocluster_check_info": "cluster/metrocluster/diagnostics",
            "ontap_system_version": "cluster/software",
            "quota_report_info": "storage/quota/reports",
            "qos_policy_info": "storage/qos/policies",
            "qos_adaptive_policy_info": "storage/qos/policies",
            "qtree_info": "storage/qtrees",
            "san_fc_logins_info": "network/fc/logins",
            "san_fc_wppn-aliases": "network/fc/wwpn-aliases",
            "san_fcp_services": "protocols/san/fcp/services",
            "san_iscsi_credentials": "protocols/san/iscsi/credentials",
            "san_iscsi_services": "protocols/san/iscsi/services",
            "san_lun_maps": "protocols/san/lun-maps",
            "security_login_account_info": "security/accounts",
            "security_login_info": "security/accounts",
            "security_login_rest_role_info": "security/roles",
            "shelf_info": "storage/shelves",
            "sis_info": ["storage/volumes", "efficiency.compression,efficiency.cross_volume_dedupe,"
                                            "efficiency.cross_volume_dedupe,efficiency.compaction,"
                                            "efficiency.compression,efficiency.dedupe,efficiency.policy.name,"
                                            "efficiency.schedule,svm.name"],
            "sis_policy_info": "storage/volume-efficiency-policies",
            "snapmirror_destination_info": ["snapmirror/relationships", "destination.path,destination.svm.name,"
                                                                        "destination.svm.uuid,policy.type,uuid,state,"
                                                                        "source.path,source.svm.name,source.svm.uuid,"
                                                                        "transfer.bytes_transferred"],
            "snapmirror_info": "snapmirror/relationships",
            "snapmirror_policy_info": "snapmirror/policies",
            "snapshot_policy_info": "storage/snapshot-policies",
            "storage_bridge_info": "storage/bridges",
            "storage_flexcaches_info": "storage/flexcache/flexcaches",
            "storage_flexcaches_origin_info": "storage/flexcache/origins",
            "storage_luns_info": "storage/luns",
            "storage_NVMe_namespaces": "storage/namespaces",
            "storage_ports_info": "storage/ports",
            "storage_qos_policies": "storage/qos/policies",
            "storage_qtrees_config": "storage/qtrees",
            "storage_quota_reports": "storage/quota/reports",
            "storage_quota_policy_rules": "storage/quota/rules",
            "storage_shelves_config": "storage/shelves",
            "storage_snapshot_policies": "storage/snapshot-policies",
            "support_ems_config": "support/ems",
            "support_ems_events": "support/ems/events",
            "support_ems_filters": "support/ems/filters",
            "svm_dns_config_info": "name-services/dns",
            "svm_ldap_config_info": "name-services/ldap",
            "svm_name_mapping_config_info": "name-services/name-mappings",
            "svm_nis_config_info": "name-services/nis",
            "svm_peers_info": "svm/peers",
            "svm_peer-permissions_info": "svm/peer-permissions",
            "sysconfig_info": "cluster/nodes",
            "system_node_info": ["cluster/nodes", "controller.cpu.firmware_release,controller.failed_fan.count,"
                                                  "controller.failed_fan.message,"
                                                  "controller.failed_power_supply.count,"
                                                  "controller.failed_power_supply.message,"
                                                  "controller.over_temperature,is_all_flash_optimized,"
                                                  "is_all_flash_select_optimized,is_capacity_optimized,state,name,"
                                                  "location,model,nvram.id,owner,serial_number,storage_configuration,"
                                                  "system_id,uptime,uuid,vendor_serial_number,nvram.battery_state,"
                                                  "version,vm.provider_type"],
            "sys_cluster_alerts": "private/support/alerts",
            "vserver_info": "svm/svms",
            "vserver_peer_info": "svm/peers",
            "vserver_nfs_info": "protocols/nfs/services",
            "volume_info": "storage/volumes",
            "volume_space_info": ["storage/volumes", 'space.logical_space.available,space.logical_space.used,'
                                                     'space.logical_space.used_percent,space.snapshot.reserve_size,'
                                                     'space.snapshot.reserve_percent,space.used,name,svm.name'],
            "vscan_connection_status_all_info": "protocols/vscan/server-status",
            "vscan_info": "protocols/vscan",
            "vscan_status_info": "protocols/vscan"
        }
        # Add rest API names as there info version, also make sure we don't add a duplicate
        subsets = []
        for subset in self.parameters['gather_subset']:
            if subset in info_to_rest_mapping:
                if info_to_rest_mapping[subset] not in subsets:
                    subsets.append(info_to_rest_mapping[subset])
            elif subset not in subsets:
                subsets.append(subset)
        return subsets

    def get_ontap_subset_info_all(self, subset, get_ontap_subset_info):
        """ Iteratively get all records for a subset """
        default_fields = None
        if isinstance(subset, list):
            subset, default_fields = subset
        try:
            # Verify whether the supported subset passed
            specified_subset = get_ontap_subset_info[subset]
        except KeyError:
            self.module.fail_json(msg="Specified subset %s is not found, supported subsets are %s" %
                                  (subset, list(get_ontap_subset_info.keys())))
        subset_info = self.get_subset_info(specified_subset, default_fields)

        if subset_info is not None and isinstance(subset_info, dict) and '_links' in subset_info:
            while subset_info['_links'].get('next'):
                # Get all the set of records if next link found in subset_info for the specified subset
                next_api = subset_info['_links']['next']['href']
                gathered_subset_info = self.get_next_records(next_api.replace('/api', ''))

                # Update the subset info for the specified subset
                subset_info['_links'] = gathered_subset_info['_links']
                subset_info['records'].extend(gathered_subset_info['records'])

            # metrocluster doesn't have a records field, so we need to skip this
            if subset_info.get('records') is not None:
                # Getting total number of records
                subset_info['num_records'] = len(subset_info['records'])
        if subset == 'private/cli/vserver/security/file-directory':
            subset_info = self.strip_dacls(subset_info)

        return subset_info

    def apply(self):
        """
        Perform pre-checks, call functions and exit
        """
        # Validating ONTAP version
        self.validate_ontap_version()

        # Defining gather_subset and appropriate api_call
        get_ontap_subset_info = {
            'application/applications': {
                'api_call': 'application/applications',
            },
            'application/templates': {
                'api_call': 'application/templates',
            },
            'cloud/targets': {
                'api_call': 'cloud/targets',
            },
            'cluster': {
                'api_call': 'cluster',
            },
            'cluster/chassis': {
                'api_call': 'cluster/chassis',
            },
            'cluster/jobs': {
                'api_call': 'cluster/jobs',
            },
            'cluster/licensing/licenses': {
                'api_call': 'cluster/licensing/licenses',
            },
            'cluster/metrocluster': {
                'api_call': 'cluster/metrocluster',
            },
            'cluster/metrocluster/diagnostics': {
                'api_call': 'cluster/metrocluster/diagnostics',
                'post': True
            },
            'cluster/metrocluster/nodes': {
                'api_call': 'cluster/metrocluster/nodes',
            },
            'cluster/metrics': {
                'api_call': 'cluster/metrics',
            },
            'cluster/nodes': {
                'api_call': 'cluster/nodes',
            },
            'cluster/ntp/servers': {
                'api_call': 'cluster/ntp/servers',
            },
            'cluster/peers': {
                'api_call': 'cluster/peers',
            },
            'cluster/schedules': {
                'api_call': 'cluster/schedules',
            },
            'cluster/software': {
                'api_call': 'cluster/software',
            },
            'cluster/software/download': {
                'api_call': 'cluster/software/download',
            },
            'cluster/software/history': {
                'api_call': 'cluster/software/history',
            },
            'cluster/software/packages': {
                'api_call': 'cluster/software/packages',
            },
            'name-services/dns': {
                'api_call': 'name-services/dns',
            },
            'name-services/ldap': {
                'api_call': 'name-services/ldap',
            },
            'name-services/name-mappings': {
                'api_call': 'name-services/name-mappings',
            },
            'name-services/nis': {
                'api_call': 'name-services/nis',
            },
            'network/ethernet/broadcast-domains': {
                'api_call': 'network/ethernet/broadcast-domains',
            },
            'network/ethernet/ports': {
                'api_call': 'network/ethernet/ports',
            },
            'network/fc/logins': {
                'api_call': 'network/fc/logins',
            },
            'network/fc/wwpn-aliases': {
                'api_call': 'network/fc/wwpn-aliases',
            },
            'network/ip/interfaces': {
                'api_call': 'network/ip/interfaces',
            },
            'network/ip/routes': {
                'api_call': 'network/ip/routes',
            },
            'network/ip/service-policies': {
                'api_call': 'network/ip/service-policies',
            },
            'network/ipspaces': {
                'api_call': 'network/ipspaces',
            },
            'network/ethernet/switches': {
                'api_call': 'network/ethernet/switches',
            },
            'private/support/alerts': {
                'api_call': 'private/support/alerts',
            },
            'protocols/cifs/home-directory/search-paths': {
                'api_call': 'protocols/cifs/home-directory/search-paths',
            },
            'protocols/cifs/services': {
                'api_call': 'protocols/cifs/services',
            },
            'protocols/cifs/shares': {
                'api_call': 'protocols/cifs/shares',
            },
            'protocols/nfs/export-policies': {
                'api_call': 'protocols/nfs/export-policies',
            },
            'protocols/nfs/kerberos/realms': {
                'api_call': 'protocols/nfs/kerberos/realms',
            },
            'protocols/nfs/services': {
                'api_call': 'protocols/nfs/services',
            },
            'protocols/nvme/interfaces': {
                'api_call': 'protocols/nvme/interfaces',
            },
            'protocols/nvme/services': {
                'api_call': 'protocols/nvme/services',
            },
            'protocols/nvme/subsystems': {
                'api_call': 'protocols/nvme/subsystems',
            },
            'protocols/san/fcp/services': {
                'api_call': 'protocols/san/fcp/services',
            },
            'protocols/san/igroups': {
                'api_call': 'protocols/san/igroups',
            },
            'protocols/san/iscsi/credentials': {
                'api_call': 'protocols/san/iscsi/credentials',
            },
            'protocols/san/iscsi/services': {
                'api_call': 'protocols/san/iscsi/services',
            },
            'protocols/san/lun-maps': {
                'api_call': 'protocols/san/lun-maps',
            },
            'protocols/vscan/server-status': {
                'api_call': 'protocols/vscan/server-status',
            },
            'protocols/vscan': {
                'api_call': 'protocols/vscan',
            },
            'security/accounts': {
                'api_call': 'security/accounts',
            },
            'security/audit/destinations': {
                'api_call': 'security/audit/destinations',
            },
            'security/roles': {
                'api_call': 'security/roles',
            },
            'snapmirror/policies': {
                'api_call': 'snapmirror/policies',
            },
            'snapmirror/relationships': {
                'api_call': 'snapmirror/relationships',
            },
            'storage/aggregates': {
                'api_call': 'storage/aggregates',
            },
            'storage/bridges': {
                'api_call': 'storage/bridges',
            },
            'storage/disks': {
                'api_call': 'storage/disks',
            },
            'storage/flexcache/flexcaches': {
                'api_call': 'storage/flexcache/flexcaches',
            },
            'storage/flexcache/origins': {
                'api_call': 'storage/flexcache/origins',
            },
            'storage/luns': {
                'api_call': 'storage/luns',
            },
            'storage/namespaces': {
                'api_call': 'storage/namespaces',
            },
            'storage/ports': {
                'api_call': 'storage/ports',
            },
            'storage/qos/policies': {
                'api_call': 'storage/qos/policies',
            },
            'storage/qtrees': {
                'api_call': 'storage/qtrees',
            },
            'storage/quota/reports': {
                'api_call': 'storage/quota/reports',
            },
            'storage/quota/rules': {
                'api_call': 'storage/quota/rules',
            },
            'storage/shelves': {
                'api_call': 'storage/shelves',
            },
            'storage/snapshot-policies': {
                'api_call': 'storage/snapshot-policies',
            },
            'storage/volumes': {
                'api_call': 'storage/volumes',
            },
            'storage/volume-efficiency-policies': {
                'api_call': 'storage/volume-efficiency-policies',
            },
            'support/autosupport': {
                'api_call': 'support/autosupport',
            },
            'support/autosupport/check': {
                'api_call': '/private/cli/system/node/autosupport/check/details' + self.private_cli_fields('support/autosupport/check'),
            },
            'support/autosupport/messages': {
                'api_call': 'support/autosupport/messages',
            },
            'support/ems': {
                'api_call': 'support/ems',
            },
            'support/ems/destinations': {
                'api_call': 'support/ems/destinations',
            },
            'support/ems/events': {
                'api_call': 'support/ems/events',
            },
            'support/ems/filters': {
                'api_call': 'support/ems/filters',
            },
            'svm/peers': {
                'api_call': 'svm/peers',
            },
            'svm/peer-permissions': {
                'api_call': 'svm/peer-permissions',
            },
            'svm/svms': {
                'api_call': 'svm/svms',
            }
        }
        if 'gather_subset' in self.parameters and (
                'private/cli/vserver/security/file-directory' in self.parameters['gather_subset']
                or 'file_directory_security' in self.parameters['gather_subset']
        ):
            get_ontap_subset_info['private/cli/vserver/security/file-directory'] = {
                'api_call': 'private/cli/vserver/security/file-directory' + self.private_cli_fields('private/cli/vserver/security/file-directory')}

        if 'all' in self.parameters['gather_subset']:
            # If all in subset list, get the information of all subsets
            self.parameters['gather_subset'] = sorted(get_ontap_subset_info.keys())
        if 'demo' in self.parameters['gather_subset']:
            self.parameters['gather_subset'] = ['cluster/software', 'svm/svms', 'cluster/nodes']

        length_of_subsets = len(self.parameters['gather_subset'])

        if self.parameters.get('fields') is not None:
            # If multiple fields specified to return, convert list to string
            self.fields = ','.join(self.parameters.get('fields'))

            if self.fields != '*' and length_of_subsets > 1:
                # Restrict gather subsets to one subset if fields section is list_of_fields
                self.module.fail_json(msg="Error: fields: %s, only one subset will be allowed." % self.parameters.get('fields'))
        converted_subsets = self.convert_subsets()

        result_message = {}
        for subset in converted_subsets:
            result_message[subset] = self.get_ontap_subset_info_all(subset, get_ontap_subset_info)

        results = {'changed': False}
        if self.parameters.get('state') is not None:
            results['state'] = self.parameters['state']
            results['warnings'] = "option 'state' is deprecated."
        if self.parameters['use_python_keys']:
            new_dict = dict((key.replace('/', '_'), value) for (key, value) in result_message.items())
            result_message = new_dict
        self.module.exit_json(ontap_info=result_message, **results)


def main():
    """
    Main function
    """
    obj = NetAppONTAPGatherInfo()
    obj.apply()


if __name__ == '__main__':
    main()
