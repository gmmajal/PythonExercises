def read_densities(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])

        if len(words[:-1]) == 2:
            substance = words[0] + ' ' + words[1]
        else:
            substance = words[0]

        densities[substance] = density
    infile.close()
    return densities

def read_densities_v2(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])
        substance=' '.join(words[:-1])
        densities[substance] = density
    infile.close()
    return densities

def read_densities_v3(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        density = float(line[12:])
        substance=str(' '.join(line[:12].split()))
        densities[substance] = density
    infile.close()
    return densities

def main():
    densities = read_densities('densities.dat')
    densities_v2= read_densities_v2('densities.dat')
    densities_v3= read_densities_v3('densities.dat')
    print("")

if __name__ == "__main__":
    main()