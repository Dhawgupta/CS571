h=readfis('inverted_pendulum.fis');
a=input(' angular position=');
b=input(' angular velocity=');
I=evalfis([a b],h); % current min and max range may be set
disp(['output current in amperes is : ', num2str(I)]);
figure(1)
plotmf(h,'input',1)


theta=a;
omega=b;
m=1;
l=1;
T=1;
g=9.8;


theta_new= a + b*t+ (t^2)/2*((3*T*I)/(m*l*l)- (3*g*cos(a))/(2*l));
omega_new= b+ t*((3*T*I)/(m*l*l)- (3*g*cos(a))/(2*l));

a1=(3*T*I)/(m*l*l*2)- (3*g*cos(a))/(4*l);
b1=b;
c1=a;

r = roots([a1,b1,c1]);
% disp(((r)));
disp(['the time taken to reverse to the original position is : ', num2str(r(1,1))]);



