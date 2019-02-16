# Betting Accounts Stats
# Isachard Rodriguez

import datetime
from calendar import monthrange


def breakdown_weekly():
    start = 17
    now = datetime.datetime.now()
    now = int(now.strftime("%j"))

    dates_differences = now - start

    avg_weekly = ("%.2f" % (dates_differences / 7))

    return float(avg_weekly)


def breakdown_monthly():
    start = 17
    now = datetime.datetime.now()
    now = int(now.strftime("%j"))

    dates_differences = now - start

    avg_monthly = ("%.2f" % (dates_differences / 30))
    print(avg_monthly)

    return float(avg_monthly)


savings = 2000
bookmaker = 51.06
dimes = 28.47

uSavings = 1691.38
uBookmaker = 195.19
u5dimes = 0.00

start = savings + bookmaker + dimes
now = uSavings + uBookmaker + u5dimes


print("\nBetting System Stats:")
print("\nInitial amount: " + str("%.2f" % start))
print("\nCurrent amount: " + str("%.2f" % now))

formulaSavings = ((float(now)-start) / start) * 100
weekly_rate = formulaSavings / breakdown_weekly()
#monthly_rate = formulaSavings *breakdown_monthly()


print("\nSavings up by: " + str("%.2f" % formulaSavings) + "% \n")
print("Weekly rate by: " + str("%.2f" % weekly_rate) + "% \n")
#print("\nMonthly rate by: " + str("%.2f" %monthly_rate) + "% \n"  )
