library(Matrix)
library(e1071)

A = readMM("/Users/nicoloripamonti/Desktop/universit??/Magistrale/Secondo Semestre/Metodi del Calcolo Scientifico/Progetto/MCS_Project/Matrici/ex15.mtx")

A = t(A)*A

sol = rep(1, times = nrow(A))

b = A * sol

C = chol(A)

y1 = t(C) / b

x1 = C / y1

Err.ass = norm(x1 - sol)
