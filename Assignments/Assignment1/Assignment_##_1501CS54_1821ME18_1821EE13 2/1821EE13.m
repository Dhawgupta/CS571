
clc
clear all;
Master_trial= 100; 
p=0.7;p1=0.6;p2=0.3;

N= 10; % no. of tosses 
tot=N;
while tot~=round(p*N)
    % generate random numbers
    sz=[N, 1];
percentage=p;
SEL = rand(sz) < percentage;
SEL=double(SEL');
tot=sum(SEL);

end

l=length(SEL);
c1= sum(SEL); % no. of occurence of coin 1
c2=N-c1; % no. of occurence of coin 2
tot1=c1;
s1=0;
  while tot1~= round(p1*c1) 
 % generate random numbers of sequence for coin1
 sz=[c1, 1];
percentage=p1;
SEL1 = rand(sz) < percentage;
 SEL1=double(SEL1');
 tot1=sum(SEL1);
  end
tot2=c2;
s2=0;
  while tot2~= round(p2*c2) 
 % generate random numbers of sequence for coin2
 sz=[c2, 1];
percentage=p2;
SEL2 = rand(sz) < percentage;
 SEL2=double(SEL2');
 tot2=sum(SEL2);
  end
  %% creating final sequence
for i=1:l
    g= SEL(1,i);
     if g==1
         s1=s1+1;
       toss(1,i)=SEL1(1,s1);  
        else 
         if g==0
             s2=s2+1;
             toss(1,i)=SEL2(1,s2); 
         end
     end
end
%%
% toss=horzcat(SEL1,SEL2); t_s=0;
E= zeros(1,N);

for q= 1:Master_trial
     p=(p);p1=(p1);p2=(p);
          
     E= zeros(1,N);sum_p1=0;t_s=0;
for t=1:N
    E(1,t)= ((p*p1^toss(1,t))*((1-p1)^(1-toss(1,t))))/((p*p1^toss(1,t))*((1-p1)^(1-toss(1,t)))+ ((1-p)*p2^toss(1,t))*((1-p2)^(1-toss(1,t))));
    sum_p1(1,t)= toss(1,t)*E(1,t);
    if toss(1,t)==1
        t_s=t_s+1;
    end
end

   
p= (sum(E)/N);
p1=(sum(sum_p1)/sum(E));
p2= ((t_s-sum(sum_p1))/(N-sum(E)));

R(q,:) = [p p1 p2];
EE(q,:)=E;
SAM(q,:)=sum_p1;
T_S(q,:)=t_s;
t_s=0;

end
 clc



   
 


         

