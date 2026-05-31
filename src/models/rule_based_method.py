def get_clean_name(name_str):
    import json

    try:
        name_dict = json.loads(name_str)
        return name_dict.get("primary", "")
    except:
        return ""
def predict_label(current, base):
    """
    Predict whether the current value, base value,
    or both values should be selected.
    """

    if current == base:
        return "same"
    elif len(base) > len(current):
        return "base"
    else:
        return "current"
# quick tests
if __name__ == "__main__":
    print(predict_label("BP", "BP"))  # same
    print(predict_label("Norauto España", "Norauto"))  # current
    print(predict_label("SushiCo", "SushiCo | Sushi & Bubble Tea Ede"))  # base