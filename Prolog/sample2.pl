member(a).
member(b).
member(c).
member(d).
member(X):- \+mc(X),fail.
member(X).
member(X):- \+sk(X),!,fail.
member(X).
%% dislike(X,Y) :- \+like(X,Y).
%% like(d, snow).
%% dislike(a,X) :- like(b, X).
like(a,rain).
like(a,snow).
%% like(b,rain).
like(a,X) :- \+ like(b,X).
like(b,X) :- like(a,X),!,fail.
like(b,X).
like(X, Y).
mc(X):- like(X,rain),!,fail.
mc(X).
sk(X):- \+like(X,snow),!,fail.
sk(X).
g(X):-member(X),mc(X),\+sk(X).