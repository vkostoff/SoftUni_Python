book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_per_book = book_pages / pages_per_hour
hours_reading_per_day = hours_per_book / days

print(hours_reading_per_day)