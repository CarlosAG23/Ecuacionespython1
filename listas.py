filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = []
for filename in filenames:
    if filename.endswith(".hpp"):
        newfilenames.append(filename.replace(".hpp", ".h"))
    else:
        newfilenames.append(filename)

print(newfilenames)
