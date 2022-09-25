f = open("fileio_inputFile.txt", "r")
passFile = open("fileio_passfile.txt", "w")
failFile = open("fileio_failfile.txt", "w")
# above can be iterated as lines in a file

count_pass = 0
count_fail = 0
# use f.read() to get whole file content as a string
for line in f :
    if line.split()[2] == "P" :
        passFile.write(line)
        count_pass += 1
    elif line.split()[2] == "F" :
        failFile.write(line)
        count_fail += 1

passFile.write(f"\nTotal passes: {count_pass}")
# extra \n needed here cos bottom record is an F
failFile.write(f"\n\nTotal fails: {count_fail}")

# remember to close any file opens
f.close()
passFile.close()
failFile.close()