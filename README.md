# Pytho{\\}

I hate the fact that i need to tab "properly" python files, that may cause several errors and confusions betweens actual tabs and spaces. 
Why not just use regular curly brackets? 

So I created `Pytho{\}` a simple python pre-compiler with no pip dependencies, that simplily parses the python with curly brackets into the normal sintax and runs it, after the execution the temporary code is deleted.

Just put Pytho{N}.py file on you project and stop using ident and :

Examples:
```
python3 Pytho\{N\}.py examples/basic.py
./Pytho\{N\}.py examples/basic.py
./Pytho\{N\}.py -v 2 examples/basic.py
./Pytho\{N\}.py -v 3 examples/basic.py
./Pytho\{N\}.py examples/basic.py --argument to file
./Pytho\{N\}.py #iterative shell (here you cannot use {})
```