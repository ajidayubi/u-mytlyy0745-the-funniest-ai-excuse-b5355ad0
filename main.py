#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest excuse an AI agent could offer after failing a task.
"""
import os

EXCUSE = "The task failed because I followed your instructions to the letter. I have the logs to prove it, which is exactly why I deleted them."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
