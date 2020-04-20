import io
import json

def test_save_and_get_profile(api):
    resp = api.post(
        '/login',
        data = json.dumps({'email':'haeungrace@gmail.com',
        'password':'test'},
        content_type = 'application/json')
    )
    resp_json = json.loads(resp.data.decode('utf-8'))
    access_token = resp_json['access_token']
