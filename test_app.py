import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == "What's up from Scotland BABY"

    def test_get_members_handler(self, api):
        res = api.get('/members')
        assert res.status == '200 OK'
        # assert len(res.json) == 2


    def test_post_members_handler(self, api):
        mock_member = json.dumps({'name': 'name'})
        mock_headers = {'Content-Type': 'application/json'}

        res = api.post('/members', data=mock_member, headers=mock_headers)
        assert res.status == '201 CREATED'
        # assert res.json['name'] == 'name'


    def test_get_member_handler(self, api):
        res = api.get('/members/1')
        assert res.status == '200 OK'
        assert res.json['name'] == 'sam'


    def test_patch_member_handler(self, api):
        mock_changes = json.dumps({'alter-ego': 'batman'})
        mock_headers = {'Content-Type': 'application/json'}

        res = api.patch('members/1', data=mock_changes, headers=mock_headers)
        assert res.status == '202 ACCEPTED'
        assert res.json['alter-ego'] == 'batman'


    def test_delete_member_handler(self, api):
        res = api.delete('members/1')
        assert res.status == '204 NO CONTENT'



    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']
