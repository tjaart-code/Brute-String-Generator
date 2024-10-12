# Brute Force String Generator

This code produces all possible combinations of strings using a specified character set. It accepts a minimum and maximum length, a prefix, and an optional output file to save the generated strings.<br><br>

#### Example Usage:<br>
<br>
<code>python3 bruteStringer.py 3 5 abc "pre_" output.txt</code><br>
This command would:<br>
Generate strings of length 3 to 5.<br>
Use the character set abc (i.e., generate combinations of "a", "b", and "c").<br>
Add the prefix "pre_" to each generated string.<br>
Save the output to output.txt.<br>
<br>
Sample Output:<br>
For min_length=3, max_length=4, charset="abc", and prefix="pre_", the output in the file could look like this:<br>
pre_aaa<br>
pre_aab<br>
pre_aac<br>
pre_aba<br>
pre_abb<br>
...<br>
pre_acc<br>
pre_baa<br>
pre_bab<br>
...<br>
