import os
import sys
import math
from datetime import datetime

def clear_screen():
"""Clear the terminal screen"""
# For Windows
if os.name == 'nt':
os.system('cls')
# For Unix/Linux/MacOS
else:
os.system('clear')

def get_numeric_input(prompt, default=None, allow_negative=True):
"""
Get numeric input from user with validation

text
Args:
    prompt (str): The input prompt to display
    default: Default value if user enters nothing
    allow_negative (bool): Whether to allow negative numbers

Returns:
    float: The validated numeric input
"""
while True:
    try:
        user_input = input(prompt).strip()

        # Allow empty input if default is provided
        if not user_input and default is not None:
            return default

        # Check for special commands
        if user_input.lower() in ['back', 'exit', 'menu', 'quit']:
            raise KeyboardInterrupt("Returning to menu")

        # Convert to float
        value = float(user_input)

        # Check for negative values if not allowed
        if not allow_negative and value < 0:
            print("Please enter a non-negative number.")
            continue

        return value

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        raise
def get_menu_choice(max_option, allow_zero=False):
"""
Get a menu choice from user with validation

text
Args:
    max_option (int): Maximum valid option number
    allow_zero (bool): Whether to allow 0 as a valid choice

Returns:
    int: The validated menu choice
"""
min_option = 0 if allow_zero else 1

