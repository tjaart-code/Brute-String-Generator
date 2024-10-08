This Python code defines a script that generates all possible strings of specified lengths using a given character set and an optional prefix. 

Brute String Generator
Start it with python3 bruteStringer.py 4 6 "abcdefghijklmnopqrstuvwxyz1234567890" "" output.txt
This will produce all strings with length 4 to 6 using characters from a to z and numbers 0 to 9.
The generated strings will be saved to output.txt.
You need to edit these settings to fit your needs.

Examples:
1. When the prefix is known, use it as the 4th parameter.
   If you know the password is "MyPass***" and the *** are some numbers, call it with:
   python3 bruteStringer.py 3 3 "1234567890" "MyPass" mypass_results.txt

2. python3 bruteStringer.py 2 3 "ab" ""
   This will generate and save:
   aa
   ab
   ba
   bb
   aaa
   aab
   aba
   abb
   baa
   bab
   bba
   bbb
