
def x (name,location):
  print()
  print(f"Hi {name}!")
  print(f"whats the whether like in {location}?")

def main():
  x_name = input("What is your name?: ")
  x_location = input("Where are you from?: ")
  x(x_name,x_location)

main()