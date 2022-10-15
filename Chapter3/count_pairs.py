def count_pairs(dna,pair):
    return dna.count(pair)

dna='ACTGCTATCCATT'
pair='AT'

occurence=count_pairs(dna,pair)
print occurence


