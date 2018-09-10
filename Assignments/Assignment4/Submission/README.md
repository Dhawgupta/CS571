## Important files : 
1. `main.py` is the file to be run 
2.  In the `main.py` file assign the expression to `Expr` varaible for which to wish to prove on the line `154`
3.  If you get `TRUE` in the end output -> that the theorem is proved


## MOdified Code with the universal solver.(10/9/18)
1. `main3.py` contains the code for implememting the any thing solver, it call the Solveexpression from teh main_main class.
2. `main_main.py` class contains the functiont to solve any expressino
3. It chains the expression , sub expression to solve them and achieve sub expressions.
4. `main3.py` solver is more powerful i.e. it can prove mmore theorems for eg `'((P^Q)>(PVP))'` can't be solved using the main_main solver, whereas it can be solved using .
5. Running the code : `python main3.py`

## Things yet to be implemented in the code 
1. Make the `main3.py` program in the format such as to take in the predicate input.
2. Clean the output of the code 


## Changes are being made to the main3_2.py and main_main2.py