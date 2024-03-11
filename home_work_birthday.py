from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_this_year = datetime.strptime(f"{today.year}.{user['birthday'][5:]}", "%Y.%m.%d").date()

        # Якщо день народження вже минув цього року, наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year + 1)

        # Визначаємо, чи день народження припадає на наступний тиждень
        days_until_birthday = (birthday_this_year - today).days
        if 0 <= days_until_birthday <= 7:
            # Якщо день народження припадає на вихідний, переносимо на наступний понеділок
            if birthday_this_year.weekday() >= 5:
                congratulation_date = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
            else:
                congratulation_date = birthday_this_year

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays
