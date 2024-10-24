function Equazioni_laplace_poisson(input_string)

if(input_string=="laplace")
    %gauss seidel dato potenziale (problema di laplace)
    %parametri fisici

    v=1e05; %potenziale assegnato
    %griglia e condizioni iniziali
    M=50;
    V=zeros(M,M);
    V(20,15:35)=v;
    V(30,15:35)=-v;
    V_old=V;

    delta=zeros(M,M);
    e_r=0.001;
    e_a=0.001;
    delta_max=1000;
    V_max=0;
    x_MAX=1;
    y_MAX=1;

    while(delta_max >= e_a+e_r*abs(V(x_MAX,y_MAX)))

       V_old=V;

        for i=2:M-1
            for j=2:M-1

                V(i,j)=0.25*(V_old(i,j+1)+V_old(i+1,j)+V(i-1,j)+V(i,j-1));

             if((i==30 && j>=15 && j<=35 || i==20 && j>=15 && j<=35)~=1)
                 delta(i,j)=abs(V_old(i,j)-V(i,j));
              end

            end
        end

      V(20,15:35)=v;
      V(30,15:35)=-v;

      delta_max=max(max(delta));
      [x_MAX,y_MAX]=find(delta==delta_max);
      V_max=max(max(V));
      surfc(V);
      drawnow;


    end
    disp("rilassamento completato")
    f2=figure;
    L=10;
    y_=linspace(0,L,M);
    x_=linspace(0,L,M);
    [X,Y]=meshgrid(x_,y_);
    [Ex,Ey]= gradient(-V);
    h=quiver(X,Y,Ex,Ey);%set(h,'LineWidth',2);
    hold on
    contour(X,Y,V);
    hold off
end

 if(input_string=="poisson")
        %metodo di jacopi data carica (problema di poisson)
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
      surfc(V);
      drawnow;


    end
    f2=figure;
    L=10;
    y=linspace(0,L,M);
    x=linspace(0,L,M);
    [X,Y]=meshgrid(x,y);
    [Ex,Ey]= gradient(-V);
    h=quiver(X,Y,Ex,Ey);%set(h,'LineWidth',2);
    hold on
    contour(X,Y,V);
    hold off
 end

    
 if(input_string=="dipolo")
   %sovrarilassamento iterativo

    e_0=8.885e-12;
    f1=figure;
    f2=figure;

    N=101;
    V=zeros(N,N);
    V_new=V;

    Charge=zeros(N,N);
    Charge(50,45)=1;
    Charge(50,55)=-1;

    delta=zeros(N,N);
    e_r=0.0001;
    e_a=0.0001;
    delta_max=1000000;

    V_max=0;

    r=zeros(N,N);
    omega=1.6;
    k=0;
    while(delta_max >= e_a+e_r*abs(V_max))



        for i=2:N-1
            for j=2:N-1

                V_n=V;
                r(i,j)=0.25*( V(i+1,j)+V_new(i-1,j)+V(i,j+1)+V_new(i,j-1))+(0.25)*Charge(i,j)-V(i,j);
                V_new(i,j)=V(i,j)+omega*r(i,j);

                %if i~=50 && j~=60 && j~=40
                 delta(i,j)=abs(V_n(i,j)-V_new(i,j));
                % end

            end 
        end  


        V=V_new;
        delta_max=max(max(delta));
        V_max=max(max(V));



        if mod(k,100)==0
            figure(f1);
            surfc(V);
            drawnow;

        end


    end
    disp("rilassamento raggiunto")
    figure(f2);
    L=100;
    y=linspace(0,L,N);
    x=linspace(0,L,N);
    [X,Y]=meshgrid(x,y);

    [Ex,Ey]= gradient(-V);

    h=quiver(X,Y,Ex,Ey);
    %set(h,'LineWidth',2);
    hold on
    contour(X,Y,V);
    hold off
 end
    








end
