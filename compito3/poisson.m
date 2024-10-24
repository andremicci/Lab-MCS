function poisson
%gauss seidel data carica (problema di poisson)

%parametri fisici
e_0=8.885e-12;
q=1e-06;

%griglia e inizializzazione
M=50;
V=zeros(M,M);


carica=zeros(M,M);
carica(20,15:35)=q;
carica(30,15:35)=-q;

%precisione
delta=zeros(M,M);
e_r=0.001;
e_a=0.001;


delta_max=100000;
V_max=0;


while(delta_max >= e_a+e_r*abs(V_max))
     
    
    for i=2:M-1
            
        for j=2:M-1
                V_n=V(i,j);
                V(i,j)=0.25*(V(i+1,j)+V(i-1,j)+V(i,j+1)+V(i,j-1))+(1/(4*e_0))*carica(i,j);
                delta(i,j)=abs(V_n-V(i,j));
            
        end
    end  
    
  delta_max=max(max(delta));
  V_max=max(max(V));
  surf(V);
  drawnow;
    
end




                                 