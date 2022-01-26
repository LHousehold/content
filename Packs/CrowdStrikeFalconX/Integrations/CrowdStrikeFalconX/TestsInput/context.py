from CommonServerPython import DemistoException

SEND_UPLOADED_FILE_TO_SENDBOX_ANALYSIS_CONTEXT = {
    'submitted_id': 'id',
    'state': 'created',
    'created_timestamp': '2020-05-12T15:34:11Z',
    'environment_id': 160,
    'sha256': 'sha256'
}

SEND_URL_TO_SANDBOX_ANALYSIS_CONTEXT = [{
    'submitted_id': 'id',
    'state': 'created',
    'created_timestamp': '2020-05-12T16:40:52Z',
    'environment_id': 160
}]

GET_REPORT_SUMMARY_CONTEXT = {
    'csfalconx.resource(val.id === obj.id)':
        [{
            'id': 'id',
            'verdict': 'no specific threat',
            'created_timestamp': '2020-03-16T17:04:48Z',
            'ioc_report_strict_csv_artifact_id': 'ioc_report_strict_csv_artifact_id',
            'ioc_report_broad_csv_artifact_id': 'ioc_report_broad_csv_artifact_id',
            'ioc_report_strict_json_artifact_id': 'ioc_report_strict_json_artifact_id',
            'ioc_report_broad_json_artifact_id': 'ioc_report_broad_json_artifact_id',
            'ioc_report_strict_stix_artifact_id': 'ioc_report_strict_stix_artifact_id',
            'ioc_report_broad_stix_artifact_id': 'ioc_report_broad_stix_artifact_id',
            'ioc_report_strict_maec_artifact_id': 'ioc_report_strict_maec_artifact_id',
            'ioc_report_broad_maec_artifact_id': 'ioc_report_broad_maec_artifact_id',
            'environment_id': 160,
            'environment_description': 'Windows 10 64 bit',
            'threat_score': 13,
            'submit_url': 'hxxps://www.google.com',
            'submission_type': 'page_url',
            'sha256': 'sha256'
        }]
}

GET_ANALYSIS_STATUS_CONTEXT = {
    'csfalconx.resource(val.id === obj.id)':
        [{
            'id': 'id',
            'state': 'success',
            'created_timestamp': '2020-03-16T17:04:48Z',
            'environment_id': 160
        }]
}

CHECK_QUOTA_STATUS_CONTEXT = {
    'csfalconx.resource(val.id === obj.id)':
        [{
            'total': 100,
            'used': 47,
            'in_progress': 2
        }]
}

FIND_SANDBOX_REPORTS_CONTEXT = {
    'csfalconx.resource(val.id === obj.id)':
        [{
            'resources': ['resources1', 'resources2', 'resources3', 'resources4']
        }]
}

FIND_SUBMISSION_ID_CONTEXT = {
    'csfalconx.resource(val.id === obj.id)':
        [{
            'resources': ['resources1', 'resources2', 'resources3', 'resources4']
        }]
}

