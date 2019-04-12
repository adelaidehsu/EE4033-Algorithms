import re

class Parser():
    def __init__(self, inputPath):
        self.inputPath = inputPath
        inputFile = open(inputPath)
        inputString = inputFile.read()
        self.splitArray = inputString.split()
        self.processedArray = []

        for i in range(len(self.splitArray)):
            specialChars = r",.;:?!~[]{}()<>\"\'"
            wordLen = len(self.splitArray[i])

            # does not contain any letter
            if not (re.search('[a-zA-Z]', self.splitArray[i])): continue
            # first character is in specialChars
            while any(elem in self.splitArray[i][0] for elem in specialChars):
                self.splitArray[i] = self.splitArray[i][1:]
            # last character is in specialChars
            while any(elem in self.splitArray[i][-1] for elem in specialChars):
                self.splitArray[i] = self.splitArray[i][:-1]
            
            self.processedArray.append(self.splitArray[i])

    def queryList(self):
        ret = self.processedArray.copy()
        return ret
    def length(self):
        return len(self.processedArray)
    def query(self, i):
        return self.processedArray[i]