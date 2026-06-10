"""Fetch pages từ Confluence REST API.

Trả về list[dict] với mỗi page: { id, title, space, html }.
"""
import json
import urllib.request

from .config import AUTH_HEADER, BASE_URL, SPACE


def api_get(path: str) -> dict:
    """GET request đến Confluence REST API."""
    req = urllib.request.Request(f"{BASE_URL}{path}", headers=AUTH_HEADER)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def fetch_page(page_id: str) -> dict:
    """Fetch 1 page: id, title, HTML body."""
    data = api_get(f"/wiki/rest/api/content/{page_id}?expand=body.storage,space")
    return {
        "id": data["id"],
        "title": data["title"],
        "space": data.get("space", {}).get("key", SPACE),
        "html": data.get("body", {}).get("storage", {}).get("value", ""),
    }


def fetch_children(parent_id: str) -> list[dict]:
    """Fetch danh sách children pages (chỉ id + title)."""
    data = api_get(f"/wiki/rest/api/content/{parent_id}/child/page?limit=50")
    return [{"id": p["id"], "title": p["title"]} for p in data.get("results", [])]
