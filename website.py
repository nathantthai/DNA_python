input_file=open('input.txt','r').readlines()

for line in input_file:
    line.rstrip('\n')
    print '<h3><b>'+line+'</b></h3>'
