syms x; %obtenemos la variable del paquete
f = 1/sqrt(x^3 + 1); %definimos la funcion
taylor(f,x,'Order',10) % calculamos la serie hasta el orden 10