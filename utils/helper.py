def calculate_total_volume(items):
    return sum(item.volume * item.quantity for item in items)

def calculate_total_weight(items):
    return sum(item.weight * item.quantity for item in items)