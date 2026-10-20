# Euler-Maruyama simulation
# Simulate a queue with noise and prints statistics across all the runs  

import numpy as np  
import matplotlib.pyplot as plt 
from time import perf_counter 



# main function 
def simulateQueue(T_final, lambda_arrival, mu_service, C, runs=1):
    start = perf_counter() # starts time
    
    #1: initialising variables 
    sigma = 1.0                        # noise strength
    dt = 0.01                          # Δt / time step  
    N = int(round(T_final / dt)) + 1   # number of time points from T = (N-1)Δt (in this case: 16,001 when T_final = 160)
    all_Q = np.zeros((runs, N))        # One table: Has runs rows and N columns (eg: 100 x 16,001)
    time_points = np.arange(N) * dt   # time in minutes (x-axis) (updated for task b)

    plt.figure() 

    #2: for loop for R simulations (rows)
    for r in range(runs):              
        Q = np.zeros(N) # Fresh queue for this run; Q[0] = 0 (starts at an empty queue for that run. All column 0 values are zero)

        
        #3: time loop over t (columns)
        for t in range(N-1): 
            omega = np.random.randn() # random number from N(0,1) -> more/fewer arrivals than average. 
            Q[t+1] = Q[t] + (lambda_arrival - mu_service * min(Q[t], C)) * dt + sigma * np.sqrt(dt) * omega # 3.4 equation in lab manual translated into python

            if Q[t+1] < 0:
                Q[t+1] = 0 # queue length cannot be negative 

        all_Q[r] = Q # stores the run in row r of the table 
        plt.plot(time_points, Q, linewidth=0.8, alpha=0.7) # curve per run

    # sigma = fixed noise strength. Amplifies the omega
    # Omega = random number each step
    # sigma x sqrt Δt x omega = noise of the step 

    #4: Computing the statistics
    mean_Q = np.mean(all_Q) #average of all values 
    std_Q = np.std(all_Q, ddof=1) # spread of all values around mean 
    occupancy = mean_Q / C # average fraction of C processors across all runs

    end = perf_counter() # ends time 

    #5: printing results 
    print(f"Queue statistics over {runs} runs")
    print("-------------------------------------")
    print(f"Mean queue length: {mean_Q:.2f}")
    print(f"Stdev queue length: {std_Q:.2f}")
    print(f"Mean occupancy: {occupancy * 100:.1f} %")
    print(f"Total run time: {end - start:.2f} seconds")

    #6 plotting results / plot figure (updated for task b)
    plt.xlabel('Time (minutes)')
    plt.ylabel('Queue length')
    plt.title('SDE queue simulation (' + str(runs) + ' runs)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('queue_runs_taskb.png', dpi=500)
    plt.close()


#7: invoke the function 
simulateQueue(120, 400/120, 0.2, 32, 5) #change 5 to 100 for task c
                                          #task d = 100 runs, and 0.1 service rate
