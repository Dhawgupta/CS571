member(a).
member(b).
member(c).
member(X) :- \+mc(X), \+sk(X), !, fail.
member(X).
like(a, X) :- \+like(b, X).
like(b,X) :- like(a,X), !, fail.
like(b,X). %% if a doesnt like X then B likes that 

mc(X) :- like(X, rain), !, fail.
mc(X).
sk(X) :- \+ like(X,snow), !, fail. %% if it is not provable that X likes snow then it is not possible that X is a skier, whereas if it provable that X likes snow then X is a skier using the below clause
%% sk(X) :-  member(X),\+ mc(X).
sk(X). %% this is used when like(X, snow) is provable and hence the above statemtne fails and the controls passes to this statemten and this statemtne is true.
g(X) :- member(X), mc(X), \+ sk(X).