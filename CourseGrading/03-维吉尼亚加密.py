def password(key, flag):
    big = [chr(i) for i in range(65, 91)]
    small = [chr(i) for i in range(97, 123)]

    zs = len(flag) // len(key)
    ys = len(flag) % len(key)
    new_key = key * zs + key[: ys]
    new_key = list(new_key)

    result = ""
    for i in range(len(new_key)):
        if new_key[i] in big:
            big_index = big.index(new_key[i])
            if big.index(flag[i]) + big_index > 25:
                result += big[big.index(flag[i]) + big_index - 26]
            else:
                result += big[big.index(flag[i]) + big_index]
        elif new_key[i] in small:
            small_index = small.index(new_key[i])
            if small.index(flag[i]) + small_index > 25:
                result += small[small.index(flag[i]) + small_index - 26]
            else:
                result += small[small.index(flag[i]) + small_index]
    return result

key = input()
flag = input()

print(password(key, flag))