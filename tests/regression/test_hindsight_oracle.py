import pytest

@pytest.mark.xfail(strict=True, reason="hindsight-oracle")
def test_hindsight_oracle():
    raise AssertionError("not implemented")
