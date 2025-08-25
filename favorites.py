
import json
import os
from datetime import datetime

class FavoritesManager:
    def __init__(self, filename="data/favorites.json"):
        self.filename = filename
        self.favorites = []
        self.load_favorites()

    def load_favorites(self):
        """Load favorite calculations from JSON file"""
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)

            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.favorites = json.load(f)
            else:
                # Create empty favorites file
                self.save_favorites()

        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load favorites file: {e}")
            self.favorites = []

    def save_favorites(self):
        """Save favorite calculations to JSON file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.favorites, f, indent=2)
            return True
        except IOError as e:
            print(f"Error: Could not save favorites file: {e}")
            return False

    def add_favorite(self, name, expression, category="general"):
        """Add a calculation to favorites"""
        # Check if favorite with same name already exists
        for fav in self.favorites:
            if fav["name"].lower() == name.lower():
                return False, "A favorite with this name already exists"

        favorite_entry = {
            "name": name,
            "expression": expression,
            "category": category,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_used": None,
            "usage_count": 0
        }

        self.favorites.append(favorite_entry)
        self.save_favorites()
        return True, "Favorite added successfully"

    def remove_favorite(self, index):
        """Remove a favorite by index"""
        if index < 0 or index >= len(self.favorites):
            return None

        removed = self.favorites.pop(index)
        self.save_favorites()
        return removed

    def remove_favorite_by_name(self, name):
        """Remove a favorite by name"""
        for i, fav in enumerate(self.favorites):
            if fav["name"].lower() == name.lower():
                return self.remove_favorite(i)
        return None

    def get_favorites(self, category=None):
        """Get all favorites, optionally filtered by category"""
        if category is None:
            return self.favorites.copy()

        return [fav for fav in self.favorites if fav["category"].lower() == category.lower()]

    def get_categories(self):
        """Get list of all favorite categories"""
        categories = set()
        for fav in self.favorites:
            categories.add(fav["category"])
        return sorted(list(categories))

    def update_usage(self, name):
        """Update usage statistics for a favorite"""
        for fav in self.favorites:
            if fav["name"].lower() == name.lower():
                fav["last_used"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                fav["usage_count"] = fav.get("usage_count", 0) + 1
                self.save_favorites()
                return True
        return False

    def search_favorites(self, search_term):
        """Search favorites by name or expression"""
        search_term = search_term.lower()
        results = []

        for fav in self.favorites:
            if (search_term in fav["name"].lower() or 
                search_term in fav["expression"].lower() or
                search_term in fav["category"].lower()):
                results.append(fav)

        return results

    def edit_favorite(self, index, new_name=None, new_expression=None, new_category=None):
        """Edit an existing favorite"""
        if index < 0 or index >= len(self.favorites):
            return False, "Invalid favorite index"

        fav = self.favorites[index]

        if new_name is not None:
            # Check if new name conflicts with existing favorites
            for i, other_fav in enumerate(self.favorites):
                if i != index and other_fav["name"].lower() == new_name.lower():
                    return False, "A favorite with this name already exists"
            fav["name"] = new_name

        if new_expression is not None:
            fav["expression"] = new_expression

        if new_category is not None:
            fav["category"] = new_category

        self.save_favorites()
        return True, "Favorite updated successfully"

    def clear_favorites(self, category=None):
        """Clear all favorites, optionally by category"""
        if category is None:
            self.favorites = []
        else:
            self.favorites = [fav for fav in self.favorites if fav["category"].lower() != category.lower()]

        return self.save_favorites()

    def export_favorites(self, export_format="txt", filename=None):
        """Export favorites to file"""
        if not self.favorites:
            return False, "No favorites to export"

        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"calc_favorites_{timestamp}.{export_format}"

        try:
            if export_format == "txt":
                with open(filename, 'w') as f:
                    f.write("CalcMaster 360 - Favorite Calculations\n")
                    f.write("=" * 50 + "\n\n")
                    for fav in self.favorites:
                        f.write(f"Name: {fav['name']}\n")
                        f.write(f"Expression: {fav['expression']}\n")
                        f.write(f"Category: {fav['category']}\n")
                        f.write(f"Created: {fav['created']}\n")
                        f.write(f"Last Used: {fav.get('last_used', 'Never')}\n")
                        f.write(f"Usage Count: {fav.get('usage_count', 0)}\n")
                        f.write("-" * 30 + "\n")

            elif export_format == "csv":
                with open(filename, 'w') as f:
                    f.write("Name,Expression,Category,Created,Last Used,Usage Count\n")
                    for fav in self.favorites:
                        # Escape commas in values
                        name = fav['name'].replace(',', ';')
                        expression = fav['expression'].replace(',', ';')
                        category = fav['category'].replace(',', ';')
                        created = fav['created'].replace(',', ';')
                        last_used = fav.get('last_used', 'Never').replace(',', ';')
                        f.write(f"{name},{expression},{category},{created},{last_used},{fav.get('usage_count', 0)}\n")

            elif export_format == "json":
                with open(filename, 'w') as f:
                    json.dump(self.favorites, f, indent=2)

            else:
                return False, f"Unsupported export format: {export_format}"

            return True, f"Favorites exported to {filename}"

        except IOError as e:
            return False, f"Could not export favorites: {e}"

    def get_most_used(self, limit=5):
        """Get most frequently used favorites"""
        sorted_favorites = sorted(self.favorites, key=lambda x: x.get("usage_count", 0), reverse=True)
        return sorted_favorites[:limit]

    def get_recently_used(self, limit=5):
        """Get recently used favorites"""
        # Filter favorites that have been used at least once
        used_favorites = [fav for fav in self.favorites if fav.get("last_used") is not None]
        sorted_favorites = sorted(used_favorites, key=lambda x: x["last_used"], reverse=True)
        return sorted_favorites[:limit]


# Example usage and testing
if __name__ == "__main__":
    # Test the FavoritesManager
    fm = FavoritesManager("test_favorites.json")

    # Add some test favorites
    fm.add_favorite("Basic Addition", "5 + 3", "basic")
    fm.add_favorite("Square Root", "sqrt(25)", "scientific")
    fm.add_favorite("Currency Conversion", "100 USD to EUR", "financial")

    # Display favorites
    print("Favorite Calculations:")
    for i, fav in enumerate(fm.get_favorites(), 1):
        print(f"{i}. {fav['name']}: {fav['expression']} ({fav['category']})")

    # Test updating usage
    fm.update_usage("Basic Addition")

    # Test search
    print("\nSearch results for 'currency':")
    results = fm.search_favorites("currency")
    for fav in results:
        print(f"{fav['name']}: {fav['expression']}")

    # Test categories
    categories = fm.get_categories()
    print(f"\nCategories: {categories}")

    # Test export
    success, message = fm.export_favorites("txt", "test_favorites_export.txt")
    print(f"Export: {message}")

    # Clean up test files
    if os.path.exists("test_favorites.json"):
        os.remove("test_favorites.json")
    if os.path.exists("test_favorites_export.txt"):
        os.remove("test_favorites_export.txt")

    print("Test completed successfully!")
