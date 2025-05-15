# 💰 BillSplitPro - Tip & Bill Split Calculator

print("Welcome to BillSplitPro! 💸")
print("----------------------------")


# Input section
try:
    bill_amount = float(input("Enter total bill amount (in ₹): "))
    tip_percent = float(input("Enter tip percentage you want to give: "))
    num_people = int(input("How many people to split the bill with? "))

    # Calculations
    tip_amount = (tip_percent / 100) * bill_amount
    total_bill = bill_amount + tip_amount
    per_person = total_bill / num_people

    # Feedback generator based on tip %
    if tip_percent > 20:
        feedback = "You are generous! 😊"
    elif 10 <= tip_percent <= 20:
        feedback = "Thanks for being fair. 🙂"
    else:
        feedback = "Tight on budget? 😅"

    # Output Section
    print("\n--------------------------")
    print(f"Base Bill: ₹{round(bill_amount, 2)}")
    print(f"Tip @{tip_percent}%: ₹{round(tip_amount, 2)}")
    print(f"Total Bill: ₹{round(total_bill, 2)}")
    print(f"Each person pays: ₹{round(per_person, 2)}")
    print(f"Feedback: {feedback}")
    print("--------------------------")

except ValueError:
    print("\n❌ Please enter valid numbers only!")

