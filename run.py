from capitalizer import capitalize as cap
from lowerer import lower as low
from scrambler import scramble as scramb

def main():
    text = "Hello World"

    print(cap.capitalize(text))
    print(low.lower(text))
    print(scramb.scramble(text))

if __name__=="__main__":
    main()