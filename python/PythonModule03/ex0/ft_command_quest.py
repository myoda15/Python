import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    args: list[str] = sys.argv[1:]
    if len(args) == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
        for i, arg in enumerate(args):
            print(f"Argument {i + 1}: {arg}")
    print(f"Total arguments: {len(sys.argv)}")
