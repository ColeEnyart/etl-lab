from api.etl.target import Quote, Tag, QuoteTags
from api.lib.db import save
from typing import Any


class QuotesAdapter:
    def quote_attributes(self: object, quote: dict) -> dict[str, str]:
        identitifer = quote["_id"]
        content = quote["content"]
        author = quote["author"]
        date_added = quote["dateAdded"]
        return {
            "identitifer": identitifer,
            "content": content,
            "author": author,
            "date_added": date_added,
        }

    def tag_attributes(self: object, quote: dict) -> dict[str, list]:
        tags = quote["tags"]
        return {"tags": tags}

    def run(
        self: object, quotes_response: dict, conn: Any, cursor: object
    ) -> list[dict[str, dict]]:
        quotes = []
        for quote in quotes_response["results"]:
            quote_attrs = self.quote_attributes(quote)
            tag_attrs = self.tag_attributes(quote)
            saved_objs = self.save_db(quote_attrs, tag_attrs, conn, cursor)
            quotes.append(saved_objs)
        return quotes

    def save_db(
        self: object,
        quote_attrs: dict[str, str],
        tag_attrs: dict[str, list],
        conn: Any,
        cursor: object,
    ) -> dict[str, dict]:
        quote_obj = Quote(**quote_attrs)
        saved_quote = save(quote_obj, conn, cursor)

        tag_objs = [Tag(name=name) for name in tag_attrs["tags"]]
        saved_tags = [save(tag, conn, cursor) for tag in tag_objs]

        QuoteTag_objs = [
            QuoteTags(quote_id=saved_quote.__dict__["id"], tag_id=tag.__dict__["id"])
            for tag in saved_tags
        ]
        saved_QuoteTags = [save(quote_tag, conn, cursor) for quote_tag in QuoteTag_objs]

        return {
            "saved_quote": saved_quote.__dict__,
            "saved_tags": [tag.__dict__ for tag in saved_tags],
            "saved_QuoteTags": [quote_tag.__dict__ for quote_tag in saved_QuoteTags],
        }
