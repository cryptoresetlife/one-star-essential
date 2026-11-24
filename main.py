"""One-Star Review of Something Essential: 160 characters at most."""
import os

LINE = (
    "★☆☆☆☆ Gravity. Hasn't failed once in my whole life, "
    "and it only seems to try when I'm holding my phone over a sink."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE.strip())
