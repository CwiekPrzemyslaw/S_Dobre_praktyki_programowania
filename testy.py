import unittest
from unittest.mock import MagicMock
from interfejs import NetworkException, TransactionResult, TransactionStatus
from klasy import PaymentProcessor

class TestPaymentProcessor(unittest.TestCase):

    def setUp(self):
        """Przygotowanie obiektu PaymentProcessor do testów."""
        self.payment_gateway = MagicMock()
        self.processor = PaymentProcessor(self.payment_gateway)

    def test_process_payment_success(self):
        """Test prawidłowego przetworzenia płatności."""
        self.payment_gateway.make_payment.return_value = TransactionResult(True, "12345", "Payment successful.")
        
        result = self.processor.processPayment("user123", 100.0)
        
        self.assertTrue(result.success)
        self.assertEqual(result.transaction_id, "12345")
        self.assertEqual(result.message, "Payment successful.")

    def test_process_payment_insufficient_funds(self):
        """Test niepowodzenia płatności z powodu braku środków."""
        self.payment_gateway.make_payment.return_value = TransactionResult(False, "", "Insufficient funds.")
        
        result = self.processor.processPayment("user123", 100.0)
        
        self.assertFalse(result.success)
        self.assertEqual(result.message, "Insufficient funds.")

    def test_process_payment_network_exception(self):
        """Test obsługi wyjątku NetworkException."""
        self.payment_gateway.make_payment.side_effect = NetworkException("Network error.")
        
        result = self.processor.processPayment("user123", 100.0)
        
        self.assertFalse(result.success)
        self.assertIn("Network error.", result.message)

    def test_process_payment_invalid_amount(self):
        """Test walidacji nieprawidłowych danych wejściowych (ujemna kwota)."""
        result = self.processor.processPayment("user123", -50.0)
        
        self.assertFalse(result.success)
        self.assertEqual(result.message, "Amount must be positive.")

    def test_process_payment_empty_user_id(self):
        """Test walidacji pustego userId."""
        result = self.processor.processPayment("", 100.0)
        
        self.assertFalse(result.success)
        self.assertEqual(result.message, "User ID cannot be empty.")

    def test_refund_payment_success(self):
        """Test prawidłowego dokonania zwrotu."""
        self.payment_gateway.refund_payment.return_value = TransactionResult(True, "12345", "Refund successful.")
        
        result = self.processor.refundPayment("12345")
        
        self.assertTrue(result.success)
        self.assertEqual(result.message, "Refund successful.")

    def test_refund_payment_nonexistent_transaction(self):
        """Test niepowodzenia zwrotu z powodu nieistniejącej transakcji."""
        self.payment_gateway.refund_payment.return_value = TransactionResult(False, "", "Transaction not found.")
        
        result = self.processor.refundPayment("nonexistent_id")
        
        self.assertFalse(result.success)
        self.assertEqual(result.message, "Transaction not found.")

    def test_refund_payment_network_exception(self):
        """Test obsługi wyjątku NetworkException podczas zwrotu."""
        self.payment_gateway.refund_payment.side_effect = NetworkException("Network error.")
        
        result = self.processor.refundPayment("12345")
        
        self.assertFalse(result.success)
        self.assertIn("Network error.", result.message)

    def test_refund_payment_empty_transaction_id(self):
        """Test walidacji pustego transactionId."""
        result = self.processor.refundPayment("")
        
        self.assertFalse(result.success)
        self.assertEqual(result.message, "Transaction ID cannot be empty.")

    def test_get_payment_status_success(self):
        """Test pobrania poprawnego statusu transakcji."""
        self.payment_gateway.get_status.return_value = TransactionStatus.COMPLETED
        
        status = self.processor.getPaymentStatus("12345")
        
        self.assertEqual(status, TransactionStatus.COMPLETED)

    def test_get_payment_status_nonexistent_transaction(self):
        """Test obsługi nieistniejącej transakcji."""
        self.payment_gateway.get_status.side_effect = ValueError("Transaction not found.")
        
        status = self.processor.getPaymentStatus("nonexistent_id")
        
        self.assertEqual(status, TransactionStatus.FAILED)

    def test_get_payment_status_network_exception(self):
        """Test obsługi wyjątku NetworkException podczas pobierania statusu."""
        self.payment_gateway.get_status.side_effect = NetworkException("Network error.")
        
        status = self.processor.getPaymentStatus("12345")
        
        self.assertEqual(status, TransactionStatus.FAILED)

    def test_get_payment_status_empty_transaction_id(self):
        """Test walidacji pustego transactionId."""
        status = self.processor.getPaymentStatus("")
        
        self.assertEqual(status, TransactionStatus.FAILED)

if __name__ == "__main__":
    unittest.main()
