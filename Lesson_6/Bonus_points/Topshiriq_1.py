hall = {
    "Samsung A12":{"price":120, "qty":10},
    "Samsung A53":{"price":300, "qty":7},
    "Samsung S23":{"price":800, "qty":4},
    "Iphone 15":{"price":1200, "qty":3},
    "redmi":{"price":110, "qty":10}
}
info = {
    "out":0,
    "clients":0,
    "summa":0

}

def bozor():
    savat = []
    summa = 0
    for nomi in hall:
        tovar = input("\nSalom nima sotib olmoqchisiz\nNomi >>> ")

        if tovar in hall:
            mahsulot = hall.get(tovar)
            qty = hall.get(tovar)

            print(f"narxi {mahsulot["price"]} $")

            soni = int(input("Soni >>> "))
            if soni <= qty["qty"]:
                print("Buyurtma Qabul qilindi  :)")
                info["out"] += 1
                info["clients"] += 1

                savat.append(tovar)
                if soni > 2:
                    print("Sizga 5% chegirma bor!  :)")

                    # chegirmali
                    chegirma = (mahsulot["price"] / 100) * 5
                    summa += mahsulot["price"] - chegirma

                # chegirmasiz
                summa += mahsulot["price"]
                info["summa"] += summa
            else:
                print("omborda buncha tovar mavjud emas")

        else:
            print(f"{tovar} hali  mavjud emas")

    print(f"siz {len(savat)} ta tovar sotib oldingiz! \nJami narx: {summa} $ ")

    print(f"\nbugun {info["out"]} ta sotildi\n{info["clients"]} ta xaridor keldi\n{info["summa"]} summa bo'ldi!")





bozor()
