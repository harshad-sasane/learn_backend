"""
SIMPLE COMMAND-LINE ARGUMENTS DEMO
Shows different uses of sys.argv
"""

import random
import sys

print("=== Command Line Arguments Demo ===")

# 1. Show what's in sys.argv
print(f"\n1. What you typed: {sys.argv}")
print(f"   Total args: {len(sys.argv)}")

# 2. Original example
if len(sys.argv) > 1:
    print(f"\n2. Hello, my name is {sys.argv[1]}")

# 3. Quick RPS game
choices = ["rock", "paper", "scissors"]
if len(sys.argv) > 1 and sys.argv[1] in choices:
    computer = random.choice(choices)
    print(f"\n3. RPS: You: {sys.argv[1]}, Computer: {computer}")

# 4. Position demonstration
print("\n4. Argument positions:")
for i in range(min(3, len(sys.argv))):
    print(f"   Position {i}: {sys.argv[i]}")
