%% del(X, L1 , L2).
%%  Write the base condititon

%%  condition to delete multipl eoocurence if X
del(X,[],[]).
del(X, [X|Tail],Tail1) :-
	del(X,Tail, Tail1). % how does this work  andl lead to the termination
del(X, [Y|Tail], [Y|Tail1]) :- 
	del(X, Tail, Tail1).


%% del(X, [X|Tail],Tail).% how does this work  andl lead to the termination
%% del(X, [Y|Tail], [Y|Tail1]) :- 
%% 	del(X, Tail, Tail1).


%% del(4, [3,1,5,6,3,3,4],Y). sampel command
