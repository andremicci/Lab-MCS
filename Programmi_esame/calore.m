function calore(input_string)
if(input_string=="crank_nicolson")
    %soluzione equazione del calore con il metodo crank nicolson
    
    k=2;
    L=10;
    
    N=100;
    x=linspace(0,L,N);

    dx=x(2)-x(1);
    dt=0.001;
    eta=(2*k*dt)/(dx*dx)
    tmax=1;
    
    T=zeros(N,1);
    T_new=T;
    
    %CONDIZIONI INIZIALI: picco di temperatura al centro
    T0=100;
    T(N/2)=T0;
   

    t=dt;
    v=ones(N-3,1)*(-1);
    M=eye(N-2,N-2)*(2/eta +2)+diag(v,1)+diag(v,-1);
    M_inv=inv(M);
    
    while(t<tmax)

        T_=zeros(N,1);
        T_(3:N-2)=T(2:N-3)+(2/eta -2)*T(3:N-2)+T(4:N-1);
        T_(2)=T(1)+T(1)+(2/eta -2)*T(2)+T(3);
        T_(N-1)=T(N)+T(N)+(2/eta-2)*T(N-1)+T(N-2);

        T_new(2:N-1)=M_inv*T_(2:N-1);
        T=T_new;

        plot(x,T,"-g");
        pause(0.001);
        %axis([0 L 0 50]);
        
        %PER MOSTRARE LA SOLUZIONE SCOMMENTA
        %hold on;
        %sigma=sqrt(2*k*t);
        %x0=L/2;
        %sol=20*(1/sqrt(2*pi*sigma))*exp(-((x-x0).^2/(2*sigma^2)));
        %plot(x,sol,"-r");
        %old off;
        
        drawnow;
        t=t+dt;

    end
end
    
  if(input_string=="metodo_esplicito")
       
    k=2;
    L=10;
    
    N=100;
    x=linspace(0,L,N);

    dx=x(2)-x(1);
    dt=0.001;
    eta=(2*k*dt)/(dx*dx)
    tmax=1;
    
    T=zeros(N,1);
    T_new=T;
    
    %CONDIZIONI INIZIALI: picco di temperatura al centro
    T0=100;
    T(N/2)=T0;

    t=dt;
    
    while (t<tmax)

        T_new(1)=T(1)+eta*(T(2)-2*T(1));
        T_new(N)=T(N)+eta*(T(N-1)-2*T(N));

        T_new(2:N-1)=T(2:N-1)+eta*(T(1:N-2)+T(3:N)-2*T(2:N-1));
        T=T_new;
        
        plot(x,T_new,"g-");
        
        % axis([0 L 20 T0/2]);
        drawnow;
        t=t+dt;
    end
  end
    

end