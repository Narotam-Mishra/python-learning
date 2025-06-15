
## 02 Python inner working (00:27:50)

==> python code  -------- python Interpreter ------> Byte Code (mostly hidden) --------> Python Virtual Machine (PVM)

# Step 1 - compiled to Byte Code (although python is Interpretered language, here compiled is just technical term)

# Byte Code - Byte Code is low level code which is Platform Independent (ByteCode is not machine code). It runs faster

# `.pyc` --> It is compiled python (frozen Binaries)

# __pycache__ is a directory that Python automatically creates to store compiled bytecode files (.pyc files) for faster program execution.

# When we run a Python script, the interpreter compiles your .py source files into bytecode and caches them in __pycache__ folders. This compilation step is skipped on subsequent runs if the source file hasn't changed, making our programs start faster.

# `hello_python.cpython-312.pyc` :- is the compiled bytecode version of your `hello_python.py` source file. It represent source change and Python Version

# Above file `hello_python.cpython-312.pyc` works only for imported files, not for top level files.

# What `hello_python.cpython-312.pyc` represents:
- Compiled bytecode :- our Python source code translated into Python's intermediate bytecode format
- Version-specific: The "cpython-312" indicates it was compiled with CPython interpreter version 3.12
- Binary format: Contains low-level instructions that the Python virtual machine can execute directly

# Key point :- This file `hello_python.cpython-312.pyc` is only created when your script is imported as a module by another script, not when you run it directly with python hello_python.py. For direct execution, Python compiles to memory without saving the .pyc file.

# Facts about Python Virtual Machine (PVM) :-
- Code loop to iterate byte code
- Runtime engine
- Also known as `python interpreter`

# Byte Code is not machine code, it is
- python specific interpretation,
- cypthon (standard implementation), jython, Inron python, stackless, pypy. These are different implementations of the Python programming language - alternative ways to run Python code with different underlying engines and features.

# Key point: They all run the same Python code but use different underlying technologies, offering various performance characteristics and platform integrations. CPython remains the reference implementation that most people use.

# Python Virtual Machine (PVM) :- The Python Virtual Machine (PVM) is the runtime engine that executes Python bytecode. It's the core component that actually runs your Python programs.

# PVM is 
- An interpreter that reads and executes Python bytecode instructions
- Part of the Python interpreter (like CPython, PyPy, etc.)
- Acts as an abstraction layer between your code and the operating system

How PVM works:
- Python source code (.py) → compiled to bytecode (.pyc)
- PVM reads bytecode instructions one by one
- Executes each instruction (variable assignment, function calls, loops, etc.)

# Example flow 
hello.py → bytecode → PVM → actual execution

# How Python Works Internally (Detailed) - https://claude.ai/share/8b16fe6e-2be1-47c7-8b3b-7344745b286f

# # Python Execution model - https://claude.ai/share/dc253a1c-048b-48fb-9b67-4eb7a89cc260


## 03 Python in shell (00:46:36)

# Python shell is useful for :-
- Interactive Development
- Data Exploration
- Learning & Prototyping
- System Administration
- Calculator/Tool

## 04 Immutable and mutable in python (01:06:40)

# Immutable and Mutable are something that is related to memory reference in python

# Mutable Objects - Can be changed after creation:

a). Lists: [1, 2, 3] - can add, remove, or modify elements
b). Dictionaries: {'a': 1} - can add, update, or delete key-value pairs
c). Sets: {1, 2, 3} - can add or remove elements
d). User-defined objects - attributes can be modified

# Immutable Objects - Cannot be changed after creation:

a). Strings: "hello" - operations create new strings
b). Tuples: (1, 2, 3) - cannot modify elements
c). Numbers: 42, 3.14 - operations create new values
d). Frozen sets: frozenset({1, 2}) - immutable version of sets
e). Booleans: True, False

# Why it matters: Affects how objects behave when passed to functions, assigned to variables, or used as dictionary keys (only immutable objects can be dict keys).

# Mutable objects can have side effects (modify original data)
# Immutable objects are safer - no unexpected changes
# Use immutable objects when you want to prevent accidental modifications

## 05 Python Data Types - Big Picture (01:23:48)

# Data Types / Object Types

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

# Python Internals & Memory Management

- Python uses dynamic typing—variables don’t have types, but the objects they reference do.

- Objects (like numbers, strings, lists) live in memory, and variables are just references (pointers) to them.

- Reference Counting: Python tracks how many references an object has. When references drop to zero, the garbage collector reclaims memory.

- Optimization: Python caches small integers and strings for efficiency (e.g., 5 or "hello" may reuse the same memory).

# Mutable vs Immutable Objects
- Immutable (can’t change after creation): int, float, str, tuple
  - Changing them creates a new object.

# Mutable (can change in-place): list, dict, set
- Modifying them affects all references.

#. Variable Assignment & References
- Assigning a variable (a = b) creates a reference, not a copy.

# To copy a list, use slicing (b = a[:]) or copy.copy().

#. `is` vs `==`
- `==` checks value equality.
- `is` checks memory identity (same object):

# Garbage Collection
- Python’s GC cleans up objects with zero references.
- Exception: Small integers/strings may linger for reuse.

# Behind-the-Scenes Optimization
- Python pre-allocates small integers (-5 to 256) for speed.
- Interning: Reuses immutable objects (like short strings) to save memory.

# Key Takeaways :-
- Variables are labels, not boxes. Objects live independently in memory.
- Mutable objects can lead to unexpected side effects if shared.
- Use copy() or slicing to avoid accidental reference sharing.

## 