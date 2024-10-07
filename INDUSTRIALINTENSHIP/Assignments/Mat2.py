import matplotlib.pyplot as plt
X = [0, 2, 4, 6, 8]
Y1 = [0, 4, 16, 36, 64]
Y2 = [0, 2, 4, 6, 8]
plt.figure(figsize=(8, 6))
plt.plot(X, Y1, label="Y1: Quadratic", linestyle='--')
plt.plot(X, Y2, label="Y2: Linear", linestyle=':')
plt.title("Assignment 2")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.grid(True)
plt.show()
