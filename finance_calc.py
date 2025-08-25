
import math
import json
import os
from utils import get_numeric_input, display_error, get_menu_choice

class FinancialCalculator:
    def __init__(self, history_manager):
        self.history_manager = history_manager
        self.currency_rates = self.load_currency_rates()

    def load_currency_rates(self):
        """Load currency rates from JSON file or use defaults"""
        rates_file = "data/currency.json"
        default_rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.75,
            "JPY": 110.0,
            "INR": 74.0,
            "CAD": 1.25,
            "AUD": 1.35,
            "CHF": 0.92,
            "CNY": 6.45
        }

        try:
            if os.path.exists(rates_file):
                with open(rates_file, 'r') as f:
                    return json.load(f)
            else:
                # Create directory if it doesn't exist
                os.makedirs(os.path.dirname(rates_file), exist_ok=True)
                # Save default rates
                with open(rates_file, 'w') as f:
                    json.dump(default_rates, f, indent=2)
                return default_rates
        except Exception as e:
            print(f"Warning: Could not load currency rates: {e}")
            return default_rates

    def save_currency_rates(self, rates):
        """Save currency rates to JSON file"""
        try:
            with open("data/currency.json", 'w') as f:
                json.dump(rates, f, indent=2)
            return True
        except Exception as e:
            display_error(f"Could not save currency rates: {e}")
            return False

    def simple_interest(self, principal, rate, time):
        """Calculate simple interest"""
        interest = (principal * rate * time) / 100
        total_amount = principal + interest
        return interest, total_amount

    def compound_interest(self, principal, rate, time, compounding_frequency=1):
        """Calculate compound interest"""
        # A = P(1 + r/n)^(nt)
        amount = principal * math.pow(1 + (rate / (100 * compounding_frequency)), 
                                     compounding_frequency * time)
        interest = amount - principal
        return interest, amount

    def emi_calculator(self, principal, rate, time):
        """Calculate Equated Monthly Installment (EMI)"""
        # Convert annual rate to monthly and time to months
        monthly_rate = rate / (12 * 100)
        months = time * 12

        # EMI formula: [P x R x (1+R)^N]/[(1+R)^N-1]
        if monthly_rate == 0:  # Handle 0% interest case
            emi = principal / months
        else:
            emi = (principal * monthly_rate * math.pow(1 + monthly_rate, months)) / (
                  math.pow(1 + monthly_rate, months) - 1)

        total_payment = emi * months
        total_interest = total_payment - principal

        return emi, total_interest, total_payment

    def gst_calculator(self, amount, gst_rate, calculation_type="add"):
        """Calculate GST amount"""
        if calculation_type == "add":
            gst_amount = (amount * gst_rate) / 100
            total_amount = amount + gst_amount
            return gst_amount, total_amount
        else:  # extract
            original_amount = (amount * 100) / (100 + gst_rate)
            gst_amount = amount - original_amount
            return gst_amount, original_amount

    def currency_converter(self, amount, from_currency, to_currency):
        """Convert currency using stored rates"""
        if from_currency not in self.currency_rates or to_currency not in self.currency_rates:
            raise ValueError("Invalid currency code")

        # Convert to USD first, then to target currency
        amount_in_usd = amount / self.currency_rates[from_currency]
        converted_amount = amount_in_usd * self.currency_rates[to_currency]

        return converted_amount

    def update_currency_rate(self, currency, rate):
        """Update currency exchange rate"""
        if currency not in self.currency_rates:
            raise ValueError("Currency not found")

        self.currency_rates[currency] = rate
        self.save_currency_rates(self.currency_rates)
        return True

    def run(self):
        """Run the financial calculator interface"""
        while True:
            print("\n" + "="*50)
            print("        FINANCIAL CALCULATOR")
            print("="*50)
            print("1. Simple Interest Calculator")
            print("2. Compound Interest Calculator")
            print("3. EMI Calculator")
            print("4. GST Calculator")
            print("5. Currency Converter")
            print("6. Manage Currency Rates")
            print("7. Back to Main Menu")
            print("="*50)

            try:
                choice = get_menu_choice(7)

                if choice == 1:
                    self.simple_interest_calculator()
                elif choice == 2:
                    self.compound_interest_calculator()
                elif choice == 3:
                    self.emi_calculator_interface()
                elif choice == 4:
                    self.gst_calculator_interface()
                elif choice == 5:
                    self.currency_converter_interface()
                elif choice == 6:
                    self.manage_currency_rates()
                elif choice == 7:
                    break

            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                break
            except Exception as e:
                display_error(str(e))

    def simple_interest_calculator(self):
        """Simple interest calculation interface"""
        print("\n--- Simple Interest Calculator ---")
        try:
            principal = get_numeric_input("Enter principal amount: ")
            rate = get_numeric_input("Enter annual interest rate (%): ")
            time = get_numeric_input("Enter time period (years): ")

            interest, total_amount = self.simple_interest(principal, rate, time)

            print(f"\nResults:")
            print(f"Principal: {principal:.2f}")
            print(f"Interest Rate: {rate}% per year")
            print(f"Time Period: {time} years")
            print(f"Interest Earned: {interest:.2f}")
            print(f"Total Amount: {total_amount:.2f}")

            # Add to history
            expression = f"SI: P={principal}, R={rate}%, T={time} years"
            self.history_manager.add_to_history(expression, total_amount)

        except ValueError as e:
            display_error(str(e))

    def compound_interest_calculator(self):
        """Compound interest calculation interface"""
        print("\n--- Compound Interest Calculator ---")
        try:
            principal = get_numeric_input("Enter principal amount: ")
            rate = get_numeric_input("Enter annual interest rate (%): ")
            time = get_numeric_input("Enter time period (years): ")
            compounding = get_numeric_input("Enter compounding frequency per year (1 for annual, 12 for monthly): ", default=1)

            interest, total_amount = self.compound_interest(principal, rate, time, compounding)

            print(f"\nResults:")
            print(f"Principal: {principal:.2f}")
            print(f"Interest Rate: {rate}% per year")
            print(f"Time Period: {time} years")
            print(f"Compounding: {compounding} times per year")
            print(f"Interest Earned: {interest:.2f}")
            print(f"Total Amount: {total_amount:.2f}")

            # Add to history
            expression = f"CI: P={principal}, R={rate}%, T={time} years, N={compounding}"
            self.history_manager.add_to_history(expression, total_amount)

        except ValueError as e:
            display_error(str(e))

    def emi_calculator_interface(self):
        """EMI calculation interface"""
        print("\n--- EMI Calculator ---")
        try:
            principal = get_numeric_input("Enter loan amount: ")
            rate = get_numeric_input("Enter annual interest rate (%): ")
            time = get_numeric_input("Enter loan tenure (years): ")

            emi, total_interest, total_payment = self.emi_calculator(principal, rate, time)

            print(f"\nResults:")
            print(f"Loan Amount: {principal:.2f}")
            print(f"Interest Rate: {rate}% per year")
            print(f"Loan Tenure: {time} years")
            print(f"Monthly EMI: {emi:.2f}")
            print(f"Total Interest Payable: {total_interest:.2f}")
            print(f"Total Payment: {total_payment:.2f}")

            # Add to history
            expression = f"EMI: Loan={principal}, Rate={rate}%, Time={time} years"
            self.history_manager.add_to_history(expression, emi)

        except ValueError as e:
            display_error(str(e))

    def gst_calculator_interface(self):
        """GST calculation interface"""
        print("\n--- GST Calculator ---")
        print("1. Add GST to amount")
        print("2. Extract GST from amount")

        try:
            choice = get_menu_choice(2)
            amount = get_numeric_input("Enter amount: ")
            gst_rate = get_numeric_input("Enter GST rate (%): ")

            if choice == 1:
                gst_amount, total_amount = self.gst_calculator(amount, gst_rate, "add")
                print(f"\nResults:")
                print(f"Original Amount: {amount:.2f}")
                print(f"GST Rate: {gst_rate}%")
                print(f"GST Amount: {gst_amount:.2f}")
                print(f"Total Amount: {total_amount:.2f}")

                expression = f"GST Add: Amount={amount}, Rate={gst_rate}%"
                self.history_manager.add_to_history(expression, total_amount)

            else:
                gst_amount, original_amount = self.gst_calculator(amount, gst_rate, "extract")
                print(f"\nResults:")
                print(f"Total Amount: {amount:.2f}")
                print(f"GST Rate: {gst_rate}%")
                print(f"GST Amount: {gst_amount:.2f}")
                print(f"Original Amount: {original_amount:.2f}")

                expression = f"GST Extract: Amount={amount}, Rate={gst_rate}%"
                self.history_manager.add_to_history(expression, original_amount)

        except ValueError as e:
            display_error(str(e))

    def currency_converter_interface(self):
        """Currency conversion interface"""
        print("\n--- Currency Converter ---")
        print("Available currencies:", ", ".join(self.currency_rates.keys()))

        try:
            amount = get_numeric_input("Enter amount to convert: ")
            from_curr = input("Enter source currency code: ").upper().strip()
            to_curr = input("Enter target currency code: ").upper().strip()

            if from_curr not in self.currency_rates or to_curr not in self.currency_rates:
                raise ValueError("Invalid currency code. Available currencies: " + ", ".join(self.currency_rates.keys()))

            converted_amount = self.currency_converter(amount, from_curr, to_curr)

            print(f"\nResult:")
            print(f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}")

            # Add to history
            expression = f"Currency: {amount} {from_curr} to {to_curr}"
            self.history_manager.add_to_history(expression, converted_amount)

        except ValueError as e:
            display_error(str(e))

    def manage_currency_rates(self):
        """Manage currency exchange rates"""
        print("\n--- Manage Currency Rates ---")
        print("Current rates (based on USD):")
        for currency, rate in self.currency_rates.items():
            print(f"{currency}: {rate}")

        print("\n1. Update exchange rate")
        print("2. Back to financial calculator")

        try:
            choice = get_menu_choice(2)

            if choice == 1:
                currency = input("Enter currency code to update: ").upper().strip()
                if currency not in self.currency_rates:
                    raise ValueError("Currency not found")

                new_rate = get_numeric_input(f"Enter new exchange rate for {currency} (1 USD = ? {currency}): ")

                success = self.update_currency_rate(currency, new_rate)
                if success:
                    print(f"Exchange rate for {currency} updated successfully!")
                    input("Press Enter to continue...")

        except ValueError as e:
            display_error(str(e))


if __name__ == "__main__":
    # For testing without the full app
    from history import HistoryManager
    hm = HistoryManager()
    calc = FinancialCalculator(hm)
    calc.run()
