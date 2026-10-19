# Euler-Maruyama 

import numpy as np  
import matplotlib.pyplot as plt 
from time import perf_counter 


# main function 
def simulateQueue(T_final, lambda_arrival, mu_service, C, runs=1):
    start = perf_counter() # starts time
    
    #1: initialising variables 
    sigma = 1.0                        # noise strength 
    dt = 0.01                          # Δt / time step  
    N = int(round(T_final / dt)) + 1   # number of time points (from T = (N-1)Δt). This should be around 16,000 + 1 steps    
    all_Q = np.zeros((runs, N))        # table of each simulation run (should be 1.6m updates and 1,600,100 cells)

    #2: for loop for R simulations 
    for r in range(runs):              
        Q = np.zeros(N)

        
        #3: for loop for time loop t 
        for t in range(N-1): 
            omega = np.random.randn()
            Q[t+1] = Q[t] + (lambda_arrival - mu_service * min(Q[t], C)) * dt + sigma * np.sqrt(dt) * omega #3.4 equation in lab manual translated into python

            if Q[t+1] < 0:
                Q[t+1] = 0 # hard coding to prevent negative queue 

        all_Q[r] = Q # copies 1600 + 1 values into row r for the table


    #4: Computing the statistics
    mean_Q = np.mean(all_Q) #average of all values 
    std_Q = np.std(all_Q, ddof=1) # 
    occupancy = mean_Q / C #

    end = perf_counter() #ends time 

    #5: printing results 
    print(f"Queue statistics over {runs} runs")
    print("-------------------------------------")
    print(f"Mean queue length: {mean_Q:.2f}")
    print(f"Stdev queue length: {std_Q:.2f}")
    print(f"Mean occupancy: {occupancy * 100:.1f} %")
    print(f"Total run time: {end - start:.2f} seconds")


#6: invoke the function 
simulateQueue(160, 4., 0.4, 16, 100)