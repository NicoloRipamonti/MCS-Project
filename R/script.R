library(Matrix)
library(e1071)

start_time_setup <- Sys.time()
A = readMM("../Matrici/ex15.mtx")

xe = rep(1, times = nrow(A))

b = A %*% xe
end_time_setup <- Sys.time()

start_time <- Sys.time()
R = chol(A)
end_time <- Sys.time()

Memory = object.size(chol(A))

start_time_solving <- Sys.time()
y = solve(t(R), b)

x = solve(R, y)
end_time_solving <- Sys.time()

xe = as.matrix(xe)

Errore = norm(x - xe) / norm(as.matrix(xe))

format(Errore, scientific = TRUE)

Time_Setup = end_time_setup - start_time_setup
Time_Chol  = end_time - start_time
Time_Solving = end_time_solving - start_time_solving

Errore
Memory
Time_Setup
Time_Chol
Time_Solving

