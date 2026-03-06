def add_expense(expenses, new_expense):
    expenses.append(new_expense)
    return expenses

def sum_amount(expenses: list) -> float:
    total = 0
    for tutar in expenses:
        total += tutar["tutar"]
    return total

def summary_by_category(expenses):
    summary = {}
    for amount in expenses:
        kat = amount["kategori"]
        tutar = amount["tutar"]
        if kat in summary:
            summary[kat] += tutar
        else:
            summary[kat] = tutar
    return summary

def filter_by_date(expenses, target_date):
    filtered = []
    for h in expenses:
        if h["tarih"] == target_date:
            filtered.append(h)
    return filtered
