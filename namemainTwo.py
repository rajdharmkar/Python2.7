# file namemainTwo.py
import namemainOne

print("top-level in namemainTwo.py")
namemainOne.func()

if __name__ == "__main__":
    print("namemainTwo.py is being run directly")
else:
    print("namemainTwo.py is being imported into another module")
