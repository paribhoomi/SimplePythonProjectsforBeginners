import json,os

class ContactBook:
    def __init__(self, filepath="contacts"):
        self.filepath = filepath
        self.contacts = self._load()

    def _load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath) as f:
                return json.load(f)
        return {}
    
    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.contacts, f, indent=2)

    def add(self,name,phone,email):
        self.contacts[name] ={"phone": phone,"email": email}
        self.save()
        print(f"Added {name}")

    def search(self, name):
        c= self.contacts.get(name)
        if c: 
            print(f"{name}: {c['phone']}, {c['email']}")
        else:
            print("Not found")

book = ContactBook()
book.add("Alice" , "123456789" , "alice@gmail.com")
book.search("Alice")
