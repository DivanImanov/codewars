# https://www.codewars.com/kata/62d34faad32b8c002a17d6d9

def fifo(n, reference_list):
    mas = [-1 for i in range(n)]
    n_el = 0
    for i in reference_list:
        if i not in mas:
            if len(mas) < n:
                mas.insert(n_el, i)
            else:
                if n_el >= n:    
                    n_el = 0
                mas[n_el] = i
            n_el += 1
    return mas
