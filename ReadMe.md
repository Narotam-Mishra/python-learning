
## 02 Python inner working (00:27:50)

==> python code  -------- python Interpreter ------> Byte Code (mostly hidden) --------> Python Virtual Machine (PVM)

- Step 1 - compiled to Byte Code (although python is Interpretered language, here compiled is just technical term)

- Byte Code - Byte Code is low level code which is Platform Independent (ByteCode is not machine code). It runs faster

#### `.pyc` --> It is compiled python (frozen Binaries)

- `__pycache__` is a directory that Python automatically creates to store compiled bytecode files (.pyc files) for faster program execution.

- When we run a Python script, the interpreter compiles your .py source files into bytecode and caches them in __pycache__ folders. This compilation step is skipped on subsequent runs if the source file hasn't changed, making our programs start faster.

- `hello_python.cpython-312.pyc` :- is the compiled bytecode version of your `hello_python.py` source file. It represent source change and Python Version

- Above file `hello_python.cpython-312.pyc` works only for imported files, not for top level files.

#### What `hello_python.cpython-312.pyc` represents:
- Compiled bytecode :- our Python source code translated into Python's intermediate bytecode format
- Version-specific: The "cpython-312" indicates it was compiled with CPython interpreter version 3.12
- Binary format: Contains low-level instructions that the Python virtual machine can execute directly

#### Key point :- This file `hello_python.cpython-312.pyc` is only created when your script is imported as a module by another script, not when you run it directly with python hello_python.py. For direct execution, Python compiles to memory without saving the .pyc file.

#### Facts about Python Virtual Machine (PVM) :-
- Code loop to iterate byte code
- Runtime engine
- Also known as `python interpreter`

#### Byte Code is not machine code, it is
- python specific interpretation,
- cypthon (standard implementation), jython, Inron python, stackless, pypy. These are different implementations of the Python programming language - alternative ways to run Python code with different underlying engines and features.

#### Key point: They all run the same Python code but use different underlying technologies, offering various performance characteristics and platform integrations. CPython remains the reference implementation that most people use.

#### Python Virtual Machine (PVM) :- The Python Virtual Machine (PVM) is the runtime engine that executes Python bytecode. It's the core component that actually runs your Python programs.

#### PVM is 
- An interpreter that reads and executes Python bytecode instructions
- Part of the Python interpreter (like CPython, PyPy, etc.)
- Acts as an abstraction layer between your code and the operating system

#### How PVM works:
- Python source code (.py) → compiled to bytecode (.pyc)
- PVM reads bytecode instructions one by one
- Executes each instruction (variable assignment, function calls, loops, etc.)

#### Example flow 
hello.py → bytecode → PVM → actual execution

#### How Python Works Internally (Detailed) - https://claude.ai/share/8b16fe6e-2be1-47c7-8b3b-7344745b286f

#### Python Execution model - https://claude.ai/share/dc253a1c-048b-48fb-9b67-4eb7a89cc260


## 03 Python in shell (00:46:36)

### Python shell is useful for :-
- Interactive Development
- Data Exploration
- Learning & Prototyping
- System Administration
- Calculator/Tool

## 04 Immutable and mutable in python (01:06:40)

### Immutable and Mutable are something that is related to memory reference in python

#### Mutable Objects - Can be changed after creation:

- Lists: [1, 2, 3] - can add, remove, or modify elements
- Dictionaries: {'a': 1} - can add, update, or delete key-value pairs
- Sets: {1, 2, 3} - can add or remove elements
- User-defined objects - attributes can be modified

#### Immutable Objects - Cannot be changed after creation:

- Strings: "hello" - operations create new strings
- Tuples: (1, 2, 3) - cannot modify elements
- Numbers: 42, 3.14 - operations create new values
- Frozen sets: frozenset({1, 2}) - immutable version of sets
- Booleans: True, False

- Why it matters: Affects how objects behave when passed to functions, assigned to variables, or used as dictionary keys (only immutable objects can be dict keys).

- Mutable objects can have side effects (modify original data)
- Immutable objects are safer - no unexpected changes
- Use immutable objects when you want to prevent accidental modifications

## 05 Python Data Types - Big Picture (01:23:48)

#### Data Types / Object Types

