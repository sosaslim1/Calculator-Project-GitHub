class CurrencyConverter:
    """Class to manage currency conversion logic."""

    def __init__(self):
        """Start conversion rates."""
        self.conversion_rates = {
            "MXN": 17.50,  # Mexican Peso
            "CAD": 1.35,   # Canadian Dollar
            "JPY": 145.85, # Japanese Yen
            "EUR": 0.92    # Euro
        }

    def convert(self, amount: float, currency: str) -> float:
        """
        Convert USD to the selected currency.

        Args:
            amount (float): The amount in USD.
            currency (str): The target currency.

        Returns:
            float: The converted amount in the target currency.
        """
        if currency not in self.conversion_rates:
            raise ValueError(f"Unsupported currency: {currency}")
        return amount * self.conversion_rates[currency]

    @staticmethod
    def validate_amount(amount: str) -> float:
        """
        Validate and convert input amount to float.

        Args:
            amount (str): The input amount in string format.

        Returns:
            float: The validated amount.

        Raises:
            ValueError: If the amount is not a valid number.
        """
        try:
            return float(amount)
        except ValueError:
            raise ValueError("Invalid amount. Please enter a valid number.")
