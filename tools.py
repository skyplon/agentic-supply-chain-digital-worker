from random import choice

# Mock enterprise data

orders = [
    {"order_id": "ORD-1021", "product": "hydraulic pumps", "priority": "high"},
    {"order_id": "ORD-1045", "product": "electronic control units", "priority": "medium"},
    {"order_id": "ORD-1099", "product": "control valves", "priority": "high"},
]

inventory = {
    "hydraulic pumps": 5,
    "electronic control units": 0,
    "control valves": 2
}

suppliers = {
    "hydraulic pumps": ["Bosch Rexroth", "Parker Hannifin"],
    "electronic control units": ["Siemens Industrial", "Honeywell"],
    "control valves": ["Emerson", "Flowserve"]
}


def get_impacted_orders(product):
    impacted = [o for o in orders if product in o["product"]]

    if not impacted:
        return "No directly impacted orders detected"

    return f"{len(impacted)} impacted orders: {impacted}"


def check_inventory(product):
    qty = inventory.get(product, 0)

    if qty == 0:
        return f"⚠️ No available inventory for {product}"
    elif qty < 3:
        return f"⚠️ Low inventory for {product}: {qty} units remaining"
    else:
        return f"✅ Sufficient inventory for {product}: {qty} units available"


def find_alternative_supplier(product):
    options = suppliers.get(product, [])

    if len(options) > 1:
        alt = options[1]
        return f"Recommended alternative supplier: {alt}"
    elif options:
        return f"Only supplier available: {options[0]}"
    else:
        return "No suppliers found"


def update_order_status(order_id):
    return f"Order {order_id} rescheduled and updated with mitigation plan"