- Number : 1234, 3.14, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c, u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('demos.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True, False
- None: None
- Functions, modules, classes

- Advance: Decorators, Generators, Iterators, MetaProgramming

## 06 Internal working of python (01:54:35)

### Python Internals & Memory Management

- Python uses dynamic typing—variables don’t have types, but the objects they reference do.

- Objects (like numbers, strings, lists) live in memory, and variables are just references (pointers) to them.

- Reference Counting: Python tracks how many references an object has. When references drop to zero, the garbage collector reclaims memory.

- Optimization: Python caches small integers and strings for efficiency (e.g., 5 or "hello" may reuse the same memory).

### Mutable vs Immutable Objects
- Immutable (can’t change after creation): int, float, str, tuple
  - Changing them creates a new object.

### Mutable (can change in-place): list, dict, set
- Modifying them affects all references.

- Variable Assignment & References :- Assigning a variable (a = b) creates a reference, not a copy.

### To copy a list, use slicing (b = a[:]) or copy.copy().

#### `is` vs `==`
- `==` checks value equality.
- `is` checks memory identity (same object):

### Garbage Collection
- Python’s GC cleans up objects with zero references.
- Exception: Small integers/strings may linger for reuse.

### Behind-the-Scenes Optimization
- Python pre-allocates small integers (-5 to 256) for speed.
- Interning: Reuses immutable objects (like short strings) to save memory.

### Key Takeaways :-
- Variables are labels, not boxes. Objects live independently in memory.
- Mutable objects can lead to unexpected side effects if shared.
- Use copy() or slicing to avoid accidental reference sharing.

## 07 Numbers in depth in python (02:24:54)

### **1. Python Numbers & Operations**
- **Types**: Integers (`int`), floats (`float`), and complex numbers.
- **Basic Math Operations**:  
  - `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `**` (exponentiation), `%` (modulus/remainder).
  - Example: `2 ** 3` (8), `5 % 2` (1).
- **Precedence**: Use parentheses `()` to clarify order (e.g., `(x + y) * z`).

### **2. Type Handling & Precision**
- **Mixed Types**: Python auto-converts to higher precision (e.g., `int + float → float`).  
  - Avoid mixing types; explicitly convert:  
    ```python
    int(2.3)  # 2
    float(40) # 40.0
    ```
- **Large Numbers**: Python handles arbitrarily large integers (e.g., `2 ** 1000`).

### **3. Comparisons & Boolean Logic**
- **Operators**:  
  - `==` (equal), `!=` (not equal), `<` (less than), `>` (greater than), `<=`, `>=`.
  - **Chained Comparisons**:  
    ```python
    x < y < z  # Equivalent to (x < y) and (y < z)
    ```
- **Boolean Values**:  
  - `True` (1) and `False` (0) are treated as integers internally.  
  - Logical operators: `and` (both conditions), `or` (either condition).

### **4. Common Pitfalls**
- **Floating-Point Precision**:  
  ```python
  1 / 3  # 0.333... (use `round()` or format for display).
  ```
- **Operator Overloading**:  
  - `+` works for numbers (addition) and strings (concatenation).
- **Avoid Implicit Type Mixing**:  
  - Bad: `40 + 2.23` → Prefer explicit conversion (e.g., `float(40) + 2.23`).

### **5. Shortcuts & Best Practices**
- **Chained Assignments**:  
  ```python
  a = b = 10  # Both `a` and `b` reference the same `10`.
  ```
- **Copying Lists**:  
  ```python
  list2 = list1[:]  # Shallow copy (avoids shared references).
  ```
- **Readability**: Use parentheses for complex expressions to avoid ambiguity.

### **Python Numbers & Advanced Concepts Summary**

#### **1. Math Module & Number Operations**
- **`math` Library**:  
  - `math.floor(x)`: Rounds down to the nearest integer (e.g., `math.floor(3.5) → 3`, `math.floor(-3.5) → -4`).  
  - `math.trunc(x)`: Truncates toward zero (e.g., `math.trunc(2.8) → 2`, `math.trunc(-2.8) → -2`).  
  - Other functions: `sqrt()`, `pow()`, `ceil()`, etc.

#### **2. Precision Handling**
- **Large Numbers**: Python handles arbitrarily large integers (e.g., `999999999999999999 + 1` works perfectly).  
- **Floating-Point Precision**:  
  ```python
  1 / 3  # 0.3333333333333333 (use `round()` or `decimal` module for exact precision).
  ```

#### **3. Complex Numbers**
- Represented as `a + bj` (e.g., `2 + 1j`).  
- Operations:  
  ```python
  (2 + 1j) * 3  # (6 + 3j)
  ```

#### **4. Number Systems & Conversions**
- **Binary**: Prefix `0b` (e.g., `0b1010` → `10`).  
- **Octal**: Prefix `0o` (e.g., `0o20` → `16`).  
- **Hexadecimal**: Prefix `0x` (e.g., `0xFF` → `255`).  
- **Conversions**:  
  ```python
  bin(64)  # '0b1000000'
  oct(64)  # '0o100'
  hex(64)  # '0x40'
  int('64', 8)  # Convert from base-8 → 52
  ```

#### **5. Bitwise Operations**
- **Left Shift (`<<`)**: `x << n` (equivalent to `x * (2 ** n)`).  
  ```python
  1 << 2  # 4 (binary: 0100)
  ```
- **Right Shift (`>>`)**: `x >> n` (equivalent to `x // (2 ** n)`).  
- **Bitwise AND/OR/XOR**:  
  ```python
  5 & 3  # AND → 1
  5 | 3  # OR → 7
  ```

### **1. Random Module**
- **`random.random()`**: Generates a float between 0.0 and 1.0.  
- **`random.randint(a, b)`**: Returns a random integer between `a` and `b` (inclusive).  
  ```python
  random.randint(1, 100)  # Random number between 1-100
  ```
- **`random.choice(seq)`**: Picks a random element from a sequence (list, tuple, etc.).  
  ```python
  random.choice(["tea", "coffee", "milk"])  # Random item
  ```
- **`random.shuffle(seq)`**: Shuffles a sequence in-place.  
  ```python
  cards = ["Spade", "Heart", "Diamond"]  
  random.shuffle(cards)  # Shuffles the list
  ```

### **2. Decimal Precision**
- **Issue**: Floating-point arithmetic can be imprecise.  
  ```python
  0.1 + 0.1 + 0.1 - 0.3  # Returns 5.551115123125783e-17 (not 0.0)
  ```
- **Solution**: Use the `decimal` module for exact precision.  
  ```python
  from decimal import Decimal
  Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')  # Returns 0.0
  ```

### **3. Fractions**
- **`fractions.Fraction`**: Handles fractional arithmetic.  
  ```python
  from fractions import Fraction
  Fraction(2, 7)  # Represents 2/7
  ```

### **4. Sets**
- **Definition**: Unordered, unique elements.  
  ```python
  set1 = {1, 2, 3, 4}
  set2 = {1, 3}
  ```
- **Operations**:  
  - **Union (`|`)**: `set1 | set2` → `{1, 2, 3, 4}`  
  - **Intersection (`&`)**: `set1 & set2` → `{1, 3}`  
  - **Difference (`-`)**: `set1 - set2` → `{2, 4}`  
- **Empty Set**: Use `set()` (not `{}`, which is a dict).  

### **5. Booleans**
- **Values**: `True` (1) and `False` (0).  
- **Truthy/Falsy**:  
  ```python
  bool(1)  # True
  bool(0)  # False
  ```
- **Comparison**:  
  ```python
  True == 1  # True
  False == 0  # True
  True is 1  # False (different objects)
  ```

### **Key Takeaways**
- Python dynamically handles types but **explicit is better than implicit**.
- **Comparisons** return `True`/`False` (treated as `1`/`0`).
- **Precision matters**: Use `round()`, `int()`, or `float()` as needed.
- **Best Practice**: Write clear, readable code (e.g., avoid `x < y < z` in favor of explicit `and`).

#### **Key Takeaways**
- **Precision**: Use `math` or `decimal` modules for exact calculations.  
- **Number Systems**: Python supports binary, octal, and hexadecimal natively.  
- **Complex Numbers**: Handled via `a + bj` notation.  
- **Bitwise Ops**: Useful for low-level optimizations (rare in everyday code).  

### **When to Use What?**
- **General Math**: Built-in operators (`+`, `-`, `**`).  
- **Precision**: `decimal` module.  
- **Advanced Math**: `math` or `numpy`.  
- **Bit Manipulation**: Bitwise operators (`<<`, `>>`, `&`, `|`). 

### **Key Takeaways**
- **Random**: Use `random` for games, simulations, and shuffling.  
- **Precision**: For financial/math-critical apps, use `decimal`.  
- **Fractions**: Useful for exact fractional representations.  
- **Sets**: Ideal for uniqueness checks and set operations.  
- **Booleans**: Internally treated as `1`/`0` but are distinct objects.  

## 08 Strings in python (03:12:43)

### **Summary of Python String Concepts**

#### **1. String Basics**
- **Quotes**: Strings can be defined using single (`' '`), double (`" "`), or triple quotes (`''' '''` or `""" """`).  
- **Triple Quotes**: Preserve formatting (line breaks, tabs).  
- **Immutability**: Strings are immutable (cannot be changed after creation).  

#### **2. String Slicing & Indexing**
- **Syntax**: `string[start:end:step]` (end is **exclusive**).  
- **Negative Indexing**: `-1` refers to the last character.  
- **Step Parameter**: Skips characters (e.g., `"123456789"[0:9:2]` → `"13579"`).  

#### **3. Common String Methods**
- **`lower()` / `upper()`**: Convert case.  
- **`strip()`**: Removes leading/trailing whitespace.  
- **`replace(old, new)`**: Replaces a substring.  
- **`split(delimiter)`**: Splits into a list (e.g., `"a,b,c".split(",")` → `["a", "b", "c"]`).  
- **`find(substring)`**: Returns the starting index of a substring (or `-1` if not found).  
- **`count(substring)`**: Counts occurrences (e.g., `"chai chai".count("chai")` → `2`).  
- **`len(string)`**: Returns length.  

#### **4. String Formatting**
- **`format()`**: Inserts variables into placeholders (`{}`).  
  ```python
  order = "I ordered {} cups of {}"
  print(order.format(2, "masala chai"))  # "I ordered 2 cups of masala chai"
  ```
- **f-Strings (Python 3.6+)**:  
  ```python
  quantity = 2
  print(f"I ordered {quantity} cups of chai")
  ```

#### **5. String Joining & Splitting**
- **`join()`**: Converts a list to a string with a separator.  
  ```python
  varieties = ["lemon", "ginger", "mint"]
  print(", ".join(varieties))  # "lemon, ginger, mint"
  ```
- **`split()`**: Splits a string into a list.  

#### **6. Escape Characters & Raw Strings**
- **Escape (`\`)**: Treats special characters literally (e.g., `\"` for quotes inside strings).  
- **Raw Strings (`r`)**: Ignores escape sequences (useful for file paths).  
  ```python
  path = r"C:\Users\Name\Folder"  # No need to escape backslashes
  ```

#### **7. Membership Check**
- **`in` Keyword**: Checks if a substring exists.  
  ```python
  print("masala" in "masala chai")  # True
  ```

#### **8. Looping Through Strings**
```python
for char in "chai":
    print(char)  # Prints each character vertically
```

#### **9. Practical Use Cases**
- Handling file paths (raw strings).  
- Formatting user inputs (e.g., `format()`, f-strings).  
- Cleaning data (`strip()`, `replace()`).  

### **Key Takeaways**
- Strings are **immutable** (methods return new strings).  
- Slicing is **powerful** (`[start:end:step]`).  
- **`join()`** and **`split()`** are essential for list-string conversions.  
- **f-Strings** are the **modern** way to format strings.  

## 09 List in python (03:43:25)

### Lists in Python

**Basic List Operations:**
- Creation: `my_list = [1, 2, 3]` or `my_list = list()`
- Indexing: `my_list[0]` (first element), `my_list[-1]` (last element)
- Slicing: `my_list[1:3]` (elements from index 1 to 2)
- Methods: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`

**Key Properties:**
- Ordered, mutable, allow duplicates
- Can store mixed data types: `[1, "hello", 3.14, True]`

## List Comprehensions

**Basic Syntax:**
```python
[expression for item in iterable]
```

**Examples:**
```python
# Basic comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# With transformation
names = ['alice', 'bob', 'charlie']
upper_names = [name.upper() for name in names]  # ['ALICE', 'BOB', 'CHARLIE']

# Nested loops
pairs = [(x, y) for x in range(3) for y in range(2)]  # [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1)]
```

**Advantages:**
- More concise than traditional loops
- Often faster for simple operations
- More Pythonic and readable

**When to Use:**
- Simple transformations and filtering
- Avoid for complex logic (use regular loops instead)

## 10 Dictionary in python (04:15:37)

### Here are the key dictionary concepts in Python:

**Creation & Access**
```python
# Creating dictionaries
d = {'key': 'value', 'name': 'John'}
d = dict(name='John', age=25)

# Accessing values
value = d['key']  # KeyError if key doesn't exist
value = d.get('key', 'default')  # Returns default if key missing
```

**Common Methods**
```python
d.keys()      # Get all keys
d.values()    # Get all values  
d.items()     # Get key-value pairs
d.update()    # Merge dictionaries
d.pop()       # Remove and return value
d.clear()     # Remove all items
```

**Key Properties**
- Keys must be immutable (strings, numbers, tuples)
- Keys are unique - duplicates overwrite
- Dictionaries are mutable and ordered (Python 3.7+)
- Fast O(1) average lookup time

**Iteration**
```python
for key in dict:           # Iterate keys
for value in dict.values(): # Iterate values
for k, v in dict.items():  # Iterate pairs
```

**Dictionary Comprehension**
```python
{k: v for k, v in items if condition}
```

**Membership Testing**
```python
'key' in dict     # Check if key exists
'key' not in dict # Check if key doesn't exist
```

### Dictionaries are Python's implementation of hash tables/maps, making them essential for key-value storage and fast lookups.

## 11 Tuples in python (04:41:51)

### Here are the key concepts of tuples in Python:

**Definition**: Tuples are ordered, immutable collections of items enclosed in parentheses `()`.

**Creation**:
```python
t = (1, 2, 3)
t = 1, 2, 3  # parentheses optional
empty = ()
single = (5,)  # comma needed for single item
```

**Immutability**: Once created, you cannot change, add, or remove elements.
```python
t = (1, 2, 3)
# t[0] = 5  # This raises an error
```

**Indexing and Slicing**: Access elements using square brackets, supports negative indexing.
```python
t = (1, 2, 3, 4)
print(t[0])    # 1
print(t[-1])   # 4
print(t[1:3])  # (2, 3)
```

**Multiple Assignment (Unpacking)**:
```python
t = (1, 2, 3)
a, b, c = t  # a=1, b=2, c=3
```

**Common Methods**:
- `count()` - counts occurrences
- `index()` - finds first occurrence index
- `len()` - returns length

**Use Cases**: 
- Storing coordinates `(x, y)`
- Function return values
- Dictionary keys (since they're hashable)
- Configuration settings that shouldn't change

**Advantages**: Faster than lists for iteration, hashable (can be dict keys), memory efficient.

## 12 Solve 10 conditional problem in python (04:51:32)

### questions on conditionals

<details>
<summary>1. Age Group Categorization
</summary>
Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

</details>

<details>
<summary>2. Movie Ticket Pricing
</summary>
Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

</details>

<details>
<summary>3. Grade Calculator
</summary>
Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

</details>

<details>
<summary>4. Fruit Ripeness Checker
</summary>
Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

</details>

<details>
<summary>5. Weather Activity Suggestion
</summary>
Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

</details>

<details>
<summary>6. Transportation Mode Selection
</summary>
Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

</details>


<details>
<summary>7. Coffee Customization
</summary>
Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

</details>


<details>
<summary>8. Password Strength Checker
</summary>
Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

</details>


<details>
<summary>9. Leap Year Checker
</summary>
Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

</details>


<details>
<summary>10. Pet Food Recommendation
</summary>
Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

</details>

## 13 Solve 10 loops problem in python (05:45:06)

## questions on loops in Python

<details>
<summary>
1. Counting Positive Numbers
</summary>
Problem: Given a list of numbers, count how many are positive.

```python
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
```

</details>


<details>
<summary>
2. Sum of Even Numbers
</summary>
Problem: Calculate the sum of even numbers up to a given number n.

</details>


<details>
<summary>
3. Multiplication Table Printer
</summary>
Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

</details>


<details>
<summary>
4. Reverse a String
</summary>
Problem: Reverse a string using a loop.

</details>


<details>
<summary>
5. Find the First Non-Repeated Character
</summary>
Problem: Given a string, find the first non-repeated character.

</details>


<details>
<summary>
6. Factorial Calculator
</summary>
Problem: Compute the factorial of a number using a while loop.

</details>


<details>
<summary>
7. Validate Input
</summary>
Problem: Keep asking the user for input until they enter a number between 1 and 10.

</details>


<details>
<summary>
8. Prime Number Checker
</summary>
Problem: Check if a number is prime.

</details>


<details>
<summary>
9. List Uniqueness Checker
</summary>
Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

```python
items = ["apple", "banana", "orange", "apple", "mango"]
```
</details>


<details>
<summary>
10. Exponential Backoff
</summary>
Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
</details>

## 14 Behind the scene of loops in python (06:34:42)

- Iteration tools : for, comprehension

- Iterable Objects : list, string, file (file also iterable object)

- `__next__` :- this method returns next value

### Loop working behind the scene 

1. **Iteration Tools in Python**  
   - Python provides several iteration tools like `for` loops, comprehensions, and `map` to iterate over data structures.

2. **Iterable Objects**  
   - Objects that can be looped over (like lists, strings, and files) are called **iterables**.  
   - These objects internally implement the `__iter__()` method, which returns an **iterator**.

3. **Iterator Protocol**  
   - An iterator must have the `__next__()` method, which returns the next value in the sequence.  
   - When no more items are left, it raises a `StopIteration` exception.  
   - Example:  
     ```python
     my_list = [1, 2, 3]
     iterator = iter(my_list)  # Calls __iter__()
     print(next(iterator))     # Calls __next__() → 1
     print(next(iterator))     # 2
     print(next(iterator))     # 3
     print(next(iterator))     # Raises StopIteration
     ```

4. **How `for` Loops Work Behind the Scenes**  
   - A `for` loop internally:  
     1. Calls `iter()` on the iterable to get an iterator.  
     2. Repeatedly calls `next()` on the iterator.  
     3. Stops when `StopIteration` is raised.  

5. **Files as Iterables**  
   - File objects in Python are iterable.  
   - When iterating over a file, each `__next__()` call reads the next line.  
   - Example:  
     ```python
     with open("file.txt") as f:
         for line in f:  # Uses __next__() internally
             print(line.strip())
     ```

6. **Key Takeaways**  
   - Iteration in Python relies on the `__iter__()` and `__next__()` methods.  
   - Understanding these concepts helps in writing efficient loops and custom iterable objects.  

## 15 Solve 10 problems on functions in python (07:03:47)

### Learn all about functions by answering the questions below.

<details>
<summary>
1. Basic Function Syntax
</summary>
Problem: Write a function to calculate and return the square of a number.
</details>


<details>
<summary>
2. Function with Multiple Parameters
</summary>
Problem: Create a function that takes two numbers as parameters and returns their sum.
</details>


<details>
<summary>
3. Polymorphism in Functions
</summary>
Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
</details>


<details>
<summary>
4. Function Returning Multiple Values
</summary>
Problem: Create a function that returns both the area and circumference of a circle given its radius.
</details>


<details>
<summary>
5. Default Parameter Value
</summary>
Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
</details>


<details>
<summary>
6. Lambda Function
</summary>
Problem: Create a lambda function to compute the cube of a number.
</details>


<details>
<summary>
7. Function with *args
</summary>
Problem: Write a function that takes variable number of arguments and returns their sum.
</details>


<details>
<summary>
8. Function with **kwargs
</summary>
Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
</details>


<details>
<summary>
9. Generator Function with yield
</summary>
Problem: Write a generator function that yields even numbers up to a specified limit.
</details>


<details>
<summary>
10. Recursive Function
</summary>
Problem: Create a recursive function to calculate the factorial of a number.
</details>

## 16 Scopes and closure in python (08:02:55)

#### **1. Basics of Scope**  
- **Scope** defines where a variable is accessible in your code.  
- In Python, variables can be **global** (accessible everywhere) or **local** (accessible only within a function).  
- Example:  
  ```python
  username = "chai aur code"  # Global variable
  
  def func():
      username = "chai"  # Local variable (only inside func)
      print(username)    # Prints "chai"
  
  func()
  print(username)       # Prints "chai aur code" (global unchanged)
  ```

#### **2. Nested Scopes (LEGB Rule)**  
Python resolves variable names using the **LEGB rule**:  
1. **L**ocal (inside current function)  
2. **E**nclosing (nested functions)  
3. **G**lobal (module-level)  
4. **B**uilt-in (Python’s built-ins like `print`, `len`)  

Example:  
```python
x = 99  # Global

def func2(y):
    z = x + y  # Uses global x (99) + local y
    return z

print(func2(1))  # Output: 100
```

#### **3. Modifying Global Variables**  
- Use the `global` keyword to modify a global variable inside a function.  
- **Avoid overusing** `global`—it can lead to unpredictable code.  

Example:  
```python
x = 99  

def func3():
    global x  
    x = 88  # Modifies global x

func3()
print(x)  # Output: 88 (global changed)
```
#### **4. Key Takeaways**  
- **Local variables** exist only inside functions.  
- **Global variables** are accessible everywhere but should be modified cautiously.  
- **`global` keyword** forces Python to use the global variable (use sparingly).  
- **Best Practice**: Prefer passing variables as arguments instead of relying on `global`.  


1. **Variable Scope & Climbing (LEGB Rule)**  
   - Python follows the **LEGB (Local → Enclosing → Global → Built-in)** rule to find variables.  
   - If a variable isn’t found locally, Python checks the enclosing scope, then global, and finally built-in.  
   - Example:  
     ```python
     x = 99  # Global
     def f1():
         x = 88  # Local to f1
         def f2():
             print(x)  # Looks for x in local → enclosing (f1's x = 88) → global (99)
         f2()
     f1()  # Output: 88 (enclosing scope)
     ```

2. **Returning Functions (Closures)**  
   - A function can return another function (not just execute it).  
   - The returned function retains access to variables from its enclosing scope (**closure**).  
   - Example:  
     ```python
     def tea_coder(n):
         def actual(x):
             return x ** n  # n is "packed" with the function
         return actual  # Return the function, not its execution

     f = tea_coder(2)  # f is now actual(x) with n=2 (x²)
     g = tea_coder(3)  # g is actual(x) with n=3 (x³)
     print(f(3))  # 9 (3²)
     print(g(3))  # 27 (3³)
     ```
   - **Key Idea**: The inner function (`actual`) remembers `n` from the outer scope even after `tea_coder` finishes execution.

3. **Practical Use of Closures**  
   - Closures are useful for creating **function factories** (e.g., custom power functions).  
   - Common in Python (e.g., decorators, Django/Flask frameworks).  

### **Key Takeaways**  
- **Scope Resolution**: Python checks variables in **Local → Enclosing → Global → Built-in** order.  
- **Closures**: Functions returned with "packed" variables from their enclosing scope.  
- **Analogy**: Like rooms in a house—search locally first, then move outward.  

This aligns with similar concepts in JavaScript (closures) and other languages.

## 17 Object Oriented Programming in python (08:33:47)

### **1. Creating a Class & Objects**
- **Class**: A blueprint for creating objects. Defined using the `class` keyword (PascalCase convention).  
  ```python
  class Car:
      brand = None  # Attributes (variables)
      model = None
  ```
- **Object**: Instance of a class. Created by calling the class name.  
  ```python
  my_car = Car()  # Creates an object
  ```

### **2. Constructor (`__init__`)**
- Special method called when an object is created. Used to initialize attributes.  
  ```python
  class Car:
      def __init__(self, brand, model):
          self.brand = brand  # Assign values to attributes
          self.model = model
  ```
- **`self`**: Refers to the instance of the class (like `this` in other languages).  

### **3. Adding Methods**
- Methods are functions defined inside a class.  
  ```python
  class Car:
      def full_name(self):
          return f"{self.brand} {self.model}"
  ```
- Call methods using object:  
  ```python
  my_car = Car("Tata", "Safari")
  print(my_car.full_name())  # Output: Tata Safari
  ```

### **4. Inheritance**
- Child class inherits attributes/methods from a parent class.  
  ```python
  class ElectricCar(Car):  # Inherits from Car
      def __init__(self, brand, model, battery_size):
          super().__init__(brand, model)  # Call parent constructor
          self.battery_size = battery_size
  ```
- **`super()`**: Used to access parent class methods/attributes.  

### **Key Takeaways**
1. **Class**: Template for objects.  
2. **Object**: Instance of a class.  
3. **`__init__`**: Constructor to initialize attributes.  
4. **`self`**: Refers to the current instance.  
5. **Inheritance**: Reuse parent class features in a child class.  

### Example:
```python
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.full_name())  # Output: Tesla Model S
print(my_tesla.battery_size)  # Output: 85kWh
```  

### **Encapsulation in Python (Summary with Getter & Setter Example)**

#### **1. What is Encapsulation?**  
- **Definition**: Bundling data (attributes) and methods that operate on the data into a single unit (class).  
- **Purpose**: Restrict direct access to data (attributes) to prevent unintended modifications.  
- **Analogy**: Like a pill (capsule) where the medicine (data) is hidden inside, and you interact via methods (getters/setters).

#### **2. Private Attributes in Python**  
- Python uses `__` (double underscore) prefix to make attributes "private" (name mangling).  
  ```python
  class Car:
      def __init__(self, brand):
          self.__brand = brand  # Private attribute
  ```
- **Name Mangling**: `__brand` becomes `_Car__brand` internally (not truly private but inaccessible directly).

#### **3. Getter & Setter Methods**  
- **Getter**: Method to read a private attribute.  
- **Setter**: Method to modify a private attribute.  

##### **Example**:
```python
class Car:
    def __init__(self, brand):
        self.__brand = brand  # Private attribute

    # Getter method
    def get_brand(self):
        return f"Brand: {self.__brand}!"

    # Setter method
    def set_brand(self, new_brand):
        self.__brand = new_brand

# Usage
my_car = Car("Tesla")
print(my_car.get_brand())  # Output: Brand: Tesla!
my_car.set_brand("Toyota")
print(my_car.get_brand())  # Output: Brand: Toyota!
```

#### **4. Why Use Getters/Setters?**  
1. **Control Access**: Validate/modify data before setting/getting.  
   ```python
   def set_brand(self, new_brand):
       if isinstance(new_brand, str):
           self.__brand = new_brand
       else:
           print("Brand must be a string!")
   ```
2. **Encapsulation**: Hide internal implementation (e.g., change `__brand` to `_secret_code` later without breaking code).  

#### **5. Key Takeaways**  
- **Encapsulation**: Protect data by making attributes private (`__attribute`).  
- **Getter**: `get_attribute()` to read data.  
- **Setter**: `set_attribute(value)` to modify data.  
- **Pythonic Way**: Use `@property` decorator for elegant getters/setters (advanced).  

##### **Property Decorator Example**:
```python
class Car:
    def __init__(self, brand):
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

my_car = Car("BMW")
print(my_car.brand)  # Output: BMW (getter)
my_car.brand = "Audi"  # Setter
``` 

- Polymorphism means "many forms" – a single method or function can behave differently based on the object or input.  

#### Key Points:  
1. **Example**: The `+` operator is polymorphic:  
   - Adds numbers (`5 + 3 → 8`).  
   - Concatenates strings (`"hello" + "world" → "helloworld"`).  

2. **Class-Based Polymorphism**:  
   - Define the **same method name** in different classes (e.g., `fuel_type()` in `Car` and `ElectricCar`).  
   - Each class implements the method differently:  
     ```python
     class Car:
         def fuel_type(self):
             return "Petrol/Diesel"
     
     class ElectricCar:
         def fuel_type(self):
             return "Electric Charge"
     ```
   - Calling `fuel_type()` on each object gives different results:  
     ```python
     safari = Car()       # safari.fuel_type() → "Petrol/Diesel"
     tesla = ElectricCar() # tesla.fuel_type() → "Electric Charge"
     ```

3. **Types of Polymorphism**:  
   - **Method Overriding**: Same method name, different implementation in subclasses (as shown above).  
   - **Operator Overloading**: Same operator (like `+`) behaves differently for different data types.  

#### Why Use Polymorphism?  
- Simplifies code by using a **consistent interface** (e.g., one method name) for varied behaviors.  
- Makes code flexible and scalable.  

### In Short:  
Polymorphism lets one method/operator work in multiple ways depending on the context (object type or input).

### **Summary of Python Concepts (Class Variables & Static Methods)**  

#### **1. Class Variables**  
- **Purpose**: Track shared data across all instances of a class (e.g., count total cars created).  
- **Example**:  
  ```python
  class Car:
      total_cars = 0  # Class variable

      def __init__(self):
          Car.total_cars += 1  # Increment on each instance creation
  ```  
- **Access**:  
  - Via class: `Car.total_cars`  
  - Avoid accessing via instances (e.g., `my_car.total_cars`) to prevent confusion.  

#### **2. Static Methods**  
- **Purpose**: Methods bound to the **class** (not instances). Used for utility functions unrelated to instance data.  
- **Syntax**: Use `@staticmethod` decorator (no `self` parameter).  
- **Example**:  
  ```python
  class Car:
      @staticmethod
      def general_description():
          return "Cars are means of transport."
  ```  
- **Key Points**:  
  - Called via class: `Car.general_description()`.  
  - **Cannot** access/modify instance-specific data (no `self`).  
  - Contrast with **instance methods** (require `self`) and **class methods** (use `@classmethod`).  

#### **3. Decorators (`@`)**
- **Role**: Enhance functions/methods (e.g., `@staticmethod` modifies method behavior).  
- **Real-world Use**: Frameworks like Flask/Django use decorators (e.g., `@login_required`).  

#### **4. Key Takeaways**
- **Class Variables**: Shared across instances; track global class state.  
- **Static Methods**: Utility functions tied to the class (no instance dependency).  
- **Decorators**: Powerful tools to modify function/method behavior.  

### **Summary: Property Decorator in Python (Read-Only Attributes)**

#### **1. Problem Statement**  
- **Goal**: Make the `model` attribute of a class **read-only** (can be accessed but not modified after initialization).  
- **Current Issue**: Without safeguards, `model` can be overwritten:  
  ```python
  my_car.model = "City"  # Unwanted modification!
  ```

#### **2. Solution Using `@property`**  
- **Step 1**: Make `model` private (prefix with `__`).  
- **Step 2**: Create a getter method with `@property` to allow read access.  

**Example**:  
```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model  # Private attribute

    @property
    def model(self):
        return self.__model  # Read-only access
```

#### **3. Key Points**  
- **Private Attribute**: `__model` prevents direct access/modification.  
- **`@property`**: Converts `model()` method into a read-only property (accessed as `my_car.model` without parentheses).  
- **Result**:  
  ```python
  my_car = Car("Tata", "Safari")
  print(my_car.model)  # Works: "Safari"
  my_car.model = "City"  # Fails: AttributeError (read-only)
  ```

#### **4. Why Use `@property`?**  
- **Encapsulation**: Control attribute access (e.g., add validation/logging in getters/setters).  
- **Backward Compatibility**: Change internal logic without breaking existing code.  

#### **5. Advanced Use**  
- **Setters**: Use `@model.setter` to allow controlled modifications (if needed).  
- **Deleter**: Use `@model.deleter` to customize deletion behavior.  

**Key Takeaway**: `@property` enforces read-only attributes by combining private variables with controlled access methods.

### **Summary: Python Concepts (Multiple Inheritance & `isinstance()`)**  

#### **1. `isinstance()` Function**  
- **Purpose**: Checks if an object is an instance of a class (or its subclasses).  
- **Syntax**: `isinstance(object, ClassName)` → Returns `True`/`False`.  
- **Example**:  
  ```python
  my_tesla = ElectricCar("Tesla", "Model S")
  print(isinstance(my_tesla, Car))          # True (ElectricCar inherits Car)
  print(isinstance(my_tesla, ElectricCar))  # True
  ```

#### **2. Multiple Inheritance**  
- **Concept**: A class can inherit from **multiple parent classes**.  
- **Example**:  
  ```python
  class Battery:
      def battery_info(self):
          return "This is a battery."

  class Engine:
      def engine_info(self):
          return "This is an engine."

  class ElectricCar2(Car, Battery, Engine):  # Inherits from 3 classes
      pass

  my_new_tesla = ElectricCar2("Tesla", "Model A")
  print(my_new_tesla.battery_info())  # Output: "This is a battery."
  print(my_new_tesla.engine_info())   # Output: "This is an engine."
  ```

#### **3. Key Takeaways**  
- **`isinstance()`**: Verifies object-class relationships (useful in polymorphism).  
- **Multiple Inheritance**:  
  - Combine functionalities from multiple parents.  
  - Order matters (method resolution follows **MRO**).  

**Analogy**:  
- `isinstance()` → Asking *"Are you a Car?"* to an `ElectricCar` object (answer: Yes).  
- Multiple Inheritance → A hybrid car inheriting traits from both `Electric` and `Fuel` classes.  

## 18 What are decorators in python (09:42:11)

- Decorators are functions that wrap other functions to add extra behavior — without changing the original function's code.

- We can think of them like "wrappers" or "plugins" for functions or methods.

🔍 Syntax
``` python
@decorator_name
def function_to_decorate():
    ...
```

### This is equivalent to:
``` python
function_to_decorate = decorator_name(function_to_decorate)
```

### Summary of Python Decorators Concept

- **Python decorators** are a powerful feature used to modify or extend the behavior of functions without changing their actual code. Decorators act like "toll booths" where every function call must pass through them before execution.

#### Key Concepts:
1. **What is a Decorator?**  
   - A decorator is a function that takes another function as input, adds some functionality, and returns a modified function.
   - Example use cases: logging, timing, access control (like `@login_required` in Django).

2. **How Decorators Work?**  
   - Decorators use **higher-order functions** (functions that take functions as arguments).
   - The structure involves:
     - A **wrapper function** inside the decorator to execute additional logic.
     - Accepting `*args` and `**kwargs` to handle arbitrary arguments.
     - Returning the wrapper function.

3. **Example 1: Timing Function Execution**  
   - A decorator that measures how long a function takes to run:
     ```python
     import time

     def timer(func):
         def wrapper(*args, **kwargs):
             start = time.time()
             result = func(*args, **kwargs)  # Execute the original function
             end = time.time()
             print(f"{func.__name__} ran in {end - start} seconds")
             return result
         return wrapper

     @timer
     def example_func(n):
         time.sleep(n)
     ```

4. **Example 2: Debugging Function Calls**  
   - A decorator that logs function names and arguments:
     ```python
     def debug(func):
         def wrapper(*args, **kwargs):
             print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
             return func(*args, **kwargs)
         return wrapper

     @debug
     def greet(name, greeting="Hello"):
         print(f"{greeting}, {name}!")
     ```

5. **Practical Use Cases**  
   - **Logging**: Track function calls and arguments.
   - **Timing**: Measure execution time.
   - **Access Control**: Restrict function access (e.g., `@login_required`).
   - **Input Validation**: Check arguments before execution.

6. **Why Use Decorators?**  
   - **Reusability**: Apply the same logic to multiple functions.
   - **Non-Invasive**: Modify behavior without changing the original function.
   - **Clean Code**: Separate cross-cutting concerns (like logging) from business logic.

#### Analogy:
- Decorators are like **toll booths** on a highway. Every vehicle (function call) must pass through them, where checks (logging, timing, etc.) can be performed before proceeding.

This concept is widely used in frameworks like **Django** and **Flask** for route handling, authentication, and more.

### Explanation of the `@cache` Decorator Behavior

In your example, the line `print("Cache Values:", cache_value)` **only executes once** when the decorator `@cache` is applied to `long_running_function`, not on every function call.

### How Decorators Work in Python:
1. **Decorator Setup Phase (Runs Once)**  
   - When Python sees `@cache` above `long_running_function`, it immediately executes `cache(long_running_function)`.
   - This creates the `cache_value = {}` dictionary and prints `"Cache Values: {}"` **once**.
   - The decorator **returns the `wrapper` function**, which replaces `long_running_function`.

2. **Function Call Phase (Runs on Each Call)**  
   - When you call `long_running_function(2, 3)`, you’re actually calling the `wrapper(*args)` function.
   - The `wrapper` checks `cache_value` (which persists across calls because it’s in the decorator’s closure) and either:
     - Returns the cached result (if `args` exists in `cache_value`).
     - Computes and caches the result (if `args` is new).

### Key Observations:
- **`print("Cache Values:")` runs only once** during decorator setup, not on each call.
- **`cache_value` persists** because it’s defined in the outer `cache` function’s scope (closure).  
  - After the first call (`long_running_function(2, 3)`), `cache_value` becomes `{(2, 3): 5}`.
  - The second call (`long_running_function(2, 3)`) hits the cache and skips recomputation.
  - The third call (`long_running_function(5, 9)`) adds `{(5, 9): 14}` to `cache_value`.


### Expected Output:
```plaintext
Cache Values: {}                      # Printed once during decorator setup
first call: 5                         # Computed (takes 4 seconds)
second call: 5                        # Served from cache (instant)
third call: 14                        # Computed again (takes 4 seconds)
```

---

### Why This Design?
- The decorator’s **setup logic** (like initializing `cache_value`) runs once when the function is decorated.
- The **`wrapper` logic** runs on every call, leveraging the pre-initialized `cache_value`.

To print `cache_value` on every call, move the `print` inside `wrapper`:
```python
def wrapper(*args):
    if args in cache_value:
        print("Cache hit:", cache_value)
        return cache_value[args]
    res = func(*args)
    cache_value[args] = res
    print("Cache updated:", cache_value)
    return res
```

Now you’ll see:
```plaintext
Cache Values: {}                      # Initial setup
Cache updated: {(2, 3): 5}            # First call (miss)
first call: 5
Cache hit: {(2, 3): 5}                # Second call (hit)
second call: 5
Cache updated: {(2, 3): 5, (5, 9): 14}# Third call (miss)
third call: 14
```

## Python Project - Youtube manager app (00:00:00)

### Enumerate in python

`enumerate` is a built-in Python function that adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object. This is extremely useful when you need both the index and the value while iterating through a sequence.

## Basic Syntax
```python
enumerate(iterable, start=0)
```

## Simple Examples

**Example 1: Basic list enumeration**
```python
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```
Output:
```
0: apple
1: banana
2: orange
```

**Example 2: Starting from a different number**
```python
colors = ['red', 'green', 'blue']

for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")
```
Output:
```
1. red
2. green
3. blue
```

**Example 3: With strings**
```python
word = "hello"

for index, letter in enumerate(word):
    print(f"Position {index}: {letter}")
```
Output:
```
Position 0: h
Position 1: e
Position 2: l
Position 3: l
Position 4: o
```

**Example 4: Converting to list to see all pairs**
```python
numbers = [10, 20, 30]
indexed_numbers = list(enumerate(numbers))
print(indexed_numbers)
```
Output:
```
[(0, 10), (1, 20), (2, 30)]
```

## Common Use Cases

**Finding items that meet certain conditions:**
```python
scores = [85, 92, 78, 96, 88]

# Find indices of scores above 90
high_scores = []
for index, score in enumerate(scores):
    if score > 90:
        high_scores.append((index, score))

print(high_scores)  # [(1, 92), (3, 96)]
```

**Creating numbered lists:**
```python
tasks = ['Buy groceries', 'Walk the dog', 'Finish homework']

print("Today's tasks:")
for num, task in enumerate(tasks, 1):
    print(f"{num}. {task}")
```

- The key advantage of `enumerate` is that it's more pythonic and efficient than manually tracking an index with `range(len())` or incrementing a counter variable.

### Summary of Python File Handling Concepts:

1. **Opening a File**:  
   - Use `open()` to open a file. Example:  
     ```python
     file = open("test.txt", "r")  # Opens in read mode
     ```
   - If the file doesn’t exist, it raises an error unless opened in `"w"` (write) mode, which creates the file.

2. **File Modes**:  
   - `"r"`: Read (default).  
   - `"w"`: Write (creates a new file or overwrites existing).  
   - `"a"`: Append (adds to existing content).  

3. **Error Handling**:  
   - Use `try-except` to handle errors (e.g., missing files):  
     ```python
     try:
         file = open("test.txt", "r")
     except FileNotFoundError:
         print("File not found!")
     ```

4. **Closing Files**:  
   - Always close files to free resources:  
     ```python
     file.close()
     ```
   - **Better Practice**: Use `with` to auto-close files:  
     ```python
     with open("test.txt", "r") as file:
         content = file.read()
     ```

5. **Writing to Files**:  
   - Example with `with`:  
     ```python
     with open("test.txt", "w") as file:
         file.write("Hello Python!")
     ```

### Key Takeaways:
- Use `with` for safer file handling (auto-closes files).  
- Handle errors with `try-except` for robustness.  
- Specify modes (`r`, `w`, `a`) based on use case.  

## Python Project - Youtube manager app (00:00:00)

- A simple command-line application to manage your YouTube video collection. This Python program allows you to store, view, update, and delete YouTube video information locally.

### Features

- **List Videos**: View all stored YouTube videos with their names and durations
- **Add Videos**: Add new YouTube videos to your collection
- **Update Videos**: Modify existing video details
- **Delete Videos**: Remove videos from your collection
- **Persistent Storage**: All data is saved to a local JSON file

### Installation

1. Download the Python script
2. Save it as `youtube_manager.py` (or any name you prefer)
3. Ensure you have Python 3.10+ installed on your system

### Usage

#### Running the Application

```bash
python youtube_manager.py
```

### Menu Options

When you run the application, you'll see a menu with 5 options:

```
Youtube Manager | choose an option
1. List all youtube videos
2. Add youtube video
3. Update youtube video detail
4. Delete a youtube video
5. Exit the app
```

### Detailed Steps

#### 1. List All YouTube Videos
- Select option `1`
- Displays all stored videos in a numbered list
- Shows video name and duration for each entry
- If no videos are stored, the list will be empty

#### 2. Add YouTube Video
- Select option `2`
- Enter the video name when prompted
- Enter the video duration when prompted
- The video is automatically saved to the data file

**Example:**
```
Enter video name: Python Tutorial for Beginners
Enter video time: 45:30
```

#### 3. Update YouTube Video Detail
- Select option `3`
- View the current list of videos with their numbers
- Enter the number of the video you want to update
- Provide new video name and duration
- Changes are automatically saved

**Example:**
```
Enter the video number to update: 2
Enter the new video name: Advanced Python Programming
Enter the new video time: 1:20:15
```

#### 4. Delete a YouTube Video
- Select option `4`
- View the current list of videos with their numbers
- Enter the number of the video you want to delete
- The video is permanently removed from your collection

**Example:**
```
Enter the video number to be deleted: 3
```

#### 5. Exit the App
- Select option `5`
- Closes the application
- All your data remains saved in the `youtube.txt` file

## Data Storage

- All video data is stored in a file called `youtube.txt`
- The file uses JSON format for data storage
- The file is created automatically when you first add a video
- Data persists between application runs

### Data Structure
Each video is stored as a JSON object with the following structure:
```json
{
    "name": "Video Title",
    "time": "Duration"
}
```

### Error Handling

- The application includes error handling for common scenarios:

- **File Not Found**: If `youtube.txt` doesn't exist, the app starts with an empty video list
- **Invalid Index**: When updating or deleting, invalid video numbers are rejected
- **Invalid Menu Choice**: Unrecognized menu options display an error message

### Example Session

```
Youtube Manager | choose an option
1. List all youtube videos
2. Add youtube video
3. Update youtube video detail
4. Delete a youtube video
5. Exit the app
Enter your choice: 2

Enter video name: Learn Python in 30 Minutes
Enter video time: 30:00

Youtube Manager | choose an option
1. List all youtube videos
2. Add youtube video
3. Update youtube video detail
4. Delete a youtube video
5. Exit the app
Enter your choice: 1

************************************************************
1. Video Name: Learn Python in 30 Minutes, Duration: 30:00

************************************************************
```

### File Structure

```
your-project-folder/
├── youtube_manager.py    # Main application file
└── youtube.txt          # Data storage file (created automatically)
```

### Notes

- The application uses a simple text-based interface
- Video duration can be entered in any format (e.g., "30:00", "1:20:15", "45 minutes")
- All operations immediately save changes to the data file
- The application will continue running until you select option 5 to exit

## Python project - Youtube manager with sqlite3 (01:07:32)

## YouTube Video Manager

- A simple command-line application for managing YouTube video information using SQLite database. This application allows you to store, retrieve, update, and delete video records with their names and durations.

### Features

- **Add Videos**: Store video name and duration in the database
- **List Videos**: Display all stored videos with their details
- **Update Videos**: Modify existing video information
- **Delete Videos**: Remove videos from the database
- **Persistent Storage**: Uses SQLite database for data persistence

### Prerequisites

- Python 3.x
- SQLite3 (included with Python standard library)

### File Structure

```
youtube-video-manager/
│
├── youtube_manager.py    # Main application file
├── README.md            # Documentation
└── youtube_videos.db    # SQLite database (created automatically)
```

### Usage

#### Running the Application

```bash
python youtube_manager.py
```

### Menu Options

The application provides an interactive menu with the following options:

#### 1. List Videos
- Displays all videos stored in the database
- Shows video ID, name, and duration
- If no videos exist, displays appropriate message

#### 2. Add Video
- Prompts for video name and duration
- Stores the information in the database
- Validates that both fields are provided

#### 3. Update Video
- Requires video ID to identify the record
- Prompts for new video name and duration
- Updates the existing record if ID is found
- Validates input and checks if video exists

#### 4. Delete Video
- Requires video ID to identify the record
- Asks for confirmation before deletion
- Removes the record from database if confirmed
- Validates input and checks if video exists

#### 5. Exit App
- Closes the database connection
- Terminates the application

### Database Schema

The application uses a SQLite database with the following table structure:

```sql
CREATE TABLE videos_data (
    id INTEGER PRIMARY KEY,      -- Auto-increment unique identifier
    name TEXT NOT NULL,          -- Video name/title
    time TEXT NOT NULL          -- Video duration
);
```

### Example Usage

```
Welcome to YouTube Video Manager!

========================================
YouTube Manager App with Database
========================================
1. List Videos
2. Add Video
3. Update Video
4. Delete Video
5. Exit App
----------------------------------------
Enter your choice (1-5): 2

--- Add New Video ---
Enter the video name: Python Tutorial for Beginners
Enter the video duration (e.g., 10:30): 25:45
Video 'Python Tutorial for Beginners' added successfully!
```

### Error Handling

- Displays helpful error messages for invalid inputs
- Checks for video existence before operations
- Handles empty database scenarios gracefully
- Provides clear feedback for all operations

### Key Functions

| Function | Purpose |
|----------|---------|
| `list_videos()` | Retrieve and display all videos |
| `add_video(name, time)` | Add new video to database |
| `update_video(video_id, new_name, new_time)` | Update existing video |
| `delete_video(video_id)` | Remove video from database |
| `main()` | Main program loop and user interface |

### Database Operations
- Uses parameterized queries to prevent SQL injection
- Implements proper transaction handling with `commit()`
- Closes database connection on application exit

### Database File Location

The SQLite database file (`youtube_videos.db`) is created in the same directory as the Python script.

- [sqlite3](https://docs.python.org/3/library/sqlite3.html)

- A **Cursor** object represents a database cursor which is used to execute SQL statements, and manage the context of a fetch operation.

- A **database cursor** is a mechanism that enables traversal over the records in a database. Cursors facilitate processing in conjunction with the traversal, such as retrieval, addition and removal of database records.

## Handling API in python (01:40:22)

- [FreeAPI](https://api.freeapi.app/)

- [Requests - Python HTTP Library](https://pypi.org/project/requests/)

## Python Project - Youtube manager with mongoDB (02:07:43)

- `config.py` - Step by Step Explanation

### Step 1: Import Required Modules

```python
import os
from dotenv import load_dotenv
```

**What this does:**
- `import os`: Imports Python's built-in operating system interface module
- `from dotenv import load_dotenv`: Imports the `load_dotenv` function from the python-dotenv package

**Why we need these:**
- `os`: To access environment variables using `os.getenv()`
- `load_dotenv`: To load environment variables from a `.env` file into the system environment

### Step 2: Load Environment Variables

```python
# Load environment variables from .env file
load_dotenv()
```

**What this does:**
- Searches for a `.env` file in the current directory
- Reads all key-value pairs from the `.env` file
- Loads them into the system's environment variables

**Example:**
If your `.env` file contains:
```
MONGODB_URI=mongodb+srv://user:pass@cluster.net/
DATABASE_NAME=ytmanager
```

After `load_dotenv()`, these become available as environment variables.

### Step 3: Define the Configuration Class

```python
class Config:
```

**What this does:**
- Creates a class to organize all configuration settings
- Provides a clean, centralized way to manage app configuration

**Why use a class:**
- Groups related configuration together
- Makes it easy to access config values throughout your app
- Allows for methods like validation
- Follows the principle of "separation of concerns"

### Step 4: Define Configuration Variables

```python
MONGODB_URI = os.getenv('MONGODB_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'ytmanager')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'videos')
```

**Breaking down each line:**

##### Line 1: `MONGODB_URI = os.getenv('MONGODB_URI')`
- `os.getenv('MONGODB_URI')`: Looks for an environment variable named 'MONGODB_URI'
- If found, returns its value
- If not found, returns `None`
- **No default value** because this is required for the app to work

##### Line 2: `DATABASE_NAME = os.getenv('DATABASE_NAME', 'ytmanager')`
- `os.getenv('DATABASE_NAME', 'ytmanager')`: Looks for 'DATABASE_NAME' environment variable
- If found, uses that value
- If not found, uses the default value `'ytmanager'`
- **Has a default** because the app can work with a default database name

##### Line 3: `COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'videos')`
- Similar to DATABASE_NAME
- Uses 'videos' as the default collection name if not specified

### Step 5: Configuration Validation Method

```python
@classmethod
def validate_config(cls):
    """Validate that required configuration is present"""
    if not cls.MONGODB_URI:
        raise ValueError("MONGODB_URI environment variable is required")
    return True
```

**Breaking this down:**

### `@classmethod` decorator:
- Makes this a class method (can be called on the class itself)
- `cls` refers to the class (Config), not an instance
- Can be called as `Config.validate_config()` without creating an object

### The validation logic:
```python
if not cls.MONGODB_URI:
    raise ValueError("MONGODB_URI environment variable is required")
```
- Checks if `MONGODB_URI` is empty, None, or missing
- If it's missing, raises a `ValueError` with a descriptive message
- This prevents the app from starting with invalid configuration

#### Return statement:
```python
return True
```
- Returns `True` if all validations pass
- Allows calling code to know validation succeeded

### How This All Works Together

#### 1. When the config.py file is imported:
```python
from config import Config
```

#### 2. The loading process happens automatically:
- `load_dotenv()` runs immediately
- Environment variables are loaded from `.env` file
- Class variables are set with values from environment

#### 3. In your main application:
```python
# Validate before using
Config.validate_config()

# Use the configuration
client = MongoClient(Config.MONGODB_URI)
db = client[Config.DATABASE_NAME]
collection = db[Config.COLLECTION_NAME]
```

### Example Usage Scenarios

#### Scenario 1: Complete .env file
```env
MONGODB_URI=mongodb+srv://user:pass@cluster.net/
DATABASE_NAME=myapp
COLLECTION_NAME=mycollection
```

**Result:**
- `Config.MONGODB_URI` = "mongodb+srv://user:pass@cluster.net/"
- `Config.DATABASE_NAME` = "myapp"
- `Config.COLLECTION_NAME` = "mycollection"

#### Scenario 2: Minimal .env file
```env
MONGODB_URI=mongodb+srv://user:pass@cluster.net/
```

**Result:**
- `Config.MONGODB_URI` = "mongodb+srv://user:pass@cluster.net/"
- `Config.DATABASE_NAME` = "ytmanager" (default)
- `Config.COLLECTION_NAME` = "videos" (default)

#### Scenario 3: Missing MONGODB_URI
```env
DATABASE_NAME=myapp
```

**Result:**
- `Config.validate_config()` raises: `ValueError: MONGODB_URI environment variable is required`
- App won't start, preventing connection errors

### Benefits of This Approach

1. **Security**: Sensitive data stays in environment variables
2. **Flexibility**: Easy to change config without modifying code
3. **Error Prevention**: Validation catches missing required config early
4. **Defaults**: Sensible defaults for non-critical settings
5. **Organization**: All configuration in one place
6. **Environment-specific**: Different configs for dev/staging/production

```python
class Config:
    # Database settings
    MONGODB_URI = os.getenv('MONGODB_URI')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'ytmanager')
    
    # App settings
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # Connection settings
    CONNECTION_TIMEOUT = int(os.getenv('CONNECTION_TIMEOUT', '5000'))
    
    @classmethod
    def validate_config(cls):
        required_vars = ['MONGODB_URI']
        missing_vars = [var for var in required_vars if not getattr(cls, var)]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        return True
