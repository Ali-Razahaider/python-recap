# Simple CLI demo
import argparse

parser = argparse.ArgumentParser(description="Greeting tool")
parser.add_argument("--name", help="Your name", default="World")
parser.add_argument("--count", help="How many times", type=int, default=1)

args = parser.parse_args()

for _ in range(args.count):
    print(f"Hello, {args.name}!")