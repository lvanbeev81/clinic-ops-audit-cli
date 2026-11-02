patient_name = input("Enter patient name: ")
billed_charge = float(input("Enter billed charge: "))
allowed_amount = float(input("Enter allowed amount: "))
copay = float(input("Enter copay: "))
procedure_name = input("Enter procedure name: ")
has_prior_auth = input("Has prior authorization? (y/n): ").lower().strip()

contractual_writeoff = billed_charge - allowed_amount

if billed_charge > 1000.00 and has_prior_auth != 'y':
    claim_status = "DENIED: Missing Prior Authorization"
    insurance_payout = 0.00
    patient_responsibility = allowed_amount
elif copay > allowed_amount or allowed_amount > billed_charge:
    claim_status = "FLAGGED: Billing Discrepancy"
    insurance_payout = 0.00
    patient_responsibility = 0.00
else:
    claim_status = "APPROVED: In-Network Clean Claim"
    insurance_payout = allowed_amount - copay
    patient_responsibility = copay

print(f"\n--- CLAIM AUDIT RESULT: {patient_name.title()} ---")
print(f"Procedure: {procedure_name.title()}")
print(f"Status:    {claim_status}")
print(f"Insurance Payout: ${insurance_payout:.2f} | Patient Responsibility: ${patient_responsibility:.2f}")