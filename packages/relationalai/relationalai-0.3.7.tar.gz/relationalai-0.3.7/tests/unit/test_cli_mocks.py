from datetime import datetime

sf_profile = {}
sf_profile['platform'] = 'snowflake'
sf_profile['user'] = 'usr'
sf_profile['password'] = 'pwd'
sf_profile['warehouse'] = 'WH'
sf_profile['role'] = 'CONSUMER'
sf_profile['rai_app_name'] = 'APP'
sf_profile['account'] = 'foo-account'

az_profile = {}
az_profile['platform'] = 'azure'
az_profile['client_id'] = 'cl_id'
az_profile['client_secret'] = 'cl_s'
az_profile['client_credentials_url'] = 'https://login.foo.com'
az_profile['host'] = 'azure-latest.relationalai.com'
az_profile['port'] = 443
az_profile['region'] = 'us-east'
az_profile['scheme'] = 'https'

mocked_import_stream_response = [{
    'id': 'foo_id',
    'created': '2024-06-03',
    'created_by': 'JOE',
    'status': 'CREATED',
    'reference_name': 'DATA_STREAM_TABLE',
    'reference_alias': '2644cadb-5e8c-469f-95aa-f91c5d50874a',
    'fq_object_name': 'FOO',
    'rai_database': 'FOO',
    'rai_relation': 'imdb_example_imdb_titles',
    'data_sync_status': 'SYNCED',
    'pending_batches_count': 0,
    'next_batch_status': None,
    'next_batch_unloaded_timestamp': None,
    'next_batch_details': None,
    'last_batch_details': '{\n  "rows": 10000,\n  "size": 466459,\n  "writeChangesDuration": 2820,\n  "writeChangesEnd": "2024-06-03T17:51:22.888Z",\n  "writeChangesStart": "2024-06-03T17:51:20.068Z"\n}',
    'last_batch_unloaded_timestamp': '2024-06-03',
    'cdc_status': 'STARTED'
}]

mocked_list_imports_response = [{
    'id': 'foo_id',
    'model': 'FOO',
    'name': 'FOO',
    'created': '2024-06-03',
    'creator': 'JOE',
    'status': 'LOADED',
    'errors': None,
    'batches': '1'
},
{
    'id': 'bar_id',
    'model': 'BAR',
    'name': 'BAR',
    'created': '2024-01-01',
    'creator': 'JAKE',
    'status': 'LOADED',
    'errors': None,
    'batches': '1'
},
{
    'id': 'baz_id',
    'model': 'BAZ',
    'name': 'BAZ',
    'created': '2024-03-03',
    'creator': 'BLAKE',
    'status': 'LOADED',
    'errors': 'err1',
    'batches': '1'
}]

mocked_imports_get_details = [
    "Field                           Value",
    "id                              foo_id",
    "created                         2024-06-03",
    "created_by                      JOE",
    "status                          CREATED",
    "reference_name                  DATA_STREAM_TABLE",
    "reference_alias                 2644cadb-5e8c-469f-95aa-f91c5d50874a",
    "fq_object_name                  FOO",
    "rai_database                    FOO",
    "rai_relation                    imdb_example_imdb_titles",
    "data_sync_status                SYNCED",
    "pending_batches_count           0",
    "next_batch_status               N/A",
    "next_batch_unloaded_timestamp   N/A",
    "next_batch_details              N/A",
    """last_batch_details              {                                                  
                                    "rows": 10000,                                   
                                    "size": 466459,                                  
                                    "writeChangesDuration": 2820,                    
                                    "writeChangesEnd": "2024-06-03T17:51:22.888Z",   
                                    "writeChangesStart": "2024-06-03T17:51:20.068Z"  
                                  }""",
    "last_batch_unloaded_timestamp   2024-06-03",
    "cdc_status                      STARTED"
]

mocked_imports_status = {'engine': 'FOO_ENG', 'status': 'started', 'info': '{\n  "createdOn": "2024-06-03 10:50:04.735 -0700",\n  "lastSuspendedOn": null,\n  "lastSuspendedReason": null,\n  "state": "started"\n}'}

mocked_engines_list = [
    {'name': 'test', 'size': 'XS', 'state': 'READY'},
    {'name': 'foo', 'size': 'XS', 'state': 'READY'},
    {'name': 'bar', 'size': 'S', 'state': 'READY'},
    {'name': 'baz', 'size': 'M', 'state': 'PENDING'},
    {'name': 'goo', 'size': 'M', 'state': 'SUSPENDED'},
]

mocked_txns_list_snowflake = [
    {'id': 'id1', 'database': 'db1', 'engine': 'FOO', 'state': 'COMPLETED', 'abort_reason': None, 'read_only': False, 'created_by': 'usr', 'created_on': datetime(2024, 6, 17, 7, 11, 17, 47000), 'finished_at': datetime(2024, 6, 17, 7, 11, 18, 691000), 'duration': 1644},
    {'id': 'id2', 'database': 'db2', 'engine': 'BAR', 'state': 'ABORTED', 'abort_reason': 'Error', 'read_only': True, 'created_by': 'usr', 'created_on': datetime(2024, 6, 17, 7, 11, 15, 237000), 'finished_at': datetime(2024, 6, 17, 7, 11, 15, 805000), 'duration': 568},
    {'id': 'id3', 'database': 'db3', 'engine': 'BAZ', 'state': 'COMPLETED', 'abort_reason': None, 'read_only': True, 'created_by': 'usr2', 'created_on': datetime(2024, 6, 17, 7, 11, 3, 738000), 'finished_at': datetime(2024, 6, 17, 7, 11, 12, 259000), 'duration': 8521}
]

mocked_txns_list_azure = [
    {
        'id': 'id1',
        'state': 'COMPLETED',
        'created_by': 'foo@clients',
        'created_on': 1718389322604,
        'finished_at': 1718389322958,
        'duration': 354,
        'read_only': True,
        'query': 'def output { 1 + 2 }',
        'query_size': 20,
        'language': 'rel',
        'tags': ['vscode-internal', 'console-internal'],
        'last_requested_interval': 0, 'response_format_version': '2.0.4',
        'account': 'relationalai-team-rd-raicloud',
        'database': 'db1',
        'engine': 'FOO',
        'agent': 'agent1'
    },
    {
        'id': 'id2',
        'state': 'ABORTED',
        'created_by': 'foo@clients',
        'created_on': 1718389322123,
        'finished_at': 1718389322349,
        'duration': 226,
        'read_only': True,
        'query': 'def output { 1 + 2 }',
        'query_size': 20,
        'language': 'rel',
        'tags': ['vscode-user'],
        'last_requested_interval': 0,
        'response_format_version': '2.0.4',
        'account': 'relationalai-team-rd-raicloud',
        'database': 'db2',
        'engine': 'BAR',
        'agent': 'agent1'
    },
    {
        'id': 'id3',
        'state': 'COMPLETED',
        'created_by': 'foo@clients',
        'created_on': 1718388515992,
        'finished_at': 1718388516940,
        'duration': 948,
        'read_only': True,
        'query': 'def output { 1 + 2 }',
        'query_size': 143,
        'language': 'rel',
        'tags': ['vscode-internal', 'console-internal'],
        'last_requested_interval': 0,
        'response_format_version': '2.0.4',
        'account': 'relationalai-team-rd-raicloud',
        'database': 'db3',
        'engine': 'BAZ',
        'agent': 'agent1'
    }
]
