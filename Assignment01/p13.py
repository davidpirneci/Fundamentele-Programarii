def find_nth_element(n: int) -> int:
    position = 0
    number = 1

    while True:
        if number == 1:
            position += 1
            if position == n:
                return 1
        else:
            temp = number
            d = 2
            while d*d<=temp:
                if temp % d == 0:
                    position += 1
                    if position == n:
                        return d

                while temp % d == 0:
                    temp //= d

                d += 1

            if temp > 1:
                position += 1
                if position == n:
                    return temp

        number += 1


n = int(input("Enter a natural non-null number: "))
print(f"The {n}-th element is:", find_nth_element(n))

