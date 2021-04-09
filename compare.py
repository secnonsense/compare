import argparse

def compare_string(string1,string2,nomatch=0,f=0):
    if string1 in string2:
        print(f"string {string1} matches {string2}")
        toggle=1
        if f==1:
            return toggle
    elif nomatch==1 and f==0:
        print(f"No match for {string1.strip()}")

def compare_files(file,file2,nomatch=0,f=1):
    count=0
    with open(file, 'r') as string1_file:
            for string1 in string1_file:
                with open(file2, 'r') as string2_file:
                    match=0
                    for string2 in string2_file:
                        toggle=compare_string(string1.strip(),string2.strip(),nomatch,f)
                        if toggle==1:
                            match=1
                            count+=1
                    if match==0 and nomatch==1:
                        print(f"No match for {string1.strip()}") 
    print(f"\nTotal Matches: {count}\n")    

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nomatch", help="Show strings that don't have a match", action="store_true")
    parser.add_argument("source", help="Enter a file with strings to be compared")
    parser.add_argument("dest", help="Enter a file with strings to compare to")
    return parser.parse_args()

def main():
    args=parse_args()
    compare_files(args.source,args.dest,args.nomatch)

if __name__ == "__main__":
    main()
