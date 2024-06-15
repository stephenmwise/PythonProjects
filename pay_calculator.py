#daily pay weekly pay and monthly pay
print("Welcome to the income calculator!")

#define variables and input expected wages, hours, and tips
hourly_pay = 17
hours_worked_4 = int(input("How many 4 hour days expected this week? "))
hours_worked_6 = int(input("How many 6 hour days expected this week? "))
hours_worked_8 = int(input("How many 8 hour days expected this week? "))
weekly_tips = int(input("How much in tips expected? "))

#calculate values and define more variables
total_hours = ((hours_worked_4*4) + (hours_worked_6*6) + (hours_worked_8*8))
pre_tax_pay = (total_hours * hourly_pay) + weekly_tips

#Calculates taxes
taxes = 0.047
taxes_removed = int(taxes * pre_tax_pay)
after_tax_pay = int(pre_tax_pay - taxes_removed)

#Calculates 2 weeks and 1 month of predicted pay
weeks_2 = after_tax_pay * 2
weeks_4 = after_tax_pay * 4
weeks_6 = after_tax_pay * 6
#Totals time and income to user
print(f"you worked {total_hours} hours this week")
print(f"You earned ${after_tax_pay} after taxes, and ${taxes_removed} was taxed.")
print(f"If you work this much for 2 weeks you'll earn ${weeks_2} and if 4 weeks: ${weeks_4}")
print(f"If 6 weeks, ${weeks_6}")