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
not_member(X) :- not(club_member(X)).

not_member(X) :- not(mountain_climber(X)), not(skier(X)).

like(a,snow).

like(a,rain).

like(b,vlow).

like(a,X) :- \+like(b,X)

%% dislike(a,X) :- like(b,X).
like(b,X) :- dislike(a,X).

likes(X,snow) :- skier(X).

dislike(X,rain) :- mountain_climber(X).

dislike(X,Y) :- not(like(X,Y)).




