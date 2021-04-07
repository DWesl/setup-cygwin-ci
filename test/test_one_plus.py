import pytest

import one_plus

@pytest.mark.parametrize(
    "i",
    range(10)
)
def test_one_plus(i):
    """Test one_plus.one_plus."""
    assert one_plus.one_plus(i) == i + 1
