Income Inequality Simulation

import random
import numpy as np

class Person():
    def __init__(self, id, wealth):
        self.id=id
        self.initial_endowment=wealth
        self.wealth=wealth
        self.transactions=[]

    def __repr__(self):
        return 'person ' + str(self.id) + ' has ' + '$' + str(self.wealth)

def run_simulation(ids, endowments, num_transactions):
    
    """
            
    Parameters
    ..........
    
    ids : list
        primary key identifiers 
    
    wealth : list 
        wealth per person 
    
    num_iterations : int 
        number of times to iterate 
        
    Returns
    ........
    
    person: list[Person]
        list of person objects 
    
    """

    person=[]

    ## intialize person wealth 
    for i in range(len(ids)):
        person.append(Person(ids[i],endowments[i]))
        person[i].transactions.append(person[i].initial_endowment)
    
    ## find random price 
    costs=(np.min(endowments),np.max(endowments))
    range_persons=range(len(ids))
    for i in range(num_transactions):
        for j in range(len(ids)):

            idxs = random.sample(range_persons, 1)
            idx1 = j ; idx2 = idxs[0]
            cost = np.random.randint(costs[0],costs[1])
            if (idx1 != idx2 and person[idx1].wealth >= cost and  person[idx2].wealth>= cost) :
                person[idx1].wealth=person[idx1].wealth -  cost
                person[idx2].wealth=person[idx2].wealth + cost
            
            person[idx1].transactions.append(person[idx1].wealth)
        

    return person


def main():
    ids = np.linspace(start=1, stop=100, num=100, dtype=int)
    wealth = np.random.randint(998, 1000, 100)
    result = run_simulation( ids, wealth, 10000)
    income_endpoint = [result[i].wealth for i in range(len(result))]
    return ( result, np.sort(income_endpoint))

if __name__="__main__":
     main()
