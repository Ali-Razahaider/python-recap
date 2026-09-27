# Simple CLI demo
import argparse

# Create parser with description
parser = argparse.ArgumentParser(description="Greeting tool")

# Add --name argument, defaults to "World" if not provided
parser.add_argument("--name", help="Your name", default="World")

# Add --count argument, defaults to 1, type must be int
parser.add_argument("--count", help="How many times", type=int, default=1)

# Parse command-line arguments
args = parser.parse_args()

# Greet the named person the specified number of times
for _ in range(args.count):
    print(f"Hello, {args.name}!")