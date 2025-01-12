'''
a={"Bellari":"BITM"} Dictonary
print(a)
a={"1,8,7,9"} Set
print(a)
'''
'''
rs=int(input(13))
five=rs/5
two=rs%5%2
one=rs%5%2//1
total=five+two+one
print(total,five,one)

input(3)
12 0 9
output(13)
7 1 10 99 3
output(100)

input(4)
22 0 21
output(40)
''''''
sie=int(input())
l=list(map(int,input().split))

class Cricketer:

#initializing
   def _init_(self, name):
      self.name=name
      print(f'Cricketer {self.name} created.')

#Deleting(Calling destructor)
   def _del_(self):
      print(f'Destructors called, Cricketer {self.name} deleted.')

#creating objects of the Cricketer class
cricketer1=Cricketer("MSD")
cricketer2=Cricketer("Jadeja")

#deleting objects
del cricketer1
del cricketer2
'''


def find_winning_party(n, votes):
    # Edge case: if there's only one vote, return that party number.
    if n == 1:
        return votes[0]

    # Step 1: Count the frequency of each party's votes.
    vote_count = {}
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1

        # Step 2: Check if any party has more than half of the votes.
        majority = n // 2
        for party, count in vote_count.items():
            if count > majority:
                return party

                # Step 3: If no party has a majority, return -1.
                return -1


    # Example Usage:

n = 68
votes = [1, 1, 2, 2, 2, 3]
print(find_winning_party(n, votes))  # Output: 2






            

