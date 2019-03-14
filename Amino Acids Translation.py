from Bio import SeqIO
amino_acid = {}
not_amino_acid_keys=["B","J","O","U","Z","X"]
amino_acid_keys=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

open_file= open('yeast_aaseqs.txt')
output_file=open('output10.txt','w')
for seq_record in SeqIO.parse(open_file, "fasta"):
    output=[]
    seq_record.seq = str(seq_record.seq).replace(str(not_amino_acid_keys),'')
    length = len(seq_record.seq)
    for aa in seq_record.seq:
        if amino_acid.has_key(aa):
            amino_acid[aa]+=1
        else:
            amino_acid[aa]=1
    output.append(seq_record.id)
    for i in amino_acid_keys:
        if i in amino_acid:
            fraction = amino_acid[i]/ float(length)
            output.append(str(round(fraction, 3)))
        else:
            output.append(str(0.0))
    output.append('\n')
    output_file.write('\t'.join(output))
    del output[:]
    amino_acid.clear()
open_file.close()
output_file.close()

