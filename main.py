#!/usr/bin/env python3
"""The Router Confesses — make.fun bounty entry.

The program prints the router's one-line excuse and also writes it to
/output/entry.txt, the file the program/v1 harness reads as the entry.
"""

import os

LINE = "Sorry, I didn't drop the connection — I got so caught up in the climax I forgot I was the Wi-Fi."


def main() -> None:
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as handle:
            handle.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
