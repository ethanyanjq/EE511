import random
import numpy as np

N = 125
rep = 500
def seq_generate(total, defective): 
    total_seq = [0] * total
    #initialize all the product to be fine
    pre_sample = np.linspace(0, total-1, total)
    def_num = random.sample(list(pre_sample),defective)
    #decide where the 5 defective product will be
    for i in range(defective):
        total_seq[int(def_num[i])] = 1
        #let all the defectives to be 1
    return total_seq
    
total_time = 0
success_detect = 0
for i in range(rep)    :
    seq = seq_generate(125, 5)
    total_time += 1
    if 1 in seq[0:4]:
        success_detect += 1 #if defective detected, counter adds
print("The probability to reject in 5 times is: " + str(success_detect/total_time))

for i in range(N):
    total_time = 0
    success_detect = 0
    for j in range(rep):
        seq = seq_generate(125, 5)
        total_time += 1
        if 1 in seq[0:i]:
            success_detect += 1
    if success_detect/total_time >= 0.95:
        print("The fewest number that should test to reject this lot 95% is: " + str(i))
        break
