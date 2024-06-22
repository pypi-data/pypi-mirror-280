import json

version_json = '''
{
 "date": "2024-05-02T00:00:00-0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "e583dbb6b404081dfdfab1ab566c626928f68f14",
 "version": "3.1.3"
}
'''  # END VERSION_JSON

def get_versions():
    return json.loads(version_json)
