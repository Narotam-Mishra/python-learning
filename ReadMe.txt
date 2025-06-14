
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

