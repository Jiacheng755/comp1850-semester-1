try:
   monthly_amount = float(input("Enter the monthly amount: "))
   
   total_savings = monthly_amount * 12
   print(total_savings)

   interest = total_savings * 0.008
   total_with_interest = total_savings+ interest

   print(f"£{total_with_interest:.2f}") 

except ValueError:
    print("Invalid amount")
    