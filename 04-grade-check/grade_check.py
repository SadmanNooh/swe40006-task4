import csv
import sys

INPUT = "/data/marks.csv"
OUTPUT = "/data/report.txt"

print("grade-check started")

try:
    rows = list(csv.DictReader(open(INPUT)))
except FileNotFoundError:
    print(f"ERROR: {INPUT} not found. Did you mount a folder to /data?")
    sys.exit(1)

earned = 0
remaining = 0
lines = []

for r in rows:
    weight = float(r["weight"])
    if r["score"]:
        pct = float(r["score"]) / float(r["out_of"])
        earned += pct * weight
        lines.append(f"{r['item']}: {pct * 100:.0f}%")
    else:
        remaining += weight
        lines.append(f"{r['item']}: not marked yet")

lines.append("")
lines.append(f"Earned so far: {earned:.1f}%")
for grade, cutoff in [("HD", 80), ("D", 70), ("C", 60), ("P", 50)]:
    need = (cutoff - earned) / remaining * 100
    lines.append(f"Need for {grade}: {need:.1f}% on the rest")

report = "\n".join(lines)
print(report)
open(OUTPUT, "w").write(report + "\n")
print(f"report saved to {OUTPUT}")
print("grade-check finished")
