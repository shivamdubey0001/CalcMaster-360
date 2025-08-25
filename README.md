# CalcMaster 360 🚀

Hey there! 👋 I'm **Shivam Dubey** and I'm excited to share my awesome calculator project with you all!

## What is CalcMaster 360?

CalcMaster 360 is not just any ordinary calculator - it's a **smart, multi-functional calculator** that can handle everything from basic math to complex scientific calculations, financial planning, and unit conversions. Think of it as your personal math assistant that never gets tired!

I built this because I was tired of using different apps for different calculations. Why not have everything in one place, right?

## What makes it special?

Here's what makes CalcMaster 360 stand out:

- **4 Different Calculator Modes** - Basic, Scientific, Financial, and Unit Converter
- **Smart History** - Remembers all your calculations so you never lose track
- **Favorites System** - Save your frequently used calculations for quick access  
- **Dark/Light Mode** - Easy on the eyes, day or night
- **Error-Proof** - Won't crash if you make a mistake (we all do!)
- **User-Friendly Interface** - Simple menus that anyone can understand

## What you need to run this

Don't worry, you don't need much! Just make sure you have:

- **Python 3.6 or higher** (most computers already have this)
- A terminal or command prompt
- That's it! No complicated setup required

## How to get started

Getting CalcMaster 360 running is super easy:

### Step 1: Download the project
```bash
git clone https://github.com/shivamdubey0001/CalcMaster-360
cd CalcMaster360
```

### Step 2: Run the calculator
```bash
python main.py
```

And boom! 💥 Your calculator is ready to use!

## How to use it

Once you run the program, you'll see a beautiful menu like this:

```
          🚀 CALCMASTER 360 🚀
==================================================
1.  Basic Calculator
2.  Scientific Calculator  
3.  Financial Calculator
4.  Unit Converter
5.  View Calculation History
6.  Favorites
7.  Toggle Dark/Light Mode
8.  Help
9.  Exit
==================================================
```

Just type the number of what you want to do and press Enter!

### The Different Modes

**1. Basic Calculator** 🧮
- Add, subtract, multiply, divide
- Square roots, squares, percentages
- Perfect for everyday math

**2. Scientific Calculator** 🔬
- Trigonometry (sin, cos, tan)
- Logarithms and exponentials
- Advanced mathematical functions
- Great for students and professionals

**3. Financial Calculator** 💰
- Calculate simple and compound interest
- EMI calculator for loans
- Currency conversion
- GST and tax calculations

**4. Unit Converter** 📏
- Length conversions (cm, meters, miles)
- Weight conversions (kg, pounds)
- Temperature conversions (Celsius, Fahrenheit)
- Time conversions

**5. History** 📊
- See all your previous calculations
- Clear history when needed
- Never lose track of important calculations

**6. Favorites** ⭐
- Save calculations you use often
- Quick access to complex formulas
- Organize your work better

## What's inside the project

Let me show you what each file does in this project. I've organized everything properly so it's easy to understand:

### Main Program Files
- **main.py** - This is the heart of CalcMaster 360! It runs the main menu and connects all the different calculator modes together
- **basic_calc.py** - Handles all your everyday math like addition, subtraction, multiplication, division, and percentages
- **scientific_calc.py** - All the advanced math functions like trigonometry, logarithms, and complex calculations
- **finance_calc.py** - Money-related calculations like interest, EMI, loan calculations, and currency conversion
- **converter.py** - Converts units like meters to feet, kilograms to pounds, Celsius to Fahrenheit, etc.
- **history.py** - Keeps track of all your calculations so you can see what you did before
- **favorites.py** - Lets you save calculations you use often for quick access later
- **utils.py** - Helper functions that make the calculator work smoothly (like clearing screen, handling errors)

### Data Storage Files (in the data/ folder)

> **🤖 Special Note**: The data storage files in this project were created with the help of **DeepSeek.ai** - an AI assistant that helped me structure the JSON files properly and organize the data efficiently!

