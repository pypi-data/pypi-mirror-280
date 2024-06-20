import sys

import pytest

# cannot currently run tests on github runners (because hosted in the US)
pytestmark = pytest.mark.skipif(
    not sys.platform.startswith("win"), reason="tests for windows only"
)


def test_place_and_cancel_order(exchanges):
    for _, exc in exchanges.items():
        # delete all open orders first
        orders = exc.cancel_orders()
        assert isinstance(orders, list)

        # place order
        order = exc.place_order(
            "ETHUSDT", type="limit", side="buy", qty=0.01, price=1000
        )
        assert order.get("id") is not None

        # cancel it
        result = exc.cancel_order(order["id"])
        assert result["success"] is True


if __name__ == "__main__":
    pytest.main([__file__])
