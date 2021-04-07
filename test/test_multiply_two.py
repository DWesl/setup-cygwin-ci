import pytest

import multiply_two


@pytest.mark.parametrize(
    "a",
    range(10)
)
@pytest.mark.parametrize(
    "b",
    range(10)
)
def test_multiply_two(a, b):
    """Test multiply_two.multiply_two_numbers."""
    assert multiply_two.multiply_two.multiply_two_numbers(a, b) == a * b
