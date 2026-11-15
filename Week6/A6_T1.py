def readfile(filename: str) -> str:
    filehandler = open(filename, "r" , encoding="UTF-8")
    content = ""
    Row = filehandler.readline()
    while Row != "":
        content += Row
        Row = filehandler.readline()
    filehandler.close()
    return content
def main():
    print("program starting.")
    print("This program can read a file")
    filename =input("Insert filename:")
    filecontent = readfile(filename)
    print(f"### start {filename} ###")
    print(filecontent)
    print(f"### end {filename} ###")
    print("program ending.")
    return None
    # Your code logic here
main()    