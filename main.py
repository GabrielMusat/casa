import json


def total_price(path: str) -> float:
    casa = json.load(open(path))
    total = 0.
    for lugar in casa:
        for elemento in casa[lugar]:
            total += casa[lugar][elemento]["precio"]
    return total


if __name__ == '__main__':
    print(total_price("casa.json"))
