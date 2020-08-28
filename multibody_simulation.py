
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
        
def run_multibody_simulation(ids, wealth, num_transactions):
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

    person = []

    for i in range(len(wealth)):
        person.append(Person(ids[i], wealth[i]))
        # person[i].transactions.append(person[i].initial_endowment)

    ## find random price
    costs = (np.min(wealth), np.max(wealth))
    range_persons = range(len(person))

    tmp = [j.wealth for j in person]
    total = np.array(tmp).sum()

    for i in range(num_iterations):

        ## calculate parameters

        ## capitalist class
        idxs = random.sample(range_persons, 2)
        banker = idxs[0]
        capitalist = idxs[1]
        capital = np.random.randint(costs[0], costs[1], 1)[0]
        interest_rate = np.random.rand(1)[0]
        interest = capital * interest_rate

        ## working and consumer class
        ## TODO : Deterministic portion to make sure the n_worker or consuemrs is never zero
        ## problem right now is that sometimes you can get a small enough n, that the difference is 0,
        ## which means a division by zero

        n = np.random.randint(10, len(person), 1)[0]
        worker_index = np.random.choice(range_persons, n)
        worker_index = np.setdiff1d(worker_index, idxs)

        m = np.random.randint(10, len(person), 1)[0]
        consumer_index = np.random.choice(range_persons, m)
        consumer_index = np.setdiff1d(consumer_index, idxs)

        quantity = m

        price = np.random.randint(10, len(person), 1)[0]
        wages = np.random.randint(10, len(person), 1)[0]

        # price and profit

        consumer_check = np.array([person[j].wealth for j in consumer_index])

        #             person[j].transactions.append(person[j].wealth)

        # do the exchanges , check that capitalist is not banker, and that the relevant amount exists for banker
        if (banker != capitalist and person[banker].wealth >= capital
                and np.all(consumer_check > price)):
            person[banker].wealth = person[banker].wealth - capital
            person[capitalist].wealth = person[capitalist].wealth + capital

            for j in worker_index:
                person[capitalist].wealth = person[capitalist].wealth - wage
                person[j].wealth = person[j].wealth + wage
        #             person[j].transactions.append(person[j].wealth)

            for k in consumer_index:
                person[k].wealth = person[k].wealth - price
                person[capitalist].wealth = person[capitalist].wealth + price

            person[capitalist].wealth = person[capitalist].wealth - interest
            person[banker].wealth = person[banker].wealth + interest

        
    return person 


def main():

    ids = np.linspace(start=1, stop=100, num=10000, dtype=int)
    wealth = np.random.randint(998, 1000, 10000)
    result = run_multibody_simulation(ids, wealth, 100000)
    income_endpoint = [result[i].wealth for i in range(len(result))]
    return (result, np.sort(income_endpoint)
    
if __name__="__main__":
     main()
