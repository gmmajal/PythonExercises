def count_substr(dna,sub_str):
    return dna.count(sub_str)
dna='ACGTTACGGAACG'
sub_str='ACG'
occurence=count_substr(dna,sub_str)
print occurence
