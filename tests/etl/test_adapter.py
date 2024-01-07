import pytest
from api.lib.db import drop_all_tables, test_conn, test_cursor
from api.etl.adapter import QuotesAdapter
import json

# json_file_path = './tests/response.json'
# with open(json_file_path, 'r') as json_file:
#         data = json.load(json_file)


@pytest.fixture
def adapter():
    drop_all_tables(test_conn, test_cursor)
    quotes_adapter = QuotesAdapter()
    yield quotes_adapter
    drop_all_tables(test_conn, test_cursor)


@pytest.fixture
def data():
    json_file_path = "/jigsaw/etl-lab/tests/response.json"
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    return data


def test_init_quotes_adapter(adapter):
    assert isinstance(adapter, object)


def test_quote_attributes_returns_selected(adapter, data):
    quote_attributes = adapter.quote_attributes(data["results"][0])
    assert quote_attributes == {
        "author": "Thomas Edison",
        "content": "As a cure for worrying, work is better than whisky.",
        "date_added": "2023-04-14",
        "identitifer": "bfNpGC2NI",
    }


def test_tag_attributes_returns_selected(adapter, data):
    tag_attributes = adapter.tag_attributes({"tags": data["results"][0]["tags"]})
    assert tag_attributes == {"tags": ["Humorous"]}


def test_save_db_returns_saved_objects(adapter, data):
    quote_attributes = adapter.quote_attributes(data["results"][0])
    tag_attributes = adapter.tag_attributes({"tags": data["results"][0]["tags"]})
    saved_objects = adapter.save_db(
        quote_attributes, tag_attributes, test_conn, test_cursor
    )
    assert saved_objects == {
        "saved_QuoteTags": [{"id": 1, "quote_id": 1, "tag_id": 1}],
        "saved_quote": {
            "author": "Thomas Edison",
            "content": "As a cure for worrying, work is better than whisky.",
            "date_added": "2023-04-14",
            "id": 1,
            "identitifer": "bfNpGC2NI",
        },
        "saved_tags": [{"id": 1, "name": "Humorous"}],
    }


def test_run_returns_all_saved_objects(adapter, data):
    all_objects = adapter.run(data, test_conn, test_cursor)
    assert all_objects[:2] == [
        {
            "saved_quote": {
                "id": 1,
                "identitifer": "bfNpGC2NI",
                "content": "As a cure for worrying, work is better than whisky.",
                "author": "Thomas Edison",
                "date_added": "2023-04-14",
            },
            "saved_tags": [{"id": 1, "name": "Humorous"}],
            "saved_QuoteTags": [{"id": 1, "quote_id": 1, "tag_id": 1}],
        },
        {
            "saved_quote": {
                "id": 2,
                "identitifer": "ghVnmSpeAo",
                "content": "Everything comes to him who hustles while he waits.",
                "author": "Thomas Edison",
                "date_added": "2023-04-14",
            },
            "saved_tags": [
                {"id": 2, "name": "Success"},
                {"id": 3, "name": "Motivational"},
            ],
            "saved_QuoteTags": [
                {"id": 2, "quote_id": 2, "tag_id": 2},
                {"id": 3, "quote_id": 2, "tag_id": 3},
            ],
        },
    ]
