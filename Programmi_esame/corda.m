function corda 

L=1; %lunghezza corda
N=1000; %divisioni L=1
tend=100;
t=0;
x=linspace(0,L,N);
dx=x(2)-x(1);
dt=0.01;

v_primo=dx/dt;
v=0.70*v_primo;
a=(v/v_primo)*(v/v_primo);
A=1;
sigma=0.2;
b=1/sqrt(2*pi*sigma);
c=2*sigma^2;

u=zeros(N,1);
u_new=u;
u_old=u;

u_new(1)=A*sin(7*t);

u_new(1)=b*exp(-(t-0.3)^2/c);
u_new(2:N-1)= u(2:N-1)+a*(u(3:N)+u(1:N-2)-2*u(2:N-1));
u_old=u;
u=u_new;

k=0;

while(t<tend)
 %impulso  
  if t<pi/7
     u_new(1)=A*sin(7*t);
   end
 
 %if t<2*sigma
  %u_new(1)=b*exp(-(t)^2/c);
  %end
  
  u_new(2:N-1)=2*u(2:N-1)-u_old(2:N-1)+a*( u(3:N)+u(1:N-2)-2*u(2:N-1) );
  u_old=u;
  u=u_new;
  if mod(k,10)==0 
    plot(x,u,'r');    
    axis([0,L,-A-3,A+3]);
    drawnow;
  end
  t=t+dt;
  k=k+1;
  
end

 
