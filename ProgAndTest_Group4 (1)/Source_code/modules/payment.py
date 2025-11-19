class PaymentManager:
    def __init__(self, db):
        self.db = db
        if "payments" not in db:
            # Initialize a list of payments if it doesn't exist
            db["payments"] = []

    def record_payment(self, order_id, amount, method="Credit Card"):
        """Records a successful payment for an order."""
        print("\n--- RECORDING PAYMENT ---")
        
        pid = len(self.db["payments"]) + 1
        
        # A simple way to get the current time for the record
        import datetime
        payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        payment_data = {
            "payment_id": pid,
            "order_id": order_id,
            "date": payment_date,
            "amount": amount,
            "method": method,
            "status": "Completed"
        }

        self.db["payments"].append(payment_data)
        print(f"Payment recorded for Order ID {order_id}. Amount: ${amount}. Status: Completed.")
        return payment_data

    def view_payments(self):
        """Displays a list of all recorded payments."""
        print("\n=== ALL PAYMENTS ===")
        if not self.db["payments"]:
            print("No payments recorded.")
            return

        for p in self.db["payments"]:
            print(f"Payment ID {p['payment_id']} | Order {p['order_id']} | ${p['amount']} | {p['date']}")
