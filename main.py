from readin import ReadIn

def main():
    filename = input("Enter filename: ")
    read = ReadIn(filename)
    read.run()

if __name__ == "__main__":
    main()
