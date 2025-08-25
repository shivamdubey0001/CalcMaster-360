# main.py - Entry point for CalcMaster 360
import os
import sys
from datetime import datetime

# Import our custom modules
from basic_calc import BasicCalculator
from scientific_calc import ScientificCalculator
from finance_calc import FinancialCalculator
from converter import UnitConverter
from history import HistoryManager
from favorites import FavoritesManager
from utils import clear_screen, get_numeric_input, get_menu_choice, display_error

class CalcMaster360:
    def __init__(self):
        self.history_manager = HistoryManager()
        self.favorites_manager = FavoritesManager()
        self.basic_calc = BasicCalculator(self.history_manager)
        self.scientific_calc = ScientificCalculator(self.history_manager)
        self.finance_calc = FinancialCalculator(self.history_manager)
        self.converter = UnitConverter(self.history_manager)

        # Initialize with light mode by default
        self.dark_mode = False

    def toggle_dark_mode(self):
        """Toggle between dark and light mode"""
        self.dark_mode = not self.dark_mode
        mode = "Dark" if self.dark_mode else "Light"
        print(f"\n{mode} mode enabled!")

    def display_main_menu(self):
        """Display the main menu options"""
        print("\n" + "="*50)
        print("          🚀 CALCMASTER 360 🚀")
        print("="*50)
        print("1.  Basic Calculator")
        print("2.  Scientific Calculator")
        print("3.  Financial Calculator")
        print("4.  Unit Converter")
        print("5.  View Calculation History")
        print("6.  Favorites")
        print("7.  Toggle Dark/Light Mode")
        print("8.  Help")
        print("9.  Exit")
        print("="*50)

    def show_help(self):
        """Display help information"""
        clear_screen()
        print("\n" + "="*60)
        print("                   HELP & INFORMATION")
        print("="*60)
        print("CalcMaster 360 is a multi-functional calculator with")
        print("various modes to suit your calculation needs.")
        print("\nFEATURES:")
        print("- Basic: Standard arithmetic operations")
        print("- Scientific: Trig, log, exponents, and more")
        print("- Financial: Interest, EMI, currency conversion")
        print("- Converter: Unit conversions for length, weight, etc.")
        print("- History: View your past calculations")
        print("- Favorites: Save frequently used calculations")
        print("\nNAVIGATION:")
        print("- Use numbers to select menu options")
        print("- Follow prompts for inputs")
        print("- Type 'back' or 'menu' to return to previous screens")
        print("="*60)
        input("\nPress Enter to return to main menu...")

    def run_basic_mode(self):
        """Run the basic calculator mode"""
        self.basic_calc.run()

    def run_scientific_mode(self):
        """Run the scientific calculator mode"""
        self.scientific_calc.run()

    def run_financial_mode(self):
        """Run the financial calculator mode"""
        self.finance_calc.run()

    def run_conversion_mode(self):
        """Run the unit conversion mode"""
        self.converter.run()

    def view_history(self):
        """View calculation history"""
        clear_screen()
        print("\n" + "="*50)
        print("          CALCULATION HISTORY")
        print("="*50)

        history = self.history_manager.get_history()

        if not history:
            print("No calculations in history yet.")
            input("\nPress Enter to return to main menu...")
            return

        for i, entry in enumerate(history, 1):
            print(f"{i}. {entry['timestamp']} - {entry['calculation']} = {entry['result']}")

        print("\nOptions:")
        print("1. Clear History")
        print("2. Back to Main Menu")

        choice = get_menu_choice(2)

        if choice == 1:
            self.history_manager.clear_history()
            print("History cleared!")
            input("Press Enter to continue...")

    def manage_favorites(self):
        """Manage favorite calculations"""
        while True:
            clear_screen()
            print("\n" + "="*50)
            print("               FAVORITES")
            print("="*50)
            print("1. View Favorites")
            print("2. Add Current Calculation to Favorites")
            print("3. Remove from Favorites")
            print("4. Back to Main Menu")

            choice = get_menu_choice(4)

            if choice == 1:
                self.view_favorites()
            elif choice == 2:
                self.add_to_favorites()
            elif choice == 3:
                self.remove_from_favorites()
            elif choice == 4:
                break

    def view_favorites(self):
        """View favorite calculations"""
        favorites = self.favorites_manager.get_favorites()

        if not favorites:
            print("No favorites saved yet.")
            input("\nPress Enter to continue...")
            return

        print("\nYour Favorite Calculations:")
        for i, fav in enumerate(favorites, 1):
            print(f"{i}. {fav['name']}: {fav['expression']}")

        print("\nSelect a favorite to use or 0 to go back:")
        choice = get_menu_choice(len(favorites), allow_zero=True)

        if choice == 0:
            return

        selected_fav = favorites[choice-1]
        expression = selected_fav['expression']

        # Use the appropriate calculator based on the expression type
        if any(op in expression for op in ['sin', 'cos', 'tan', 'log', 'ln']):
            result = self.scientific_calc.evaluate_expression(expression)
        elif any(op in expression for op in ['EMI', 'interest', 'currency']):
            # This would need more sophisticated detection
            result = self.finance_calc.evaluate_expression(expression)
        else:
            result = self.basic_calc.evaluate_expression(expression)

        print(f"\nResult: {result}")
        input("\nPress Enter to continue...")

    def add_to_favorites(self):
        """Add a calculation to favorites"""
        # Get the last calculation from history
        history = self.history_manager.get_history()

        if not history:
            print("No recent calculations to add to favorites.")
            input("\nPress Enter to continue...")
            return

        last_calc = history[-1]
        calculation = f"{last_calc['calculation']} = {last_calc['result']}"

        print(f"Recent calculation: {calculation}")
        name = input("Enter a name for this favorite: ").strip()

        if not name:
            print("Favorite name cannot be empty.")
            input("\nPress Enter to continue...")
            return

        self.favorites_manager.add_favorite(name, last_calc['calculation'])
        print("Favorite added successfully!")
        input("\nPress Enter to continue...")

    def remove_from_favorites(self):
        """Remove a calculation from favorites"""
        favorites = self.favorites_manager.get_favorites()

        if not favorites:
            print("No favorites to remove.")
            input("\nPress Enter to continue...")
            return

        print("\nSelect a favorite to remove:")
        for i, fav in enumerate(favorites, 1):
            print(f"{i}. {fav['name']}: {fav['expression']}")

        print("0. Cancel")
        choice = get_menu_choice(len(favorites), allow_zero=True)

        if choice == 0:
            return

        removed = self.favorites_manager.remove_favorite(choice-1)
        print(f"Removed: {removed['name']}")
        input("\nPress Enter to continue...")

    def run(self):
        """Main application loop"""
        clear_screen()

        while True:
            clear_screen()
            self.display_main_menu()

            try:
                choice = get_menu_choice(9)

                if choice == 1:
                    self.run_basic_mode()
                elif choice == 2:
                    self.run_scientific_mode()
                elif choice == 3:
                    self.run_financial_mode()
                elif choice == 4:
                    self.run_conversion_mode()
                elif choice == 5:
                    self.view_history()
                elif choice == 6:
                    self.manage_favorites()
                elif choice == 7:
                    self.toggle_dark_mode()
                elif choice == 8:
                    self.show_help()
                elif choice == 9:
                    print("\nThank you for using CalcMaster 360! Goodbye! 👋")
                    sys.exit(0)

            except KeyboardInterrupt:
                print("\n\nOperation cancelled. Returning to main menu...")
                input("Press Enter to continue...")
            except Exception as e:
                display_error(f"An unexpected error occurred: {str(e)}")
                input("Press Enter to continue...")

# Run the application
if __name__ == "__main__":
    app = CalcMaster360()
    app.run()