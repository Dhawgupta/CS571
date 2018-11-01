
%%  single delection rule
del(X, [X|Tail],Tail).% how does this work  andl lead to the termination
del(X, [Y|Tail], [Y|Tail1]) :- 
	del(X, Tail, Tail1).


permutation([],[]).
permutation(L, [X|P]) :-
	 permutation(L1, P), del(X, L, L1).
