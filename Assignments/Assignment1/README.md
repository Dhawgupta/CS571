## Assignment 1
I have attached to solutions for the assignment 
Our assignment contains solutions from each member conatianed in the file named after their repestive roll numbers
Followinga are the files
1. 1501CS54 - Dhawal Gupta
2. 1821ME18 - Vikash Kumar
3. 1821EE13 - Avishek Kumar

### Notes for 1501CS54 
I would like to attach some notes with my results 

We were to implement the expectation maximisation paradigm:
The starting values that we have been suggested are 
P= 0.7
P1 = 0.6
P2 = 0.3

The probability for heads comes very close to 0.5 i.e.
0.7*0.6 + 0.3*0.3 = 0.42 + 0.09 = 0.51 i.e. very close to 0.5

So no matter what value we set for p the estimate for p1 and p2 will always come and settle near 0.5 and 0.5
Experiments
```
Dhawals-MacBook-Pro:Assignment1 dhawgupta$ python solution.py 
The real Parameters P:0.7, P1:0.6, P2:0.3
Experiment Number : 0
Starting Params P:0.905182959313453, P1:0.9399312012708729, P2:0.5200474107099269
Experiment Number : 0, Having results : p : 0.7484422975004176, p1 : 0.6429336555674402, p2 : 0.1108622690128488
Ending the Experiment
Old : 0.51 
Estimated: 0.509087
Experiment Number : 1
Starting Params P:0.8300663873044123, P1:0.9869013812484541, P2:0.17678523429232085
Experiment Number : 1, Having results : p : 0.5264812997822954, p1 : 0.9327549092911148, p2 : 0.03803225293914913
Ending the Experiment
Old : 0.51 
Estimated: 0.5090870000000001
Experiment Number : 2
Starting Params P:0.9530758678292399, P1:0.6233446707414315, P2:0.8761554096110299
Experiment Number : 2, Having results : p : 0.9592296735703926, p1 : 0.4963744783471353, p2 : 0.8081826674430387
Ending the Experiment
Old : 0.51 
Estimated: 0.5090870000000001
Experiment Number : 3
Starting Params P:0.4874231727279612, P1:0.6833544284381429, P2:0.5995486396037447
Experiment Number : 3, Having results : p : 0.47548421615253017, p1 : 0.5568759266418223, p2 : 0.4657653669342056
Ending the Experiment
Old : 0.51 
Estimated: 0.5090870000000001
Experiment Number : 4
Starting Params P:0.1889320851310543, P1:0.7707111545092137, P2:0.4058616562171289
Experiment Number : 4, Having results : p : 0.1966208132709723, p1 : 0.7940633982228822, p2 : 0.43934124095220595
Ending the Experiment
Old : 0.51 
Estimated: 0.5090870000000001
Experiment Number : 5
Starting Params P:0.6292324786551203, P1:0.3485753964986952, P2:0.07956040175660606
Experiment Number : 5, Having results : p : 0.716618341794837, p1 : 0.6261859527269173, p2 : 0.21296600945825353
Ending the Experiment
Old : 0.51 
Estimated: 0.509087
Experiment Number : 6
Starting Params P:0.198248978183301, P1:0.9430491378063666, P2:0.08481491026767818
Experiment Number : 6, Having results : p : 0.3807470990482506, p1 : 0.9804611499574338, p2 : 0.21926302035163953
Ending the Experiment
Old : 0.51 
Estimated: 0.509087
Experiment Number : 7
Starting Params P:0.19787514090135805, P1:0.686761639653904, P2:0.3519101159275405
Experiment Number : 7, Having results : p : 0.21773550196360775, p1 : 0.7598157418971853, p2 : 0.4392991614738705
Ending the Experiment
Old : 0.51 
Estimated: 0.509087
Experiment Number : 8
Starting Params P:0.06262111034298556, P1:0.06637872330276029, P2:0.02184910938516127
Experiment Number : 8, Having results : p : 0.11531603843863829, p1 : 0.7448237124039002, p2 : 0.47835938994929955
Ending the Experiment
Old : 0.51 
Estimated: 0.509087
Experiment Number : 9
Starting Params P:0.5874225251265222, P1:0.04396553180552343, P2:0.28852513813611513
Experiment Number : 9, Having results : p : 0.41315851974437257, p1 : 0.21967154313782408, p2 : 0.712846389496856
Ending the Experiment
Old : 0.51 
Estimated: 0.509087
```

Break down of the outputs :
```
The real Parameters P:0.7, P1:0.6, P2:0.3
Experiment Number : 0
Starting Params P:0.905182959313453, P1:0.9399312012708729, P2:0.5200474107099269
Experiment Number : 0, Having results : p : 0.7484422975004176, p1 : 0.6429336555674402, p2 : 0.1108622690128488
Ending the Experiment
Old : 0.51 
Estimated: 0.509087
```
Line wise breakdown:
1. Contains the original parameter (printed only once)
2. The experiment number
3. The starting estimate of p,p1,p2 for the current experiment
4. Final convergence of the parameters 
5. Old : Tells the probability of heads based on the real parameters
6. Estimated : Tells us the probability of the heads based on the estimated parameters

Points :
1. The fact that we only have the experiment as heads and tail tells  us that we only have the information of the fact that what is the probability of heads
2. These can probably be called as the local solution to the problem , there is not meaning for a global solution
3. All these answers not converging are also solution to the expectation maximisation problem

Question : 
1. What more information can be provided to guide our experiment towards the intended result
