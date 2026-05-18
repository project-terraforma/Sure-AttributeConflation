def get_clean_name(name_str): #takes name
    import json
    try:
        name_dict = json.loads(name_str)
        return name_dict.get("primary", "")
    except:
        return ""
    
#first rule: for a group of names, pick the best one
def pick_longest_name(names):
    if not names:
        return ""
    return max(names, key=len)

if __name__ == "__main__": #test
    test_names = ["CVS", "CVS Pharmacy", "CVS Store"]
    print(pick_longest_name(test_names))

if __name__ == "__main__":
    test_names = ["99 Ranch Market", "99 Ranch"]
    print(pick_longest_name(test_names))

"""
if __name__ == "__main__":
    test_names = ["99 Ranch Market", "99 Ranch", "99 Ranch market"]
    print(pick_longest_name(test_names))
"""



