from Bio import SeqIO
db_GC=open("rosalind_gc.txt","r")
percentage={}

for seq_record in SeqIO.parse(db_GC, "fasta"):
    length = len(seq_record.seq)
    G = seq_record.seq.count("G")
    C = seq_record.seq.count("C")
    fraction=(G+C)*100.0/length
    percentage[seq_record.id]=round(fraction,4)
high_GC=max(percentage, key=percentage.get)
print "{0}\n{1}".format(high_GC, percentage[high_GC])
