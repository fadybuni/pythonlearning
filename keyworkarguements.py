def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
hello("Hello",title="Mr", first=  "Spongebob",last = "Squarepants")

def get_phone(country, area, first, last):
    return (f"{country}-{area}-{first}-{last}")

phone_num = get_phone(country=1, area=586, first=453,last=5181)

print(phone_num)