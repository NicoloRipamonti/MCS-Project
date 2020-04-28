tic

%Leggo la matrice A
A = Problem.A;

%Creo soluzione che è un vettore lungo righe di A con tutti 1
xe = ones(size(A,1), 1);

%Calcolo b dalla equazione Axe = b
b = A * xe;

%Calcolo Cholesky triangolare inferiore della matrice A 
R = chol(A);

%{
Calcolo la soluzione del sistema:
Siccome per ipotesi di Cholesky A = R * R',
allora risolvere Ax = b diventa
R * R' * x = b,
quindi x = R \ (R' \ b)
(N.B. A\B è l'operatore che risolve Ax=B)
%}

y = R' \ b;
x = R \ y;

toc

%{
Calcolo errore fra x (soluzione calcolata) e xe (soluzione
con tutti 1)
%}

errore = norm(x - xe) / norm(xe);