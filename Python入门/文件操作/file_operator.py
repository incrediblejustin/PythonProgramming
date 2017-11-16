infile_name = input("please input file name you want to  backup: \n")
infile = open(infile_name, "r")

pos = infile_name.rfind(".")
outfile_name = infile_name[0:pos] + "[back_up]" + infile_name[pos:]

outfile = open(outfile_name, "w")
while True:
    buffer = infile.read(1024)
    if buffer:
        outfile.write(buffer)
    else:
        break

infile.close()
outfile.close()