I've created a special `data/` folder to keep all the important information organized:

- **currency.json** ✨ **(Created with DeepSeek.ai help)** - This file stores currency exchange rates (like 1 USD = 83 INR). With AI assistance, I made sure the JSON structure is perfect so the financial calculator can convert between different currencies without needing internet
- **history.json** ✨ **(Created with DeepSeek.ai help)** - Every calculation you do gets saved here automatically. The AI helped me design the data format so it saves calculations efficiently and loads them quickly
- **favorites.json** ✨ **(Created with DeepSeek.ai help)** - When you mark a calculation as "favorite", it gets stored in this file. DeepSeek.ai helped me create the proper JSON structure to store and retrieve favorite formulas easily

### How AI helped me build this

I want to be transparent with you all - I used **DeepSeek.ai** as my coding assistant for the data management part of this project. Here's how:

- **JSON Structure Design**: DeepSeek.ai helped me create clean, efficient JSON formats for storing data
- **Data Organization**: The AI suggested the best ways to organize currency rates, calculation history, and favorites
- **Error Handling**: AI assistance helped me make sure the data files don't get corrupted if something goes wrong

This collaboration between human creativity (my ideas and logic) and AI assistance (proper data structuring) made the project much better than I could have built alone!

### Why I organized it this way
Instead of putting everything in one big messy file, I separated different features into different files. This makes the code:
- **Easier to understand** - Each file has one main job
- **Easier to fix** - If there's a problem with history, I know exactly where to look
- **Easier to add new features** - Want to add a new calculator mode? Just create a new file!

The `data/` folder keeps all your personal information separate from the program code. This means your data stays safe even if I update the calculator code.

## Common issues and solutions

**Problem**: "Python is not recognized as a command"
- **Solution**: Make sure Python is installed and added to your system PATH

**Problem**: Calculator closes unexpectedly
- **Solution**: Check if all the required files are in the same folder

**Problem**: Can't see the menu properly
- **Solution**: Try maximizing your terminal window

If you're still having trouble, don't hesitate to reach out!

## Want to make it even better?

I'd love your help! Here's how you can contribute:

1. **Fork** the project on GitHub
2. **Create a new branch** for your awesome feature
3. **Make your changes** (add new features, fix bugs, improve design)
4. **Test everything** to make sure it works
5. **Submit a pull request** 

Even small improvements like fixing typos or adding comments are super helpful!

## Technologies used

This project is built with:
- **Python** - The main programming language
- **JSON** - For storing history and favorites data
- **Built-in Python libraries** - No external dependencies needed!

## Cool features coming soon

I'm working on adding these exciting features:

- **Graphing calculator** - Visualize mathematical functions
- **Unit conversion API** - Real-time exchange rates
- **Voice commands** - Calculate by speaking
- **Export calculations** - Save results to PDF or Excel
- **Custom themes** - More color options

## Fun facts about this project

- **Lines of code**: Over 500 lines of pure Python magic!
- **Development time**: Built over several weekends
- **Tested by**: My friends who always need help with math 😄
- **Favorite feature**: The history system - I never lose my calculations now!

## A personal note

Building CalcMaster 360 has been an amazing journey. I started with just a simple calculator idea, but it grew into something much bigger and more useful. Every feature was added because I or my friends needed it in real life.

If you find any bugs or have suggestions for new features, please let me know! I'm always learning and your feedback helps me become a better programmer.

## License

This project is open source and free for everyone to use, modify, and share. Feel free to make it your own!

---

**Thanks for checking out CalcMaster 360!** If you like this project, please give it a ⭐ on GitHub. It really motivates me to keep building cool stuff!

*Made with ❤️ and lots of ☕ by Shivam Dubey*

---

*P.S. - If you spot any mistakes or think something could be explained better, please let me know! I'm always trying to improve and make things clearer for everyone.*
