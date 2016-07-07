# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Pytest
import pytest

pytestmark = pytest.mark.django_db


def test_api_endpoint(client):
    url = '/api/suttacontri/'
    content = client.get(url)
    assert content.status_code == 405  # GET METHOD NOT ALLOWED
    data = {
        "name": "test",
        "brand_of_cig": "test",
        "number_of_cig": "test",
        "money_given": "100.00"
    }
    content = client.post(url, data)
    assert content.status_code == 201  # Created