while True:
    try:
        choice = input(f"Enter your choice ({min_option}-{max_option}): ").strip()

        # Check for special commands
        if choice.lower() in ['back', 'exit', 'menu', 'quit']:
            raise KeyboardInterrupt("Returning to menu")

        choice_num = int(choice)

        if min_option <= choice_num <= max_option:
            return choice_num
        else:
            print(f"Please enter a number between {min_option} and {max_option}.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        raise
def display_error(message):
"""
Display an error message in a consistent format

text
Args:
    message (str): The error message to display
"""
print(f"\n❌ Error: {message}")
print("Please try again.")
def display_success(message):
"""
Display a success message in a consistent format

text
Args:
    message (str): The success message to display
"""
print(f"\n✅ {message}")
def format_number(number, precision=6):
"""
Format a number for display, removing unnecessary decimal places

text
Args:
    number (float): The number to format
    precision (int): Maximum number of decimal places

Returns:
    str: Formatted number string
"""
if number is None:
    return "N/A"

# Check if it's a whole number
if number == int(number):
    return str(int(number))

# Format with appropriate precision
formatted = f"{number:.{precision}f}"

# Remove trailing zeros and decimal point if not needed
if '.' in formatted:
    formatted = formatted.rstrip('0').rstrip('.')

return formatted
def confirm_action(prompt="Are you sure you want to continue?"):
"""
Ask user for confirmation before proceeding

text
Args:
    prompt (str): The confirmation prompt

Returns:
    bool: True if user confirms, False otherwise
"""
while True:
    response = input(f"{prompt} (y/n): ").strip().lower()

    if response in ['y', 'yes']:
        return True
    elif response in ['n', 'no']:
        return False
    else:
        print("Please enter 'y' for yes or 'n' for no.")
def get_valid_filename(name):
"""
Convert a string to a valid filename

text
Args:
    name (str): The original filename

Returns:
    str: Valid filename
"""
# Replace invalid characters with underscores
invalid_chars = '<>:"/\\|?*'
for char in invalid_chars:
    name = name.replace(char, '_')

# Remove leading/trailing spaces and dots
name = name.strip().strip('.')

# Ensure filename is not empty
if not name:
    name = 'untitled'

return name
def format_timestamp(timestamp=None, format_str="%Y-%m-%d %H:%M:%S"):
"""
Format a timestamp for display

text
Args:
    timestamp: datetime object or None for current time
    format_str: Format string for datetime

Returns:
    str: Formatted timestamp
"""
if timestamp is None:
    timestamp = datetime.now()

if isinstance(timestamp, str):
    # Try to parse if it's a string
    try:
        timestamp = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
    except ValueError:
        return timestamp  # Return original if can't parse

return timestamp.strftime(format_str)
def progress_bar(iteration, total, length=50, prefix='Progress:', suffix='Complete'):
"""
Display a progress bar in the console

text
Args:
    iteration (int): Current iteration
    total (int): Total iterations
    length (int): Character length of bar
    prefix (str): Prefix text
    suffix (str): Suffix text
"""
percent = ("{0:.1f}").format(100 * (iteration / float(total)))
filled_length = int(length * iteration // total)
bar = '█' * filled_length + '░' * (length - filled_length)
print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')

# Print new line when complete
if iteration == total:
    print()
def safe_divide(numerator, denominator):
"""
Safe division that handles division by zero

text
Args:
    numerator: The numerator
    denominator: The denominator

Returns:
    float: Result of division or 0 if denominator is 0
"""
if denominator == 0:
    return 0
return numerator / denominator
def is_valid_email(email):
"""
Basic email validation

text
Args:
    email (str): Email address to validate

Returns:
    bool: True if email appears valid
"""
if not email or '@' not in email or '.' not in email:
    return False
return True
def get_input_with_default(prompt, default):
"""
Get input from user with a default value

text
Args:
    prompt (str): The input prompt
    default: Default value

Returns:
    str: User input or default
"""
response = input(f"{prompt} [{default}]: ").strip()
return response if response else default
def pause():
"""Pause execution and wait for user to press Enter"""
input("\nPress Enter to continue...")

def format_file_size(size_bytes):
"""
Convert file size in bytes to human-readable format

Args:
    size_bytes (int): Size in bytes

Returns:
    str: Human-readable file size
"""
if size_bytes == 0:
    return "0 bytes"

size_names = ["bytes", "KB", "MB", "GB"]
i = 0
size = float(size_bytes)

while size >= 1024 and i < len(size_names) - 1:
    size /= 1024
    i += 1

return f"{size:.2f} {size_names[i]}"
Example usage and testing
if name == "main":
# Test the utility functions
print("Testing utility functions...")

# Test numeric input
try:
    number = get_numeric_input("Enter a number: ", default=42)
    print(f"You entered: {number}")
except KeyboardInterrupt:
    print("Input cancelled")

# Test menu choice
try:
    choice = get_menu_choice(5)
    print(f"You chose option: {choice}")
except KeyboardInterrupt:
    print("Menu selection cancelled")

# Test formatting
test_numbers = [123, 45.0, 67.890, 123.456789]
for num in test_numbers:
    print(f"{num} -> {format_number(num)}")

# Test timestamp formatting
print(f"Current timestamp: {format_timestamp()}")

# Test progress bar
print("Progress bar test:")
for i in range(101):
    progress_bar(i, 100)
    import time
    time.sleep(0.02)

print("\nAll utility functions tested successfully!")
import os
import sys
from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_numeric_input(prompt, default=None):
    """Get numeric input from user with validation"""
    while True:
        try:
            user_input = input(prompt).strip()
            
            if not user_input and default is not None:
                return default
            
            if not user_input:
                raise ValueError("Input cannot be empty")
            
            # Try to convert to float first
            value = float(user_input)
            return value
            
        except ValueError:
            display_error("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            raise

def get_menu_choice(max_choice, allow_zero=False):
    """Get menu choice from user with validation"""
    min_choice = 0 if allow_zero else 1
    
    while True:
        try:
            choice = input(f"Enter your choice ({min_choice}-{max_choice}): ").strip()
            
            if not choice:
                raise ValueError("Please enter a choice")
            
            choice = int(choice)
            
            if choice < min_choice or choice > max_choice:
                raise ValueError(f"Choice must be between {min_choice} and {max_choice}")
            
            return choice
            
        except ValueError as e:
            display_error(str(e))
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            raise

def display_error(message):
    """Display error message in red color"""
    print(f"{Fore.RED}Error: {message}{Style.RESET_ALL}")

def display_success(message):
    """Display success message in green color"""
    print(f"{Fore.GREEN}Success: {message}{Style.RESET_ALL}")

def display_warning(message):
    """Display warning message in yellow color"""
    print(f"{Fore.YELLOW}Warning: {message}{Style.RESET_ALL}")

def display_info(message):
    """Display info message in blue color"""
    print(f"{Fore.BLUE}Info: {message}{Style.RESET_ALL}")

def format_number(value, decimal_places=2):
    """Format number for display"""
    if isinstance(value, float):
        if value.is_integer():
            return str(int(value))
        else:
            return f"{value:.{decimal_places}f}"
    return str(value)

def get_yes_no_input(prompt):
    """Get yes/no input from user"""
    while True:
        try:
            response = input(f"{prompt} (y/n): ").strip().lower()
            
            if response in ['y', 'yes', '1', 'true']:
                return True
            elif response in ['n', 'no', '0', 'false']:
                return False
            else:
                display_error("Please enter 'y' for yes or 'n' for no")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            raise

def pause_for_user():
    """Pause and wait for user to press Enter"""
    input("\nPress Enter to continue...")

def create_directory(path):
    """Create directory if it doesn't exist"""
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        display_error(f"Could not create directory '{path}': {e}")
        return False

def safe_divide(a, b):
    """Safely divide two numbers"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def validate_positive_number(value, name="Value"):
    """Validate that a number is positive"""
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return True

def validate_non_negative_number(value, name="Value"):
    """Validate that a number is non-negative"""
    if value < 0:
        raise ValueError(f"{name} cannot be negative")
    return True

def truncate_string(text, max_length=50):
    """Truncate string if it's too long"""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."

def print_separator(char="=", length=50):
    """Print a separator line"""
    print(char * length)

def print_header(title, char="=", length=50):
    """Print a formatted header"""
    print_separator(char, length)
    print(f"{title:^{length}}")
    print_separator(char, length)

def get_file_size(filepath):
    """Get file size in bytes"""
    try:
        return os.path.getsize(filepath)
    except OSError:
        return 0

def is_valid_filename(filename):
    """Check if filename is valid"""
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    return not any(char in filename for char in invalid_chars)

# Color constants
class Colors:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL

# Testing function
if __name__ == "__main__":
    print("Testing utils.py functions...")
    
    # Test numeric input
    try:
        num = get_numeric_input("Enter a test number: ", default=5)
        print(f"You entered: {num}")
    except KeyboardInterrupt:
        print("Test cancelled")
    
    # Test menu choice
    try:
        choice = get_menu_choice(3)
        print(f"You chose: {choice}")
    except KeyboardInterrupt:
        print("Test cancelled")
    
    # Test error display
    display_error("This is a test error")
    display_success("This is a test success")
    display_warning("This is a test warning")
    display_info("This is a test info")
    
    print("Utils test completed!")
