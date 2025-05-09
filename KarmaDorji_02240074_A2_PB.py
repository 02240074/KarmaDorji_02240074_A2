class PokemonBinder:
    def __init__(self):
        self.cards = []
    
    def add_card(self):
        try:
            num = int(input("Enter Pokemon number (1-10): "))
            if num < 1 or num > 100:
                print("Please enter 1-10")
                return
            
            if num in self.cards:
                print("You already have this card!")
            else:
                self.cards.append(num)
                print(f"Added Pokemon #{num}")
        except:
            print("Please enter a number!")
    
    def show_cards(self):
        if not self.cards:
            print("Your binder is empty!")
            return
        
        print("\nYour Pokemon Cards:")
        for num in sorted(self.cards):
            print(f"#{num}")
        
        total = len(self.cards)
        print(f"\nTotal cards: {total}/100")
        print(f"Completion: {total}%")
    
    def reset_binder(self):
        if input("Are you sure? (y/n): ").lower() == 'y':
            self.cards = []
            print("Binder cleared!")
    
    def run(self):
        print("Pokemon Card Binder")
        while True:
            print("\nMenu:")
            print("1. Add a Pokemon card")
            print("2. View your collection")
            print("3. Reset binder")
            print("4. Exit")
            
            choice = input("Choose (1-4): ")
            
            if choice == '1':
                self.add_card()
            elif choice == '2':
                self.show_cards()
            elif choice == '3':
                self.reset_binder()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Please choose 1-4")

if __name__ == "__main__":
    binder = PokemonBinder()
    binder.run()