import json

class ExpenseTracker:
    def __init__(self,file="expenses.json"):
        self.file=file
        self.expenses=self.load()

    def load(self):
        try:
            with open(self.file,"r") as f:
                return json.load(f)
            
        except:
            return []
        
    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.expenses, f, indent=2)

    def add_expense(self,title,amount):
        self.expenses.append({"title": title,"amount": amount})
        self.save()

    def total(self):
        return sum(e["amount"] for e in self.expenses)
    
tracker = ExpenseTracker()
tracker.add_expense("Food",200)
tracker.add_expense("Transport",100)

print("Total spent : ", tracker.total())