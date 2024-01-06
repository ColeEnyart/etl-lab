import pytest
from api.lib.db import (drop_all_tables, test_conn, test_cursor)
from tests.build import build_records

@pytest.fixture
def targets():
    drop_all_tables(test_conn, test_cursor)
    records = build_records()
    yield records
    drop_all_tables(test_conn, test_cursor)
    
def test_init_objects(targets):
    assert [isinstance(target, object) for target in targets]
    
def test_mass_assignment(targets):
    assert targets['saved_quote_1'].identitifer == 'BzfxvRlA2Y'
    assert targets['saved_tag_1'].name == 'Knowledge'
    assert targets['saved_quote_tag_1'].quote_id == 1
    
def test_quote_tags_returns_related_tags(targets):
    tags = [tag.name for tag in targets['saved_quote_3'].tags(test_cursor)]
    assert tags == ['Inspirational', 'Motivational']
    