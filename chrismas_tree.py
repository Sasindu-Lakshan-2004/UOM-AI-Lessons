def chrismas_tree(hight):
     for i in range(1,hight+1):
        # number of stars = 2*i - 1
        stars = '*' * (2 * i - 1)
        print(stars.center(2 * hight - 1))
chrismas_tree(5)        