"""Common fixtures for the V2G Liberty tests."""
from collections.abc import Generator
from unittest.mock import AsyncMock, patch

import pytest


@pytest.fixture
def mock_setup_entry() -> Generator[AsyncMock, None, None]:
    """Override async_setup_entry."""
    with patch(
        "homeassistant.components.v2g_liberty.async_setup_entry", return_value=True
    ) as mock_setup_entry:
        yield mock_setup_entry
