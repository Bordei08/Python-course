def validate_dict(rules, dictionary):
    key_rules = []
    for rule in rules:
        key_rules.append(rule[0])

    for key in dictionary:
        if key not in key_rules:
            print(key)
            return False

    for key in dictionary:
        key_rule = [x for x in rules if x[0] == key]
        if not dictionary[key].startswith(key_rule[0][1]):
            return False
        if not dictionary[key].endswith(key_rule[0][3]):
            return False
        if dictionary[key].find(key_rule[0][2]) == -1 or \
           dictionary[key].find(key_rule[0][2]) == 0 or \
           dictionary[key].find(key_rule[0][2]) >= len(dictionary[key]) - len(key_rule[0][2]):
            return False

    return True

print(validate_dict({("key1", "", "inside", ""), ("key2", "", "valid", "")},
                             {"key1": "come inside, it's too cold out", "key2": "this is not valid"}))    