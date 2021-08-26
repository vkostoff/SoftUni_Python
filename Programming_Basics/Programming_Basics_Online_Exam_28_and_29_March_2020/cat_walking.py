minutes_per_day = int(input())
daily_walks = int(input())
calories_taken = int(input())

calories_burnt = (minutes_per_day * 5) * daily_walks

if calories_burnt >= (calories_taken / 2):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burnt}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burnt}.")
