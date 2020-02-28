def is_valid_walk(walk):
    # determine if walk is valid
    n_s = list(filter(lambda x: x in ['n', 's'], walk))
    w_e = list(filter(lambda x: x in ['w', 'e'], walk))

    n_s = map(lambda x: 1 if x == 'n' else -1, list(n_s))
    w_e = map(lambda x: 1 if x == 'w' else -1, list(w_e))
    if len(walk) == 10:
        if sum(w_e) == 0 and sum(n_s) == 0:
            return True
        else:
            return False
    else:
        return False

print(is_valid_walk(['n', 'w', 'e', 's', 's', 'e', 'w', 'n']))

