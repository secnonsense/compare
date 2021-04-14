# compare
Check to see if items in one file containing strings are also in another file.  The default behavior is to find a match within the destination strings. For an exact match use the -x option.  

Usage:  

python3 compare.py \<option\> \<source_file\> \<dest_file\>  

options -   
"-n", "--nomatch" - "Show strings that don't have a match in the destination string"    
"-m", "--matchonly" - "Display matching strings only with no other verbiage"  
"-d", "--dontmatch" - "Print a list of strings that don't match with no other verbiage"  
"-x", "--exactmatch" - "Print a list of strings that match exactly"   
  
source_file -  The file containing strings to compare   
dest_file   -  The file containing strings to be compared to  
