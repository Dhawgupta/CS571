member(a).
member(b).
member(c).
member(X):- sk(X); mc(X).
% member(X):-mc(X).
% member(X):-mc(X).
%% member(X):- sk(X),mc(X).
%(sk(X) ; mc(X)) :- member(X).
%(sk(X), mc(X)) :- member(X)
sk(d).
likes(a,rain).
likes(a,snow).
likes(a,X):- \+ likes(b,X).
likes(a,X).  %% 
likes(b,X):- likes(a,X),!,fail.
likes(b,X).
mc(X):- likes(X,rain),!,fail.
mc(X).
sk(X):- \+ likes(X,snow),!,fail.
sk(X).