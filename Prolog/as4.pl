club_member(a).
club_member(b).
club_member(c).
%%  above is the definiotin for different members in the club

%% mountain_climber(d).

%% club_member(X) :- 
%% 	%%  WEither a mountain climber or a skier
%% 	mountain_climber(X).

%% club_member(X) :- 
%% 	skier(X).

mountatin_climber

like(a,snow).

like(a,rain).

dislike(X,Y) :- like(X,Y),!,fail.

like(a,X) :- like(b,X),!,fail.

dislike(a,X) :- like(b,X).

dislike(X,rain) :- mountain_climber(X).





