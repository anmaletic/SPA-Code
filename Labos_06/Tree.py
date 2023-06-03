class Tree:
    def __init__(self, v, l=None, d=None):
        self.value = v
        self.left = l
        self.right = d

    def preorder(self):
        s = str(self.value)
        if self.left != None:
            s += self.left.preorder()
        if self.right != None:
            s += self.right.preorder()
        return s

    def inorder(self):
        s = ''
        if self.left != None:
            s += self.left.inorder()
        s += str(self.value)
        if self.right != None:
            s += self.right.inorder()
        return s

    def postorder(self):
        s = ''
        if self.left != None:
            s += self.left.postorder()
        if self.right != None:
            s += self.right.postorder()
        s += str(self.value)
        return s

    def makeBST(a):
        root = Tree(a[0])
        for e in a[1:]:
            tmp = root
            gotovo = False
            while not gotovo:
                if tmp.value < e:
                    if tmp.right == None:
                        tmp.right = Tree(e)
                        gotovo = True
                    else:
                        tmp = tmp.right
                else:
                    if tmp.left == None:
                        tmp.left = Tree(e)
                        gotovo = True
                    else:
                        tmp = tmp.left
        return root
    
    def minv(self):
        while self.left != None:
            self = self.left
        return self.value
            
    def buc(self):
        if self.left == None and self.right == None:
            return 0
        else:
            bul = 0
            bud = 0
            if self.left != None:
                bul = self.left.buc()
            if self.right != None:
                bud = self.right.buc()
            return bul + bud + 1

    def listova(self):
        if self.left == None and self.right == None:
            return 1
        else:
            bL = 0
            bD = 0
            if self.left != None:
                bL = self.left.listova()
            if self.right != None:
                bD = self.right.listova()
            return bL + bD

    def dubina(self):
        if self.left == None and self.right == None:
            return 0
        else:
            dL = 0
            dD = 0
            if self.left != None:
                dL = self.left.dubina()
            if self.right != None:
                dD = self.right.dubina()
            return max(dL, dD) + 1
        
    def brisiKorijen(self):
        if self.left == None and self.right == None:
            self = None
        elif self.left  != None:
            tmp = self.left
            if self.right != None:
                desno = self.left.right
                while desno.right != None:
                    tmp = desno
                    desno = desno.right
                self.value = desno.value
                tmp.right = None
            else:
                tmp = self.right
                self = self.left
                self.right = tmp
        else:
            tmp = self.right
            if self.right.left != None:
                lijevo = self.right.left
                while lijevo.left != None:
                    tmp = lijevo
                    lijevo = lijevo.left
                self.value = lijevo.value
                tmp.left = None
            else:
                tmp = self.left
                self = self.right
                self.left = tmp