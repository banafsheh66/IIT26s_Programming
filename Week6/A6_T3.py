def writeFile(fileName: str, content: str):
    Filehandle = open(fileName, 'w', encoding='utf-8')
    Filehandle.write(content)
    Filehandle.close()
    return None


def readFile(fileName: str) -> str:
    Filehandle = open(fileName, 'r', encoding='utf-8')
    content = Filehandle.read()
    Filehandle.close()
    return content


def main():
    print("Program starting.")
    print("This program can copy a file.")

    fileName = input("Insert source filename: ")
    desfileName = input("Insert destination filename: ")

    print(f"Reading file '{fileName}' content.")
    file1 = readFile(fileName)
    print("File content ready in memory.")

    print(f"Writing content into file '{desfileName}'.")
    writeFile(desfileName, file1)

    print("Copying operation complete.")
    print("Program ending.")


main()