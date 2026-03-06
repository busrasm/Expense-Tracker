import storage
import logic
from datetime import date, datetime

expenses = storage.load_expense()

while True:
    print("-----Expense Tracker-----")
    print("1. Harcama Ekle")
    print("2. Harcamaları Listele")
    print("3. Bugün Toplam")
    print("4. Kategori Özeti")
    print("5. Çıkış")
    print("-----------------------------")
    choice = int(input("Yapmak istediğiniz işlem (1-5): "))

    if choice == 1:
        spending_date = input("Tarih (GG.AA.YYYY - Bugün için boş bırak): ")
        if spending_date == "": 
            spending_date = date.today().strftime("%d.%m.%Y") 
        amount = float(input("Tutar: "))
        category = input("Kategori: ")
        note = input("Açıklama: ")
        new_expense = {
            "tarih" : spending_date,
            "tutar" : amount,
            "kategori" : category,
            "açıklama" : note
        }
        expenses = logic.add_expense(expenses, new_expense)
        storage.save_expense(expenses)
        print("Harcama başarıyla eklendi!")

    elif choice == 2:
        for h in expenses:
            print(f"{h['tarih']} - {h['kategori']}: {h['tutar']} TL ({h['açıklama']})")
    
    elif choice == 3:
        today = date.today().strftime("%d.%m.%Y")
        today_list = logic.filter_by_date(expenses, today)
        today_total = logic.sum_amount(today_list)
        print(f"Bugünün {today} toplam harcaması: {today_total} TL")
    
    elif choice == 4:
        summary = logic.summary_by_category(expenses)
        print("\n--- KATEGORİ ÖZETİ ---")
        if not summary:
            print("Herhangi bir harcama bulunamadı.")
        else:
            for kat, tutar in summary.items(): # sözlük içindeki key ve value yu aynı anda döndürür.
                print(f"{kat.capitalize():<15}: {tutar:>8.2f} TL")
        print("-------------------------")

    elif choice == 5: 
        print("Görüşürüz!")
        break

    else:
        print("Yanlış tuşlama!!!")
        continue