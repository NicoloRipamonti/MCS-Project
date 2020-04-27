library(Matrix)
install.packages("matlib")
noA = readMM("/Users/nicoloripamonti/Desktop/universit??/Magistrale/Secondo Semestre/Metodi del Calcolo Scientifico/Progetto/MCS_Project/Matrici/ex15.mtx")

A = t(A)*A

xe = matrix(rep(1, times = nrow(A)), nrow = nrow(A), ncol = 1)

b = (A %*% xe)

C = chol(A)

y1 = t(C) / b

x = C / y1

ErrRel = norm(x - xe)

ErrAss = ErrRel / xe

R = sqrt(3) * sqrt(3) - 3


