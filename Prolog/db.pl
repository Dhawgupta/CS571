what_grade(5) :-  
	write('Go to kindergarden').

what_grade(6) :-  
	write('Go to first grade').
	
what_grade(Other) :-  
	Grade is Other - 5,
	format('Go to grade ~w',[Grade]).

	