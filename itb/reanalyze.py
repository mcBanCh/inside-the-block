"""Offline: recompute results for every run under <data>/runs from committed raw files."""
import glob
import os
import sys

from .analyze import analyze

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "data"
    for rdir in sorted(glob.glob(os.path.join(root, "runs", "*"))):
        if os.path.exists(os.path.join(rdir, "landed.jsonl")):
            analyze(rdir)
            print("re-analyzed", rdir)
