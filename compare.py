#!/usr/local/bin/python3

import argparse

def compare_string(string1,string2,nomatch=0,i=0,d=0,x=0,ignore=0,matchdest=0):
    string1a=string1
    string2a=string2
    if ignore:
        string1=string1.lower()
        string2=string2.lower()
    if string1 in string2 and x==0:
        if i==1 and d==0 and matchdest==0:
            print(string1a)
        elif i==1 and d==0 and matchdest==1:
            print(string2a)
        elif i==0 and d==0:
            print(f"string {string1a} matches {string2a}")
        toggle=1
        return toggle
    if string1 == string2 and x==1:
        if i==1 and d==0:
                print(string1a)
        elif i==0 and d==0:
            print(f"string {string1a} matches {string2a}")
        toggle=1
        return toggle

def compare_files(file,file2,nomatch=0,i=0,d=0,x=0,ignore=0,matchdest=0):
    count=0
    with open(file, 'r') as string1_file:
            for string1 in string1_file:
                with open(file2, 'r') as string2_file:
                    match=0
                    for string2 in string2_file:
                        toggle=compare_string(string1.strip(),string2.strip(),nomatch,i,d,x,ignore,matchdest)
                        if toggle==1:
                            match=1
                            count+=1
                    if match==0 and nomatch==1:
                        print(f"No match for {string1.strip()}") 
                    elif match==0 and d==1:
                        print(string1.strip())
    if i==1 or d==1:
        print("\n")
    else:
        print(f"\nTotal Matches: {count}\n")    

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nomatch", help="Show strings that don't have a match", action="store_true")
    parser.add_argument("-m", "--matchonly", help="Print a list of matching strings only", action="store_true")
    parser.add_argument("-d", "--dontmatch", help="Print a list of strings that don't match", action="store_true")
    parser.add_argument("-x", "--exactmatch", help="Print a list of strings that match exactly", action="store_true")
    parser.add_argument("-w", "--matchdest", help="Print a list of what has been matched against", action="store_true")
    parser.add_argument("-i", "--ignore_case", help="Ignore Case", action="store_true")
    parser.add_argument("source", help="Enter a file with strings to be compared")
    parser.add_argument("dest", help="Enter a file with strings to compare to")
    return parser.parse_args()

def main():
    args=parse_args()
    compare_files(args.source,args.dest,args.nomatch,args.matchonly,args.dontmatch,args.exactmatch,args.ignore_case,args.matchdest)

if __name__ == "__main__":
    main()
