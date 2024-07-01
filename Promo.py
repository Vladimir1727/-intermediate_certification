# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

data = pd.DataFrame(random.sample(['robot', 'human']*10, 10) ,columns={'WhoAmI'})  
data.head() 