with open("practise.txt", "r") as f:
    data =f.read()

new_data = data.replace("python", "c++")
print(new_data) 

with open("practise.txt", "w")as f:
    f.write(new_data)