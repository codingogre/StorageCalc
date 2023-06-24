# This is a sample Python script.

# Price per GB / month
OBJECT_STORE_RATE = 0.0330
# In TB
DAILY_INGEST = 1
# Cost per TB / month
OBJECT_STORE_COST_MONTHLY = (OBJECT_STORE_RATE * 1024 * DAILY_INGEST)
# Cost per TB / day
OBJECT_STORE_COST_DAILY = OBJECT_STORE_COST_MONTHLY / 30
# Days in a year
YEAR_DAYS = 365

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    total_cost = 0
    for i in range(1, YEAR_DAYS):
        total_cost   = total_cost + OBJECT_STORE_COST_DAILY
    print(f"Total annual cost: {total_cost:.2f}")
    print(f"Total monthly cost: {OBJECT_STORE_COST_MONTHLY:.2f}")
    print(f"Total daily cost: {OBJECT_STORE_COST_DAILY:.2f}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
