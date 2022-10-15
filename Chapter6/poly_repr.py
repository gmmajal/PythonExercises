


def eval_poly_list(poly, x):
    sum = 0
    for power in range(len(poly)):
        sum += poly[power]*x**power
    return sum

def eval_poly_dict(poly, x):
    sum = 0.0
    for power in poly:
        sum += poly[power]*x**power
    return sum

def main():
    list=[0]*101
    list[0]=-0.5
    list[100]=2
    print(list)
    dict={}
    dict[0]=-0.5
    dict[100]=2
    print(dict)
    x=1.05
    list_eval=eval_poly_list(list,1.05)
    dict_eval=eval_poly_dict(dict,1.05)

    assert list_eval,dict_eval

if __name__=='__main__':
    main()