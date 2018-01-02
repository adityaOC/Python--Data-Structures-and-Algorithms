def get_power_set(s):

    power_set = [set()]

    for element in s:
        new_sets = []
        for subset in power_set:
            new_sets.append(subset | {element})
        power_set.extend(new_sets)

    return power_set



string = "ABC"
print(get_power_set(string))
