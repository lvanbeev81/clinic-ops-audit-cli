patient_name = input("Enter patient name: ")
billed_charge = float(input("Enter billed charge: "))
allowed_amount = float(input("Enter allowed amount: "))
copay = float(input("Enter copay: "))
contractual_writeoff = billed_charge - allowed_amount
insurance_payout = allowed_amount - copay
print(f"{patient_name}, ${contractual_writeoff:.2f}, ${insurance_payout:.2f}, ${copay:.2f}")