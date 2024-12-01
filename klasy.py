from interfejs import TransactionResult, TransactionStatus

class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def processPayment(self, user_id, transaction_id, amount):
        if not user_id:
            print("Error: User ID cannot be empty.")
            return TransactionResult(success=False, transaction_id=transaction_id, message="User ID cannot be empty.")
        if amount <= 0:
            print("Error: Amount must be positive.")
            return TransactionResult(success=False, transaction_id=transaction_id, message="Amount must be positive.")

        try:
            result = self.payment_gateway.make_payment(user_id, amount)
            if result.success:
                print(f"Payment processed successfully for user {user_id}: {amount}")
            else:
                print(f"Error: Payment failed for user {user_id}: {result.message}")
            return result
        except Exception as e:
            print(f"An error occurred while processing payment: {str(e)}")
            return TransactionResult(success=False,transaction_id = transaction_id, message=str(e))

    def refundPayment(self, transaction_id):
        if not transaction_id:
            print("Error: Transaction ID cannot be empty.")
            return TransactionResult(success=False,transaction_id = transaction_id, message="Transaction ID cannot be empty.")

        try:
            result = self.payment_gateway.refund_payment(transaction_id)
            if result.success:
                print(f"Refund processed successfully for transaction {transaction_id}.")
            else:
                print(f"Error: Refund failed for transaction {transaction_id}: {result.message}")
            return result
        except Exception as e:
            print(f"An error occurred while processing refund: {str(e)}")
            return TransactionResult(success=False, transaction_id = transaction_id, message=str(e))

    def getPaymentStatus(self, transaction_id):
        if not transaction_id:
            print("Error: Transaction ID cannot be empty.")
            return TransactionStatus.FAILED

        try:
            status = self.payment_gateway.get_status(transaction_id)
            print(f"Payment status for transaction {transaction_id}: {status}")
            return status
        except Exception as e:
            print(f"An error occurred while retrieving payment status: {str(e)}")
            return TransactionStatus.FAILED