library(Matrix)

start_time_setup <- Sys.time()

#Leggo la matrice A
A = readMM("../Matrici/ex15.mtx")

#Creo soluzione che e' un vettore lungo righe di A con tutti 1
xe = rep(1, times = nrow(A))

#Calcolo b dalla equazione A * xe = b
b = A %*% xe
end_time_setup <- Sys.time()

start_time <- Sys.time()
#Calcolo Cholesky triangolare inferiore della matrice A
R = chol(A)
end_time <- Sys.time()

Memory = object.size(chol(A))

start_time_solving <- Sys.time()
y = solve(t(R), b)

x = solve(R, y)
end_time_solving <- Sys.time()

xe = as.matrix(xe)

#Calcolo errore tra x e xe
Errore = norm(x - xe) / norm(as.matrix(xe))

format(Errore, scientific = TRUE)

#Calcolo dei vari tempi
Time_Setup = end_time_setup - start_time_setup
Time_Chol  = end_time - start_time
Time_Solving = end_time_solving - start_time_solving

Errore
Memory
Time_Setup
Time_Chol
Time_Solving


