# Memory Manager

`memory_manager` is a Python package designed to facilitate hooking and manipulating game memory using the `pymem` library. This package simplifies the process of reading and writing memory addresses for various in-game variables, such as currency and weapon ammo, providing an easy-to-use library.

## Features

- Hook into a game's process using `pymem`.
- Read and write different data types (e.g., integers, floats) at specified memory addresses.
- Support for both constant and recalculated pointers.
- Simple and clear API for memory manipulation.

## Installation

You can install `memory_manager` via pip:

```bash
pip install memory_manager
```

# Usage
## Basic Setup

To get started, import the MemoryManager class and use the hook method to attach to the game's process and module.

```python
from memory_manager import MemoryManager

# Initialize the memory manager and hook into the game's process and module
process_name = "game_name"
module_name = "game_module"
pointers = {
    "Health": {
        "Address": 0xB6,
        "Offsets": [0x1A, 0x2B, 0x3C],
        "Type": "4 Bytes",
        "Constant": True
    },
    "Gold": {
        "Address": 0x1DE,
        "Offsets": [0x4D, 0x5E, 0x6F],
        "Type": "4 Bytes",
        "Constant": False
    },
    "PlayerStats": {
        "Stamina": {
            "Address": 0x2F,
            "Offsets": [0xA, 0xB, 0xC],
            "Type": "Float",
            "Constant": True
        },
        "Experience": {
            "Address": 0x3A,
            "Offsets": [0xD, 0xE],
            "Type": "2 Bytes",
            "Constant": True
        }
    }
}

mm = MemoryManager()
pointers = mm.hook(process_name, module_name, pointers)
```
## Reading and Writing Memory
Once you've hooked into the game's process, you can read and write memory values using the Get and Set methods attached to each pointer.

### Reading Memory
```python
# Read the value of health
health = pointers["Health"]["Get"]()
print(f"Current health: {health}")

# Read the value of gold
gold = pointers["Gold"]["Get"]()
print(f"Current gold: {gold}")

# Read the value of stamina
stamina = pointers["PlayerStats"]["Stamina"]["Get"]()
print(f"Current stamina: {stamina}")

# Read the value of experience
experience = pointers["PlayerStats"]["Experience"]["Get"]()
print(f"Current experience: {experience}")
```

### Writing Memory
```python
# Set the value of health
new_health_value = 100
pointers["Health"]["Set"](new_health_value)

# Set the value of gold
new_gold_value = 9999
pointers["Gold"]["Set"](new_gold_value)

# Set the value of stamina
new_stamina_value = 75.5
pointers["PlayerStats"]["Stamina"]["Set"](new_stamina_value)

# Set the value of experience
new_experience_value = 5000
pointers["PlayerStats"]["Experience"]["Set"](new_experience_value)
```

## Handling Errors
The memory_manager package is designed to handle errors gracefully. If a memory read or write operation fails, the functions will return False instead of raising an exception.

```python
# Attempt to read memory
success = pointers["Health"]["Get"]()
if not success:
    print("Failed to read health value.")

# Attempt to write memory
success = pointers["PlayerStats"]["Experience"]["Set"](new_gold_value)
if not success:
    print("Failed to write new gold value.")
```

## Advanced Usage
### Custom Data Types
You can extend the MemoryManager to support additional data types by modifying the read_funcs and write_funcs dictionaries.

```python
# Add support for 8-byte integers
mm.read_funcs["8 Bytes"] = mm.mem.read_longlong
mm.write_funcs["8 Bytes"] = mm.mem.write_longlong

# Example usage
pointers["New Pointer"] = {
    "Address": 0x11223344,
    "Offsets": [0x70, 0x80],
    "Type": "8 Bytes",
    "Constant": True
}

value = pointers["New Pointer"]["Get"]()
pointers["New Pointer"]["Set"](value + 100)
```

### Dynamic Pointer Calculation
For pointers that require dynamic recalculation (i.e., Constant is False), the Get and Set methods will automatically recalculate the pointer address before performing the read or write operation.

```python
# Read and write dynamic pointers
gold = pointers["Gold"]["Get"]()
pointers["Gold"]["Set"](gold + 500)
```
# Acknowledgments
- pymem - A python library for process memory manipulation.