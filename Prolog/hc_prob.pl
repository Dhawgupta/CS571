mem(a).
mem(b).
mem(c).

mem(X) :- notmc(X), notsk(X), !, fail.
mem(X).
like(a,rain).
like(a, snow).

like(a,X):-dislike(b, X).
like(b, X) :- dislike(a, X).

mc(X):-like(X, rain), !, fail.
mc(X).
notsk(X):-dislike(X , snow).
notmc(X) :- mc(X), !, fail.
notmc(X).

dislike(P,Q):-like(P,Q),!,fail.
dislike(P,Q).
g(X):-mem(X),mc(X), notsk(X).