from rapidfuzz import fuzz

def get_similarity(name1, name2):
    return fuzz.ratio(name1, name2)

if __name__ == "__main__":
    print(get_similarity("CVS", "CVS Pharmacy"))
    print(get_similarity("McDonalds", "Burger King"))

def predict_label(name1, name2):
    score = get_similarity(name1, name2)

    if score > 70:
        return "same"
    else:
        return "current"
    
if __name__ == "__main__":
    print(predict_label("CVS", "CVS Pharmacy"))   # expect "same"
    print(predict_label("McDonalds", "Burger King"))  # expect "current"