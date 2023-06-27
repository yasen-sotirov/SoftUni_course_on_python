def print_order(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def rank_order(**kwargs):
    winners = {}
    for key, value in kwargs.items():
        if value[0] > 15:
            winners[key] = value
    return winners


final_winners = rank_order(John=[15, "Sofia"], David=[17, "Sofia"], Steven=[20, "Varna"])
print_order(**final_winners)
