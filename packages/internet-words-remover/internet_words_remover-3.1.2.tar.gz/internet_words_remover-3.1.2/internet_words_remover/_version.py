import json

version_json = '''
{
 "date": "2024-05-02T00:00:00-0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "d39af7d9bec3888ba4036f200bd45f8e8457b53f",
 "version": "3.1.2"
}
'''  # END VERSION_JSON

def get_versions():
    return json.loads(version_json)
