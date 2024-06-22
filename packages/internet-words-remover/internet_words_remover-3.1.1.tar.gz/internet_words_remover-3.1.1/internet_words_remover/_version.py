import json

version_json = '''
{
 "date": "2024-05-02T00:00:00-0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "4b4bb47b82062a17311aef1aac3102381f73b2fe",
 "version": "3.1.1"
}
'''  # END VERSION_JSON

def get_versions():
    return json.loads(version_json)
