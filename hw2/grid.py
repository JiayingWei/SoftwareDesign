def grid(n):
    hori =  ('+' + '-' * 4) * n + '+'
    vert =  ('|' + ' ' * 4) * n + '|'
    def pvert():
        print vert
        print vert
        print vert
        print vert

    for i in range(0,n):
        print hori
        pvert()
    print hori

grid(4)