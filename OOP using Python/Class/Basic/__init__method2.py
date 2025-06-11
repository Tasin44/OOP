class Counter:
    def __init__(self, start):
        self.st = start    # Instance variable
    
    def increment(self):   # No need to pass 'st' here
        self.st += 3       # Accesses and updates self.st
        return self.st
        
    def decrement(self):
        self.st -= 2
        return self.st 

ct1 = Counter(7)
print(ct1.increment())  # Output: 10
print(ct1.decrement())  # Output: 8



'''
if you define instance variables (like self.st) in __init__, then inside other methods of the class, you don’t necessary to pass them as parameters again. 
Just use self.st.
💡 Why?

Because:

    self.st = start in __init__ creates an instance variable.

    That variable is then accessible in all methods of the same instance via self.st.
    
Like if we do:

🔁 If You Had Written This Instead (❌ Wrong):

def increment(self, st):  # ❌ You're passing 'st' explicitly, unnecessary and confusing
    st += 3
    return st

This would not modify self.st, and would only change the value locally in that method.

🧠 Rule of Thumb:

    ✅ Use self.<name> for values that belong to the object's state.

    ❌ Avoid passing them again in methods unless you want to override or use new inputs.
'''
