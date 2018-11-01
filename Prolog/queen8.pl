del(X, [X | Tail],  Tail).
del(X, [Y|Tail], [Y|Tail1]) :- 
	del(X,Tail, Tail1).


%%  make the permutations
perm([],[]).
perm([Head  | Tail],Permlist) :-
	perm(Tail, Permtail), del(Head , Permlist, Permtail).

%%  the solution to the 8 queen problem
solution(Queens) :- 
	perm([1,2,3,4,5,6,7,8], Queens),safe(Queens).
%% Generate different permutationf for the possible row position and check if the posititon is safe or nto


safe([]).
safe([Queen| Other]) :-
	safe(Other), noattack(Queen, Other, 1).


noattack(_, [], _). %% no attack possible if there is not queen lsef tot eh right and aslo we woiuld have check ed all teh queens tot eh lsegft
noattack(Y, [Y1| Ylist], Xdist):-
Y1 - Y  =\= Xdist,
Y - Y1 =\= Xdist,
Dist1 is Xdist + 1, 
noattack(Y, Ylist, Dist1).



