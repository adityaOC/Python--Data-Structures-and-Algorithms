def reverse(s):
    # Base Case
    if len(s) <= 1:
        return s

    # Recursion
    return reverse(s[1:]) + s[0]



print(str(reverse("ABC")))


def permute(s):
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, let in enumerate(s):

            print(permute(s[:i] + s[i + 1:]))
            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i + 1:]):
                # Add it to output
                out += [let + perm]

    return out


print(permute("abc"))