GET_FULL_REPORT_CONTEXT = [{'architecture': 'WINDOWS',
                            'classification': ['91.6% (.URL) Windows URL shortcut',
                                               '8.3% (.INI) Generic INI configuration'],
                            'contacted_hosts': [{'address': '111.27.12.67',
                                                 'associated_runtime': [{'name': 'name.exe', 'pid': 6428},
                                                                        {'name': 'name.exe',
                                                                         'pid': 9372}],
                                                 'country': 'United States',
                                                 'port': 443,
                                                 'protocol': 'TCP'},
                                                {'address': '111.27.12.67',
                                                 'associated_runtime': [{'name': 'name.exe', 'pid': 6428},
                                                                        {'name': 'name.exe',
                                                                         'pid': 9372}],
                                                 'country': 'United States',
                                                 'port': 80,
                                                 'protocol': 'TCP'},
                                                {'address': '111.27.12.67',
                                                 'associated_runtime': [{'name': 'name.exe',
                                                                         'pid': 6428}],
                                                 'country': 'United States',
                                                 'port': 443,
                                                 'protocol': 'TCP'},
                                                {'address': '111.27.12.67',
                                                 'associated_runtime': [{'name': 'name.exe',
                                                                         'pid': 6428}],
                                                 'country': 'United States',
                                                 'port': 443,
                                                 'protocol': 'TCP'},
                                                {'address': '111.27.12.67',
                                                 'associated_runtime': [{'name': 'name.exe',
                                                                         'pid': 6428}],
                                                 'country': 'United States',
                                                 'port': 443,
                                                 'protocol': 'TCP'},
                                                {'address': '111.27.12.67',
                                                 'associated_runtime': [{'name': 'name.exe',
                                                                         'pid': 6428}],
                                                 'country': 'United States',
                                                 'port': 443,
                                                 'protocol': 'TCP'},
                                                {'address': '111.27.12.67',
                                                 'associated_runtime': [{'name': 'name.exe',
                                                                         'pid': 6428}],
                                                 'country': 'United States',
                                                 'port': 443,
                                                 'protocol': 'TCP'}],
                            'created_timestamp': '2020-03-16T17:04:48Z',
                            'dns_requests': [{'address': '111.111.1.1',
                                              'country': 'United States',
                                              'domain': 'googleads.g.doubleclick.net',
                                              'registrar_creation_timestamp': '1996-01-16T00:00:00+00:00',
                                              'registrar_name': 'registrar_name',
                                              'registrar_organization': 'registrar_organization'},
                                             {'address': '172.217.7.163',
                                              'country': 'United States',
                                              'domain': 'domain'},
                                             {'address': '111.27.12.67',
                                              'country': 'United States',
                                              'domain': 'ssl.gstatic.com',
                                              'registrar_creation_timestamp': '2008-02-11T00:00:00+00:00',
                                              'registrar_name': 'registrar_name',
                                              'registrar_organization': 'Google Inc.'},
                                             {'address': '172.217.14.163',
                                              'country': 'United States',
                                              'domain': 'www.gstatic.com',
                                              'registrar_creation_timestamp': '2008-02-11T00:00:00+00:00',
                                              'registrar_name': 'registrar_name',
                                              'registrar_organization': 'registrar_organization'}],
                            'environment_description': 'Windows 10 64 bit',
                            'environment_id': 160,
                            'id': 'id',
                            'incidents': [{'details': ['Contacts 4 domains and 4 hosts'],
                                           'name': 'Network Behavior'}],
                            'ioc_report_broad_csv_artifact_id': 'ioc_report_broad_csv_artifact_id',
                            'ioc_report_broad_json_artifact_id': 'ioc_report_broad_json_artifact_id',
                            'ioc_report_broad_maec_artifact_id': 'ioc_report_broad_maec_artifact_id',
                            'ioc_report_broad_stix_artifact_id': 'ioc_report_broad_stix_artifact_id',
                            'ioc_report_strict_csv_artifact_id': 'ioc_report_strict_csv_artifact_id',
                            'ioc_report_strict_json_artifact_id': 'ioc_report_strict_json_artifact_id',
                            'ioc_report_strict_maec_artifact_id': 'ioc_report_strict_maec_artifact_id',
                            'ioc_report_strict_stix_artifact_id': 'ioc_report_strict_stix_artifact_id',
                            'processes': [{'command_line': 'command_line',
                                           'icon_artifact_id': 'icon_artifact_id',
                                           'name': 'rundll32.exe',
                                           'normalized_path': 'normalized_path.exe',
                                           'pid': 6648,
                                           'process_flags': [{'name': 'Reduced Monitoring'}],
                                           'sha256': 'sha256',
                                           'uid': '00074182-00006648'}],
                            'screenshots_artifact_ids': ['screenshots_artifact_ids1',
                                                         'screenshots_artifact_ids2',
                                                         'screenshots_artifact_ids3',
                                                         'screenshots_artifact_ids4'],
                            'sha256': 'sha256',
                            'signatures': [{'category': 'General',
                                            'description': 'description',
                                            'identifier': 'network-0',
                                            'name': 'Contacts domains',
                                            'origin': 'Network Traffic',
                                            'relevance': 1,
                                            'threat_level_human': 'informative',
                                            'type': 7},
                                           {'category': 'General',
                                            'description': 'description',
                                            'identifier': 'network-1',
                                            'name': 'Contacts server',
                                            'origin': 'Network Traffic',
                                            'relevance': 1,
                                            'threat_level_human': 'informative',
                                            'type': 7},
                                           {'category': 'Network Related',
                                            'description': 'description',
                                            'identifier': 'string-3',
                                            'name': 'Found potential URL in binary/memory',
                                            'origin': 'String',
                                            'relevance': 10,
                                            'threat_level_human': 'informative',
                                            'type': 2},
                                           {'category': 'External Systems',
                                            'description': 'description',
                                            'identifier': 'suricata-0',
                                            'name': 'Detected Suricata Alert',
                                            'origin': 'Suricata Alerts',
                                            'relevance': 10,
                                            'threat_level_human': 'informative',
                                            'type': 18},
                                           {'category': 'Ransomware/Banking',
                                            'description': 'description',
                                            'identifier': 'string-12',
                                            'name': 'Detected text artifact in screenshot that indicate '
                                                    'file could be ransomware',
                                            'origin': 'String',
                                            'relevance': 10,
                                            'threat_level': 1,
                                            'threat_level_human': 'suspicious',
                                            'type': 2},
                                           {'category': 'Network Related',
                                            'description': 'description',
                                            'identifier': 'network-23',
                                            'name': 'Sends traffic on typical HTTP outbound port, but '
                                                    'without HTTP header',
                                            'origin': 'Network Traffic',
                                            'relevance': 5,
                                            'threat_level': 1,
                                            'threat_level_human': 'suspicious',
                                            'type': 7}],
                            'submission_type': 'page_url',
                            'submit_url': 'hxxps://www.google.com',
                            'threat_score': 13,
                            'verdict': 'no specific threat'}]

MULTIPLE_ERRORS_RESULT = DemistoException(
    '403: access denied, authorization failed\n401: test error #1\n402: test error #2')
