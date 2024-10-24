function laplace 
%gauss seidel dato potenziale (problema di laplace)
%parametri fisici

v=100; %potenziale assegnato

%griglia e condizioni iniziali
M=50;
V=zeros(M,M);
V(20,15:35)=v;
V(30,15:35)=-v;

delta=zeros(M,M);
e_r=0.001;
e_a=0.001;

delta_max=1000;
V_max=0;
V_new=V;
V_old=V;
q=0;
x=1;
y=1;
while(delta_max >= e_a+e_r*abs(V_new(x,y)))
    
   V_old=V_new;
   
    for i=2:M-1
        for j=2:M-1
           
            V_new(i,j)=0.25*(V_old(i,j+1)+V_old(i+1,j)+V_new(i-1,j)+V_new(i,j-1));
            
         if((i==30 && j>=15 && j<=35 || i==20 && j>=15 && j<=35)~=1)
             delta(i,j)=abs(V_old(i,j)-V_new(i,j));
          end
            
        end
    end
    
  V_new(20,15:35)=v;
  V_new(30,15:35)=-v;
  
 delta_max=max(max(delta))
 [x,y]=find(delta==delta_max);
  V_max=max(max(V_new));
  surf(V_new);
  drawnow;
  q=q+1
  
  e_a+e_r*abs(V_max)
 
end