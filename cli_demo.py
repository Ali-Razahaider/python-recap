# Simple CLI demo - renamed from argparse to avoid module conflict
import argparse as argparse_module

# Create parser
parser = argparse_module.ArgumentParser(description="A simple greeting tool")

# Add arguments
parser.add_argument("--name", help="Your name", default="World")
parser.add_argument("--count", help="How many times to greet", type=int, default=1)

# Parse arguments
args = parser.parse_args()

# Use arguments
for i in range(args.count):
    print(f"Hello, {args.name}!")