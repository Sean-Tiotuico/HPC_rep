# Euler-Maruyama 
import numpy as np  
import matplotlib.pyplot as plt 
from time import perf_counter 


# main function 
def simulateQueue(T_final, lambda_arrival, mu_service, C, runs=1):
    start = perf_counter() 
    
    #1: initialising variables 
    sigma = 1.0  
    dt = 0.01 
    N = int(round(T_final / dt)) + 1  
    all_Q = np.zeros((runs, N))   

    #2: for loop for R simulations 
    for r in range(runs):
        Q = np.zeros(N)

        
        #3: for loop for time loop t 
        for t in range(N-1): 
            omega = np.random.randn()
            Q[t+1] = Q[t] + (lambda_arrival - mu_service * min(Q[t], C)) * dt + sigma * np.sqrt(dt) * omega

            if Q[t+1] < 0:
                Q[t+1] = 0

        all_Q[r] = Q 


    #4: Computing the statistics
    mean_Q = np.mean(all_Q)
    std_Q = np.std(all_Q, ddof=1)
    occupancy = mean_Q / C 

    end = perf_counter() 


    #5: printing results 
    print(f"Queue statistics over {runs} runs")
    print("-------------------------------------")
    print(f"Mean queue length: {mean_Q:.2f}")
    print(f"Stdev queue length: {std_Q:.2f}")
    print(f"Mean occupancy: {occupancy * 100:.1f} %")
    print(f"Total run time: {end - start:.2f} seconds")


#6: invoke the function 
simulateQueue(160, 4., 0.4, 16, 100)