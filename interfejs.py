class PaymentGateway:
    def charge(self, user_id: str, amount: float):
        if not user_id:
            raise ValueError("User ID cannot be empty.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        try:
            print(f"Charging user {user_id} for amount: {amount}")
            
            success = True  
            
            if not success:  
                raise PaymentException("Payment processing failed.")
            
            if False: 
                raise NetworkException("Network error occurred.")

            return {"success": True, "message": "Charge successful."}

        except NetworkException as ne:
            raise NetworkException(f"Network error: {str(ne)}")
        except PaymentException as pe:
            raise PaymentException(f"Payment error: {str(pe)}")
        
    def refund(self, transaction_id: str):

        if not transaction_id:
            raise ValueError("Transaction ID cannot be empty.")

        try:
            print(f"Refunding transaction {transaction_id}")

            success = True 
            
            if not success:  
                raise RefundException("Refund processing failed.")
            
            if False:  
                raise NetworkException("Network error occurred.")

            return {"success": True, "message": "Refund successful."}

        except NetworkException as ne:
            raise NetworkException(f"Network error: {str(ne)}")
        except RefundException as re:
            raise RefundException(f"Refund error: {str(re)}")
        
    def getStatus(self, transaction_id: str):
        if not transaction_id:
            raise ValueError("Transaction ID cannot be empty.")

        try:
            print(f"Getting status for transaction {transaction_id}")

            status = "COMPLETED"  

            if False:  
                raise NetworkException("Network error occurred.")

            return status

        except NetworkException as ne:
            raise NetworkException(f"Network error: {str(ne)}")
        
class TransactionResult:
    def __init__(self, success: bool, transaction_id: str, message: str = ""):
        self.success = success
        self.transaction_id = transaction_id
        self.message = message

from enum import Enum

class TransactionStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class NetworkException(Exception):
    """Rzucany w przypadku problemów z siecią."""
    pass

class PaymentException(Exception):
    """Rzucany w przypadku błędów płatności."""
    pass

class RefundException(Exception):
    """Rzucany w przypadku błędów podczas zwrotu."""
    pass
