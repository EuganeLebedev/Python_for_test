bool_list = [True, False, False]

true_found = False
for i in bool_list:
    if i:
        true_found = True
        break

print(true_found)

true_found_any = any(bool_list)

print(true_found_any)

all_true = all(bool_list)
print(all_true)

str_list = ["asdasdasd", "zz", "reterty"]
all([len(x) > 3 for x in str_list])
all(map(lambda x: len(x) > 3, str_list))



