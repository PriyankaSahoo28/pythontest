def mul(i,j):
    return str(i*j)
print(mul(10,20))


def sub(i,j):
    return str(i-j)
print(sub(30,10))



def div(i,j):
    return str(i/j)
print(div(20,10))



def writeFile(path,data):
    myFile = open(path, 'w')
    myFile.write(data)
    myFile.close()

def findAge(name,age,inputName):

    for i in range(len(name)):
        if (name[i] == inputName):
            return inputName+" : "+str(age[i])

inputName=input("Enter a Name: ")
name = ["a", "b", "c"]
age = [10, 12, 13]
data=findAge(name,age,inputName)
writeFile("file.txt",data)