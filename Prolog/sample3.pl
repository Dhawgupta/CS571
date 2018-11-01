membro(a).
membro(b).
membro(c).
%% membro(X) :- \+ notmembro(X).
like(a,rain).
like(a,snow).
%% climber(d).
%% notmembro(X) :- \+ski(X), \+climber(X).
climber(X) :- \+ski(X), membro(X).
ski(X) :- \+ notski(X).
%% dislike(X, Y) :- \+ like(X,Y).
dislike(X,rain) :- climber(X).
%% like(X,snow) :- ski(X).
notski(X) :- \+like(X,snow).
like(b,X) :- dislike(a, X).
dislike(b, X) :- like(a,X).
g(X) :- membro(X), climber(X), \+ski(X),!.