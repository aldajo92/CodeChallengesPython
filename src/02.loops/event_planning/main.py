read_input = input()

try:

    while read_input is not None:
        n, b, h, w = [int(x) for x in read_input.split(" ")]

        cheap_cost = 0
        weeks = 0
        for i in range(h):
            price = int(input())
            arr_beds = [int(x) for x in input().split(" ")]

            total_event = 0
            w_to_take = 0
            total_weekend = price * n

            for bed in arr_beds:
                if n <= bed and (total_event + total_weekend) <= b:
                    w_to_take += 1
                    total_event += total_weekend

            if (total_weekend < cheap_cost and w_to_take > 0) or cheap_cost == 0:
                weeks = w_to_take
                cheap_cost = total_weekend

        if weeks == 0:
            print("stay home")
        else:
            print(cheap_cost)

        read_input = input()

except EOFError:
    pass


'''
n, b, h, w = [int(x) for x in input().split(" ")]

cheap_cost = 0
weeks = 0
for i in range(h):
    price = int(input())
    arr_beds = [int(x) for x in input().split(" ")]

    total_event = 0
    w_to_take = 0
    total_weekend = price * n

    for bed in arr_beds:
        if n <= bed and (total_event + total_weekend) <= b:
            w_to_take += 1
            total_event += total_weekend

    if (total_weekend < cheap_cost and w_to_take > 0) or cheap_cost == 0:
        weeks = w_to_take
        cheap_cost = total_weekend

if weeks == 0:
    print("stay home")
else:
    print(cheap_cost)

'''