# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
age1 = int(age)
years_rem = (90-age1)
days_rem = (years_rem * 365)
weeks_rem = (years_rem * 52)
months_rem = (years_rem * 12)
print(f"you have {days_rem} days, {weeks_rem} weeks, and {months_rem} months left.")
