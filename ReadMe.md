
## 02 Python inner working (00:27:50)

==> python code  -------- python Interpreter ------> Byte Code (mostly hidden) --------> Python Virtual Machine (PVM)

### Step 1 - compiled to Byte Code (although python is Interpretered language, here compiled is just technical term)

#### Byte Code - Byte Code is low level code which is Platform Independent (ByteCode is not machine code). It runs faster

#### `.pyc` --> It is compiled python (frozen Binaries)

#### __pycache__ is a directory that Python automatically creates to store compiled bytecode files (.pyc files) for faster program execution.

##### When we run a Python script, the interpreter compiles your .py source files into bytecode and caches them in __pycache__ folders. This compilation step is skipped on subsequent runs if the source file hasn't changed, making our programs start faster.

#### `hello_python.cpython-312.pyc` :- is the compiled bytecode version of your `hello_python.py` source file. It represent source change and Python Version

#### Above file `hello_python.cpython-312.pyc` works only for imported files, not for top level files.

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

#### Why it matters: Affects how objects behave when passed to functions, assigned to variables, or used as dictionary keys (only immutable objects can be dict keys).

### Mutable objects can have side effects (modify original data)
### Immutable objects are safer - no unexpected changes
### Use immutable objects when you want to prevent accidental modifications

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

#. Variable Assignment & References
- Assigning a variable (a = b) creates a reference, not a copy.

### To copy a list, use slicing (b = a[:]) or copy.copy().

#. `is` vs `==`
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

## 13 Solve 10 loops problem in python (05:45:06)

## 14 Behind the scene of loops in python (06:34:42)

### Iteration tools : for, comprehension

### Iterable Objects : list, string, file (file also iterable object)

### `__next__` :- this method returns next value

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

**Next Steps**: Explore `@classmethod` and other decorators!  

---  
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

**Next Steps**: Explore **Method Resolution Order (MRO)** for complex inheritance!