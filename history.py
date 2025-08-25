
import json
import os
from datetime import datetime

class HistoryManager:
    def __init__(self, filename="data/history.json"):
        self.filename = filename
        self.history = []
        self.load_history()

    def load_history(self):
        """Load calculation history from JSON file"""
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)

            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.history = json.load(f)
            else:
                # Create empty history file
                self.save_history()

        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load history file: {e}")
            self.history = []

    def save_history(self):
        """Save calculation history to JSON file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.history, f, indent=2)
            return True
        except IOError as e:
            print(f"Error: Could not save history file: {e}")
            return False

    def add_to_history(self, calculation, result):
        """Add a calculation to history with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        history_entry = {
            "timestamp": timestamp,
            "calculation": str(calculation),
            "result": str(result)
        }

        # Add to beginning of list (most recent first)
        self.history.insert(0, history_entry)

        # Keep only last 100 entries to prevent file from growing too large
        if len(self.history) > 100:
            self.history = self.history[:100]

        # Save to file
        self.save_history()

        return history_entry

    def get_history(self, limit=None):
        """Get calculation history, optionally limited to recent entries"""
        if limit is None or limit >= len(self.history):
            return self.history.copy()
        return self.history[:limit]

    def clear_history(self):
        """Clear all calculation history"""
        self.history = []
        return self.save_history()

    def search_history(self, search_term):
        """Search history for calculations containing search term"""
        search_term = search_term.lower()
        results = []

        for entry in self.history:
            if (search_term in entry["calculation"].lower() or 
                search_term in entry["result"].lower() or
                search_term in entry["timestamp"].lower()):
                results.append(entry)

        return results

    def export_history(self, export_format="txt", filename=None):
        """Export history to file in various formats"""
        if not self.history:
            return False, "No history to export"

        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"calc_history_{timestamp}.{export_format}"

        try:
            if export_format == "txt":
                with open(filename, 'w') as f:
                    f.write("CalcMaster 360 - Calculation History\n")
                    f.write("=" * 50 + "\n\n")
                    for entry in self.history:
                        f.write(f"{entry['timestamp']}: {entry['calculation']} = {entry['result']}\n")

            elif export_format == "csv":
                with open(filename, 'w') as f:
                    f.write("Timestamp,Calculation,Result\n")
                    for entry in self.history:
                        # Escape commas in values
                        calc = entry['calculation'].replace(',', ';')
                        result = entry['result'].replace(',', ';')
                        f.write(f"{entry['timestamp']},{calc},{result}\n")

            elif export_format == "json":
                with open(filename, 'w') as f:
                    json.dump(self.history, f, indent=2)

            else:
                return False, f"Unsupported export format: {export_format}"

            return True, f"History exported to {filename}"

        except IOError as e:
            return False, f"Could not export history: {e}"

    def get_stats(self):
        """Get statistics about calculation history"""
        if not self.history:
            return {"total_calculations": 0}

        # Count calculations by type
        type_count = {}
        for entry in self.history:
            calc = entry["calculation"].lower()

            if any(op in calc for op in ["+", "-", "*", "/", "basic"]):
                calc_type = "basic"
            elif any(op in calc for op in ["sin", "cos", "tan", "log", "scientific"]):
                calc_type = "scientific"
            elif any(op in calc for op in ["interest", "emi", "gst", "currency", "financial"]):
                calc_type = "financial"
            elif "convert" in calc:
                calc_type = "conversion"
            else:
                calc_type = "other"

            type_count[calc_type] = type_count.get(calc_type, 0) + 1

        return {
            "total_calculations": len(self.history),
            "calculations_by_type": type_count,
            "first_calculation": self.history[-1]["timestamp"] if self.history else None,
            "last_calculation": self.history[0]["timestamp"] if self.history else None
        }


if __name__ == "__main__":
    # Test the HistoryManager
    hm = HistoryManager("test_history.json")

    # Add some test entries
    hm.add_to_history("2 + 2", 4)
    hm.add_to_history("sin(45)", 0.7071)
    hm.add_to_history("100 USD to EUR", 85.0)

    # Display history
    print("Calculation History:")
    for entry in hm.get_history():
        print(f"{entry['timestamp']}: {entry['calculation']} = {entry['result']}")

    # Test search
    print("\nSearch results for 'USD':")
    results = hm.search_history("USD")
    for entry in results:
        print(f"{entry['timestamp']}: {entry['calculation']}")

    # Test stats
    stats = hm.get_stats()
    print(f"\nStatistics: {stats}")

    # Test export
    success, message = hm.export_history("txt", "test_export.txt")
    print(f"Export: {message}")

    # Clean up test files
    if os.path.exists("test_history.json"):
        os.remove("test_history.json")
    if os.path.exists("test_export.txt"):
        os.remove("test_export.txt")

    print("Test completed successfully!")
