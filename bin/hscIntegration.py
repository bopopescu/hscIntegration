#!/usr/bin/env python

import argparse
from hsc.integration import Integration

parser = argparse.ArgumentParser()
parser.add_argument("--only", action="append", default=[], choices=Integration.getTests(),
                    help="Only execute specified tests")
parser.add_argument("--deactivate", action="append", default=[], choices=Integration.getKeywords(),
                    help="Deactivate tests with this keyword")
parser.add_argument("--output", type=str, default=".", help="Output path")
parser.add_argument("--pbs", type=str, default="--nodes 1 --procs 12 --queue mini",
                    help="Arguments for PBS jobs")
args = parser.parse_args()

Integration(args.only, args.deactivate).run(workDir=args.output, pbsArgs=args.pbs)
