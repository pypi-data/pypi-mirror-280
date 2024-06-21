from .main import MessageCreate
from unittest.mock import MagicMock
import responses


class TestValidation:

    def test_validate_type_success(self):
        obj = MessageCreate(private_key="your_private_key", secret_key="your_secret_key", baseUrl="your_base_url")  
        # Test if the validation passes for the correct type
        assert obj.validate_type(5, int, "Error message") is True

    def test_validate_length_success(self):
        obj = MessageCreate(private_key="your_private_key", secret_key="your_secret_key", baseUrl="your_base_url")  
        
        # Test if the validation passes for the correct type and length
        assert obj.validate_length("string length", 15, "Error message") is True
        print("Validation success: Type is string and length is within limit")

