# Run: python command_line.py 5 3 add
# Run: python command_line.py 5 3 subtract
# Run: python command_line.py 5 3 multiply
# Run: python command_line.py 5 3 divide
# Difficulty: VIII

import argparse

# Create a parser
parser = argparse.ArgumentParser(description="Perform basic arithmetic operations.")

# Add arguments
parser.add_argument("x", type=int, help="the first number")
parser.add_argument("y", type=int, help="the second number")
parser.add_argument("operation", type=str, choices=["add", "subtract", "multiply", "divide"], help="the operation to perform")

# Parse arguments
args = parser.parse_args()

# Perform operation and print result
if args.operation == "add":
    result = args.x + args.y
elif args.operation == "subtract":
    result = args.x - args.y
elif args.operation == "multiply":
    result = args.x * args.y
elif args.operation == "divide":
    if args.y != 0:
        result = args.x / args.y
    else:
        result = "Error: Division by zero is not allowed."

print(result)