last_sector = input()
first_sector_rows = int(input())
last_sector_rows = ord(last_sector) - 65
odd_row_seats = int(input())
even_row_seats = odd_row_seats + 2
counter = 0
for sectors in range(65, ord(last_sector) + 1):
    for rows in range(1, first_sector_rows + 1):
        if rows % 2 == 0:
            for seats in range(97, 97 + even_row_seats):
                print(f"{chr(sectors)}{rows}{chr(seats)}")
                counter += 1
        else:
            for seats in range(97, 97 + odd_row_seats):
                print(f"{chr(sectors)}{rows}{chr(seats)}")
                counter += 1
    first_sector_rows += 1
print(counter)