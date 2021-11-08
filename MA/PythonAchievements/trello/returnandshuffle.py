import random 
def shuffle(word):
     return '' .join(random.sample(word, len(word)))

print(shuffle("random"))
print(shuffle("random"))
print(shuffle("random"))