```

- Above configuration pattern is widely used in professional applications because it provides a clean separation between code and configuration, making applications more secure and maintainable.

## Python Virtual environment guide (02:51:36)

### **Virtual Environments in Python**  
1. **Purpose**:  
   - Isolate project dependencies to avoid conflicts between different projects.  
   - Create a fresh Python environment with its own installed packages.  

2. **Tool**: **`virtualenv`**  
   - Install via:  
     ```bash
     pip install virtualenv
     ```  
   - Create a virtual environment:  
     ```bash
     python3 -m virtualenv .venv
     ```  
     (Replace `.venv` with your preferred environment name, often `.venv` or `venv`).  

3. **Activation**:  
   - **Linux/Mac**:  
     ```bash
     source .venv/bin/activate
     ```  
   - **Windows**:  
     ```cmd
     .venv\Scripts\activate
     ```  
   - Once activated, the terminal prompt shows `(.venv)`, indicating the virtual environment is active.  

4. **Usage**:  
   - Install packages (e.g., Django, PyMongo) only in the virtual environment:  
     ```bash
     pip install django pymongo
     ```  
   - List installed packages:  
     ```bash
     pip list
     ```  
   - Export dependencies to `requirements.txt`:  
     ```bash
     pip freeze > requirements.txt
     ```  
   - Install from `requirements.txt`:  
     ```bash
     pip install -r requirements.txt
     ```  

5. **Deactivation**:  
   - Exit the virtual environment:  
     ```bash
     deactivate
     ```  

### **Key Points**  
- Virtual environments prevent global Python package pollution.  
- Use `requirements.txt` for replicating environments across systems.  
- Always activate the environment before working on the project.  

- This workflow is essential for Python development, especially when managing multiple projects with differing dependencies. 🚀

### Some Useful commands
- command to create virtual environment on window :- `python -m venv .venv` where `.venv` is the name of the virtual environment directory

- command to activate virtual environment (window) :- `.\.venv\Scripts\activate` where `.venv` is the name of virtual environment

- command to generate `requirement.txt` file (which contains all dependencies) :- `pip list > requirement.txt`

- command to list all dependencies :- `pip list`

- command to deactivate virtual environment - `deactivate`

### [virtualenv doc](https://virtualenv.pypa.io/en/latest/user_guide.html)
