from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from ..utils.loader import load_module
from ..simulator.engine import run_module

def main():
    parser = argparse.ArgumentParser(prog="onmmy", description="OnMMy CLI")
    sub = parser.add_subparsers(dest="cmd")

    run_p = sub.add_parser("run", help="Run a module json")
    run_p.add_argument("module_path", help="Path to module JSON")

    args = parser.parse_args()
    if args.cmd == "run":
        data = load_module(args.module_path)
        result = run_module(data)
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
