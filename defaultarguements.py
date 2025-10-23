import time
#default arguements
def net_price(list_price, discount = 0 , tax= 0.05):
    return list_price * (1-discount) * (1 + tax)

print(net_price(500, 0, 0.05))


def count(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")

conut(0,10)

