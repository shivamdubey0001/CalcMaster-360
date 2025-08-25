
from utils import get_numeric_input, display_error, get_menu_choice

class UnitConverter:
    def __init__(self, history_manager):
        self.history_manager = history_manager

        # Conversion factors (base unit is the first one in each category)
        self.conversion_factors = {
            "length": {
                "meter": 1.0,
                "centimeter": 0.01,
                "millimeter": 0.001,
                "kilometer": 1000.0,
                "inch": 0.0254,
                "foot": 0.3048,
                "yard": 0.9144,
                "mile": 1609.34
            },
            "weight": {
                "kilogram": 1.0,
                "gram": 0.001,
                "milligram": 0.000001,
                "pound": 0.453592,
                "ounce": 0.0283495,
                "ton": 1000.0
            },
            "temperature": {
                # Special handling required for temperature
                "celsius": "celsius",
                "fahrenheit": "fahrenheit", 
                "kelvin": "kelvin"
            },
            "time": {
                "second": 1.0,
                "millisecond": 0.001,
                "minute": 60.0,
                "hour": 3600.0,
                "day": 86400.0,
                "week": 604800.0
            },
            "volume": {
                "liter": 1.0,
                "milliliter": 0.001,
                "gallon": 3.78541,
                "quart": 0.946353,
                "pint": 0.473176,
                "cup": 0.236588,
                "fluid_ounce": 0.0295735
            },
            "area": {
                "square_meter": 1.0,
                "square_kilometer": 1000000.0,
                "square_centimeter": 0.0001,
                "square_mile": 2589988.11,
                "square_foot": 0.092903,
                "square_inch": 0.00064516,
                "acre": 4046.86,
                "hectare": 10000.0
            }
        }

        # User-friendly display names
        self.display_names = {
            "meter": "Meter", "centimeter": "Centimeter", "millimeter": "Millimeter",
            "kilometer": "Kilometer", "inch": "Inch", "foot": "Foot", "yard": "Yard",
            "mile": "Mile", "kilogram": "Kilogram", "gram": "Gram", "milligram": "Milligram",
            "pound": "Pound", "ounce": "Ounce", "ton": "Ton", "celsius": "Celsius",
            "fahrenheit": "Fahrenheit", "kelvin": "Kelvin", "second": "Second",
            "millisecond": "Millisecond", "minute": "Minute", "hour": "Hour",
            "day": "Day", "week": "Week", "liter": "Liter", "milliliter": "Milliliter",
            "gallon": "Gallon", "quart": "Quart", "pint": "Pint", "cup": "Cup",
            "fluid_ounce": "Fluid Ounce", "square_meter": "Square Meter",
            "square_kilometer": "Square Kilometer", "square_centimeter": "Square Centimeter",
            "square_mile": "Square Mile", "square_foot": "Square Foot",
            "square_inch": "Square Inch", "acre": "Acre", "hectare": "Hectare"
        }

    def convert_length(self, value, from_unit, to_unit):
        """Convert length units"""
        return value * (self.conversion_factors["length"][from_unit] / 
                       self.conversion_factors["length"][to_unit])

    def convert_weight(self, value, from_unit, to_unit):
        """Convert weight units"""
        return value * (self.conversion_factors["weight"][from_unit] / 
                       self.conversion_factors["weight"][to_unit])

    def convert_temperature(self, value, from_unit, to_unit):
        """Convert temperature units"""
        # First convert to Celsius
        if from_unit == "celsius":
            celsius = value
        elif from_unit == "fahrenheit":
            celsius = (value - 32) * 5/9
        elif from_unit == "kelvin":
            celsius = value - 273.15

        # Then convert from Celsius to target unit
        if to_unit == "celsius":
            return celsius
        elif to_unit == "fahrenheit":
            return (celsius * 9/5) + 32
        elif to_unit == "kelvin":
            return celsius + 273.15

    def convert_time(self, value, from_unit, to_unit):
        """Convert time units"""
        return value * (self.conversion_factors["time"][from_unit] / 
                       self.conversion_factors["time"][to_unit])

    def convert_volume(self, value, from_unit, to_unit):
        """Convert volume units"""
        return value * (self.conversion_factors["volume"][from_unit] / 
                       self.conversion_factors["volume"][to_unit])

    def convert_area(self, value, from_unit, to_unit):
        """Convert area units"""
        return value * (self.conversion_factors["area"][from_unit] / 
                       self.conversion_factors["area"][to_unit])

    def convert_units(self, category, value, from_unit, to_unit):
        """Generic unit conversion method"""
        if category == "temperature":
            return self.convert_temperature(value, from_unit, to_unit)
        elif category == "length":
            return self.convert_length(value, from_unit, to_unit)
        elif category == "weight":
            return self.convert_weight(value, from_unit, to_unit)
        elif category == "time":
            return self.convert_time(value, from_unit, to_unit)
        elif category == "volume":
            return self.convert_volume(value, from_unit, to_unit)
        elif category == "area":
            return self.convert_area(value, from_unit, to_unit)
        else:
            raise ValueError("Invalid conversion category")

    def run(self):
        """Run the unit converter interface"""
        while True:
            print("\n" + "="*50)
            print("          UNIT CONVERTER")
            print("="*50)
            print("1. Length Converter")
            print("2. Weight Converter")
            print("3. Temperature Converter")
            print("4. Time Converter")
            print("5. Volume Converter")
            print("6. Area Converter")
            print("7. Back to Main Menu")
            print("="*50)

            try:
                choice = get_menu_choice(7)

                if choice == 1:
                    self.convert_interface("length")
                elif choice == 2:
                    self.convert_interface("weight")
                elif choice == 3:
                    self.convert_interface("temperature")
                elif choice == 4:
                    self.convert_interface("time")
                elif choice == 5:
                    self.convert_interface("volume")
                elif choice == 6:
                    self.convert_interface("area")
                elif choice == 7:
                    break

            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                break
            except Exception as e:
                display_error(str(e))

    def convert_interface(self, category):
        """Generic interface for unit conversion"""
        units = list(self.conversion_factors[category].keys())
        display_units = [self.display_names[unit] for unit in units]

        print(f"\n--- {category.upper()} CONVERTER ---")
        print("Available units:")

        for i, unit in enumerate(display_units, 1):
            print(f"{i}. {unit}")

        # Get source unit
        print(f"\nSelect source unit (1-{len(units)}):")
        from_index = get_menu_choice(len(units)) - 1
        from_unit = units[from_index]

        # Get target unit
        print(f"Select target unit (1-{len(units)}):")
        to_index = get_menu_choice(len(units)) - 1
        to_unit = units[to_index]

        # Get value to convert
        value = get_numeric_input(f"Enter value in {self.display_names[from_unit]}: ")

        try:
            # Perform conversion
            result = self.convert_units(category, value, from_unit, to_unit)

            # Display result
            print(f"\nResult:")
            print(f"{value} {self.display_names[from_unit]} = {result:.6f} {self.display_names[to_unit]}")

            # Add to history
            expression = f"Convert: {value} {from_unit} to {to_unit}"
            self.history_manager.add_to_history(expression, result)

        except ValueError as e:
            display_error(str(e))

    def quick_convert(self, value, from_unit, to_unit, category=None):
        """Quick conversion without user interface"""
        # Auto-detect category if not provided
        if category is None:
            for cat, units in self.conversion_factors.items():
                if from_unit in units and to_unit in units:
                    category = cat
                    break
            else:
                raise ValueError(f"Cannot find conversion from {from_unit} to {to_unit}")

        return self.convert_units(category, value, from_unit, to_unit)

    def get_available_units(self, category):
        """Get list of available units for a category"""
        return list(self.conversion_factors[category].keys())

    def get_available_categories(self):
        """Get list of available conversion categories"""
        return list(self.conversion_factors.keys())


if __name__ == "__main__":
    # For testing without the full app
    from history import HistoryManager
    hm = HistoryManager()
    converter = UnitConverter(hm)

    # Test conversion
    result = converter.quick_convert(100, "centimeter", "meter", "length")
    print(f"100 cm = {result} m")

    # Run interactive mode
    converter.run()
