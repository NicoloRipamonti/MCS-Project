library(Matrix)
library(e1071)

##MATRIX EX15:
ex15= readMM("../Matrici/ex15.mtx")

xe = rep(1, times = nrow(ex15))

b = ex15 %*% xe

start_time <- Sys.time()
C = chol(ex15)
end_time <- Sys.time()

Memory = object.size(chol(ex15))

y = solve(t(C), b)

x = solve(C, y)


Time  = end_time - start_time
format(Time, scientific = TRUE)
xe = as.matrix(xe)

Errore = norm(x - xe) / norm(as.matrix(xe))
format(Errore, scientific = TRUE)

Memory
Time
