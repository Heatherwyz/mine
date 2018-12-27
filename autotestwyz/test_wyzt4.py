# -*- coding:utf-8 -*-
import pytest
import requests


class TestV2exApiWithExpectation(object):
    domain = 'https://www.v2ex.com/'

    @pytest.mark.parametrize("name,node_id", [('python', 90), ('java', 63), ('go', 375), ('nodejs', 436)])
    def test_node(self, name, node_id):
        path = 'api/nodes/show.json?name=%s' % (name)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == name
        assert res['id'] == node_id
        #想要看一下调试结果的话
        assert 0
