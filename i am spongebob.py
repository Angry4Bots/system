import json
try:
    with open('users.json','r') as f:
        d = json.load(f)
except:
    print("coś poszło nie tak")
# class Worker:
#     employee = dict
#     def __init__(self,nick,password,permission,number):
#         self.nick = nick
#         self.password = password
#         self.permission = permission
#         self.number = number
#     def create_an_employee(self):
#         employee = {}
#         employee["nick"] = self.nick,
#         employee["password"] = self.password,
#         employee["permission"] = self.permission,
#         employee["number"] = self.number,

p = True
log_out = -1
def browser(i):
    global p
    global log_out
    spongebob = -1
    print("Witam "+i["nick"])
    print(i)
    i = i
    while p:
        print(i)
        print("0.Wyjście")
        print("1.Towary")
        print("2.Użytkownicy")
        print("3.Raport")
        print("4.Wyloguj się")
        spongebob = int(input("Twój wybór:"))
        if int(i["permission"]) > 3 and spongebob == 2:
            with open('users.json','r') as user:
                u = json.load(user)
            for r in u["users"]:
                clean_r = str(r).replace("{","").replace("[","").replace("'","").replace("}","")
                print(clean_r)
            print("Co chcesz zmienić?")
            print("1.Nic")
            print("2.Usunąć Użytkownika")
            print("3.Zmienić wartość")
            try:
                kasacja = int(input("Twój wybór:"))
            except ValueError:
                print("Jeszcze raz, wpisz tym razem liczbe")
                kasacja = int(input("Twój wybór:"))
            if kasacja == 2:
                print("Którego (Podaj numer, który jest podany jako ostatni w użytkownik)")
                deleting = input("Numer:")
                for d in u["users"]:
                    if d["number"] == deleting:
                        u["users"].remove(d)
                with open('users.json', 'w') as user:
                    json.dump(u, user)
            if kasacja == 3:
                print("Jakiego usera chcesz zmienić wartość(Podaj numer usera od góry)")
                change = input("Twój wybór:")
                print("Jaką chcesz zmienić wartość")
                print("1.Nick")
                print("2.Password")
                print("3.Permission")
                print("4.Number")
                try:
                    change2 = int(input("Twój wybór:"))
                except ValueError:
                    print("Jeszcze raz, wpisz tym razem liczbe")
                    change2 = int(input("Twój wybór:"))
                change3 = str(input("Na co chcesz zmienić:"))
                for idx, p in enumerate(u["users"]):
                    if idx == change - 1:
                        if change2 == 1:
                            p["nick"] = change3
                        if change2 == 2:
                            p["password"] = change3
                        if change2 == 3:
                            p["permission"] = change3
                        if change2 == 4:
                            p["number"] = change3
                with open('users.json', 'w') as user:
                    json.dump(u, user)
        if int(i["permission"]) < 3 and spongebob == 2:
            print("Nie masz wystarczających permisji")
        if spongebob == 1:
            print("1.Sprzedaż")
            print("2.Kupno")
            print("3.Sprawdzenie pieniędzy")
            try:
                browsing = int(input("Twój wybór:"))
            except ValueError:
                print("Jeszcze raz, wpisz tym razem liczbe")
                browsing = int(input("Twój wybór:"))
            if browsing > 3:
                print("Kurcze chyba troche za daleko")
                browsing = int(input("Twój wybór:"))
            if browsing == 3:
                with open('currency.json','r') as money:
                    c = json.load(money)
                print("O to pieniążki:\n")
                for m in c["list of money"]:
                    clean_m = str(m).replace("{","").replace("[","").replace("'","").replace("}","")
                    print(clean_m + "\n")
            if int(i["permission"]) > 2 and browsing == 2:
                with open('black market.json','r') as buy:
                    t = json.load(buy)
                for i in t["products"]:
                    clean_i = str(i).replace("{","").replace("[","").replace("'","").replace("}","")
                    print(clean_i)
                print("Co chcesz kupić")
                print("1.Nic")
                print("2.Jurka Owsiaka")
                print("3.Artura Rojka")
                print("4.Magika")
                try:
                    choice = int(input("Twój wybór:"))
                except ValueError:
                    print("Jeszcze raz, wpisz tym razem liczbe")
                    continue
                if choice > 5:
                    print("Kurcze chyba troche za daleko")
                if choice == 2:
                    with open('currency.json', 'r') as ilikemoney:
                        v = json.load(ilikemoney)
                        money = int(v["list of money"][0]["money"])
                    with open('black market.json', 'r') as buy:
                        t = json.load(buy)
                        price = int(t["products"][choice - 2]["price"])
                    if money < price:
                        print("Zero pieniędzy?")
                    if money >= price:
                        money = money - price
                        v["list of money"][0]["money"] = str(money)
                        print("Uhuhu kupiłeś Jurka Owsiaka. Został teraz twoim pracownikiem.")
                        t["products"][choice - 2]["quantity"] = str(int(t["products"][choice - 2]["quantity"]) - 1)
                        money = str(money)
                        with open('black market.json', 'w') as buy_file:
                            json.dump(t, buy_file)
                        with open('users.json', 'r') as f:
                            data = json.load(f)
                        data["users"].append({"nick": "Jurek Owsiak", "password": "KochamCzeczenow1954", "permission": "1", "number": "70"})
                        with open('users.json', 'w') as user:
                            json.dump(data, user)
                        with open('currency.json', 'w') as money_file:
                            json.dump(v, money_file)

                if choice == 3:
                    with open('currency.json', 'r') as ilikemoney:
                        v = json.load(ilikemoney)
                        money = int(v["list of money"][0]["money"])
                    with open('black market.json', 'r') as buy:
                        t = json.load(buy)
                        price = int(t["products"][choice - 2]["price"])
                    if money < price:
                        print("Zero pieniędzy?")
                    if money >= price:
                        money = money - price
                        v["list of money"][0]["money"] = str(money)
                        print("Uhuhu kupiłeś Artura Rojka. W końcu nie jest sam, został teraz twoim pracownikiem.")
                        t["products"][choice - 2]["quantity"] = str(int(t["products"][choice - 2]["quantity"]) - 1)
                        money = str(money)
                        with open('black market.json', 'w') as buy_file:
                            json.dump(t, buy_file)
                        with open('users.json', 'r') as f:
                            data = json.load(f)
                        data["users"].append({"nick": "Artur Rojek", "password": "KochamPloty1972", "permission": "4", "number": "52"})
                        with open('users.json', 'w') as user:
                            json.dump(data, user)
                        with open('currency.json', 'w') as money_file:
                            json.dump(v, money_file)

                if choice == 4:
                    print("Nie ma Magika😔")
                if choice == 5:
                    with open('currency.json', 'r') as ilikemoney:
                        v = json.load(ilikemoney)
                        money = int(v["list of money"][0]["money"])
                    with open('black market.json', 'r') as buy:
                        t = json.load(buy)
                        price = int(t["products"][choice - 2]["price"])
                    if money < price:
                        print("Zero pieniędzy?")
                    if money >= price:
                        money = money - price
                        v["list of money"][0]["money"] = str(money)
                        print("Uhuhu kupiłeś szyszke.")
                        t["products"][choice - 2]["quantity"] = str(int(t["products"][choice - 2]["quantity"]) - 1)
                        money = str(money)
                        with open('black market.json', 'w') as buy_file:
                            json.dump(t, buy_file)
                        with open('products.json', 'r') as f:
                            w = json.load(f)
                        try:
                            w["products"][4]["quantity"] = str(int(w["products"][choice - 2]["quantity"]) + 1)
                        except IndexError:
                            w["products"].append({"name": "Szyszka", "price": "1", "quantity": "1"})
                        with open('products.json', 'w') as f:
                            json.dump(w, f)
                        with open('currency.json', 'w') as money_file:
                            json.dump(v, money_file)
                
        if spongebob == 0:
            p = False
            log_out = 1
            return
        if spongebob == 4:
            return
while p:
    inp = input("Twoja nazwa: ")
    inp2 = input("Twoje hasło: ")
    user_found = False
    
    for i in d["users"]:
        if i["password"] == inp2 and i["nick"] == inp:
            user_found = True
            browser(i)
            if log_out == 1:
                break

    if user_found == False:
        print("Nie ma takiego użytkownika")
        continue