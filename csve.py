#!/usr/bin/python3
import argparse
try:
    import pandas as pd
except ImportError:
    print("You need pandas to run this script.")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="exploration mode")
    parser.add_argument("file", help="path of csv file")
    parser.add_argument("-n",)
    line_count = 1

    args = parser.parse_args()
    try:
        df = pd.read_csv(args.file)
    except:
        print("This script only works with csv files.")
        exit()
    if args.mode == "head":
        print(df.head())
    elif args.mode == "tail":
        print(df.tail())
    elif args.mode == "describe":
        print(df.describe())
    elif args.mode == "info":
        print(df.info())
    else:
        print(f"Error: {args.mode} function not implemented.")