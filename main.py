import Persona as p

def tree_view(root,n, x):
    print(f' {n}  {root} ({root.pred})')
    n = '   |-'
    if x != 0: n = '     |-'
    for i in root.list_chil:
        tree_view(i, n, root.list_chil.index(i))

def tree_chil(root):
    print(f' {root}')
    for i in range(0, len(root.list_chil)):
        print(f' - {root.list_chil[i]}')

if __name__ == '__main__':

    father = p.Person('Олег', 'м', '1970')
    mother = p.Person('Тамара', 'ж', '1973')
    son1 = p.Person('Петя', 'м', '2000')
    son2 = p.Person('Максим', 'м', '2001')
    sister1 = p.Person('Зоя', 'ж', '2000')
    g_daugther1 = p.Person('Елена', 'ж', '2021')
    sister2= p.Person('Зина', 'ж', '1999')


    father.add_chil(son1)
    father.add_chil(son2)
    father.add_chil(sister1)
    sister1.add_chil(g_daugther1)
    father.add_chil(sister2)


    tree_view(father, '', 0)
    print('\n')
    tree_chil(father)
    print('\n')
    tree_chil(sister1)
    print('\n')

    print(father.action('навесной', 'on'))









