"""Shared config: đọc Confluence credentials từ .gemini/settings.json."""
import json
import sys
from base64 import b64encode
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
SETTINGS_FILE = ROOT / ".gemini" / "settings.json"
MEMORIES_DIR = ROOT / "docs" / "memories"
SPACE = "VNXMKT"


def load_config() -> dict:
    """Đọc Confluence credentials từ MCP settings."""
    if not SETTINGS_FILE.exists():
        print("❌ Không tìm thấy .gemini/settings.json")
        sys.exit(1)
    data = json.loads(SETTINGS_FILE.read_text())
    env = data["mcpServers"]["atlassian"]["env"]
    return {
        "base_url": env["ATLASSIAN_URL"],
        "username": env["ATLASSIAN_USERNAME"],
        "token": env["ATLASSIAN_API_TOKEN"],
    }


CONFIG = load_config()
BASE_URL = CONFIG["base_url"]
AUTH_HEADER = {
    "Authorization": f"Basic {b64encode(f'{CONFIG['username']}:{CONFIG['token']}'.encode()).decode()}",
    "Accept": "application/json",
}
