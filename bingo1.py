
import random

player1 =['' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' ,'' , '' , '' , '' , '' , '' , '' , '' ,'' , '' ,'' ,'' ]

B1 = []     
for i in range(1 , 6):
    B = random.randint(1 , 15)
    while (B in B1):
        B =random.randint(1 , 15)
    while not (B in B1):
        B1.append(B)
    
        
player1[0] = B1[0]
player1[5] = B1[1]
player1[10] = B1[2]
player1[15] = B1[3]
player1[20] = B1[4]

I1 = []
for i in range(1,6):
    I = random.randint(16 , 30)
    while (I in I1):
        I =random.randint(16 , 30)
    while not (I in I1):
        I1.append(I)
    
    
player1[1] = I1[0]
player1[6] = I1[1]
player1[11] = I1[2]
player1[16] = I1[3]
player1[21] = I1[4]

N1 = []
for i in range(1,6):
    N =random.randint(31 , 45)
    while (N in N1):
        N =random.randint(31 , 45)
    while not (N in N1):
        N1.append(N)
    
    
player1[2] = N1[0]
player1[7] = N1[1]
player1[12] = N1[2]
player1[17] = N1[3]
player1[22] = N1[4]

G1 = []
for i in range(1 , 6):
    G = random.randint(46 , 60)
    while (G in G1):
        G =random.randint(46 , 60)
    while not (G in G1):
        G1.append(G)
    
    
player1[3] = G1[0]
player1[8] = G1[1]
player1[13] = G1[2]
player1[18] = G1[3]
player1[23] = G1[4]


O1 = []
for i in range(1,6):
    O = random.randint(61 , 75)
    while (O in O1):
        O =random.randint(61 , 75)
    while not (O in O1):
        O1.append(O)
    
    
player1[4] = O1[0]
player1[9] = O1[1]
player1[14] = O1[2]
player1[19] = O1[3]
player1[24] = O1[4]

player2 = ['' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' ,'' , '' , '' , '' , '' , '' , '' , '' ,'' , '' ,'' ,'' ]

B2 = []      
for i in range(1 , 6):
    B = random.randint(1 , 15)
    while (B in B2):
        B =random.randint(1 , 15)
    while not (B in B2):
        B2.append(B)
    
    
player2[0] = B2[0]
player2[5] = B2[1]
player2[10] = B2[2]
player2[15] = B2[3]
player2[20] = B2[4]

I2 = []
for i in range(1,6):
    I = random.randint(16 , 30)
    while (I in I2):
        I =random.randint(16 , 30)
    while not (I in I2):
        I2.append(I)
    
    
player2[1] = I2[0]
player2[6] = I2[1]
player2[11] = I2[2]
player2[16] = I2[3]
player2[21] = I2[4]

N2 = []
for i in range(1,6):
    N =random.randint(31 , 45)
    while (N in N2):
        N =random.randint(31 , 45)
    while not (N in N2):
        N2.append(N)
    
    
player2[2] = N2[0]
player2[7] = N2[1]
player2[12] = N2[2]
player2[17] = N2[3]
player2[22] = N2[4]

G2 = []
for i in range(1 , 6):
    G = random.randint(46 , 60)
    while (G in G2):
        G =random.randint(46 , 60)
    while not (G in G2):
        G2.append(G)
    
    
player2[3] = G2[0]
player2[8] = G2[1]
player2[13] = G2[2]
player2[18] = G2[3]
player2[23] = G2[4]


O2 = []
for i in range(1,6):
    O = random.randint(61 , 75)
    while (O in O2):
        O =random.randint(61 , 75)
    while not (O in O2):
        O2.append(O)
    
        
player2[4] = O2[0]
player2[9] = O2[1]
player2[14] = O2[2]
player2[19] = O2[3]
player2[24] = O2[4]

a = []
b = []
c = []
d = []
e = [] 
f = []
g = []
h = []
i = []
j = []
k = []
l = []
list1 = []
a.extend((player1[0] , player1[1] , player1[2] , player1[3] , player1[4]))
a.sort()
list1.append(a)

b.extend((player1[5] , player1[6] , player1[7] , player1[8] , player1[9]))
b.sort()
list1.append(b)

c.extend((player1[10] , player1[11] , player1[12] , player1[13] , player1[14]))
c.sort()
list1.append(c)

d.extend((player1[15] , player1[16] , player1[17] , player1[18] , player1[19]))
d.sort()
list1.append(d)

e.extend((player1[20] , player1[21] , player1[22] , player1[23] , player1[24]))
e.sort()
list1.append(e)

f.extend((player1[0] , player1[5] , player1[10] , player1[15] , player1[20]))
f.sort()
list1.append(f)

g.extend((player1[1] , player1[6] , player1[11] , player1[16] , player1[21]))
g.sort()
list1.append(g)

h.extend((player1[2] , player1[7] , player1[12] , player1[17] , player1[22]))
h.sort()
list1.append(h)

i.extend((player1[3] , player1[8] , player1[13] , player1[18] , player1[23]))
i.sort()
list1.append(i)

j.extend((player1[4] , player1[9] , player1[14] , player1[19] , player1[24]))
j.sort()
list1.append(j)

k.extend((player1[0] , player1[6] , player1[12] , player1[18] , player1[24]))
k.sort()
list1.append(k)

l.extend((player1[4] , player1[8] , player1[12] , player1[16] , player1[20]))
l.sort()
list1.append(l)

m = []
n = []
o = []
p = []
q = [] 
r = []
s = []
t = []
u = []
v = []
w = []
x = []
list2 = []
m.extend((player2[0] , player2[1] , player2[2] , player2[3] , player2[4]))
m.sort()
list2.append(m)

n.extend((player2[5] , player2[6] , player2[7] , player2[8] , player2[9]))
n.sort()
list2.append(n)

o.extend((player2[10] , player2[11] , player2[12] , player2[13] , player2[14]))
o.sort()
list2.append(o)

p.extend((player2[15] , player2[16] , player2[17] , player2[18] , player2[19]))
p.sort()
list2.append(p)

q.extend((player2[20] , player2[21] , player2[22] , player2[23] , player2[24]))
q.sort()
list2.append(q)

r.extend((player2[0] , player2[5] , player2[10] , player2[15] , player2[20]))
r.sort()
list2.append(r)

s.extend((player2[1] , player2[6] , player2[11] , player2[16] , player2[21]))
s.sort()
list2.append(s)

t.extend((player2[2] , player2[7] , player2[12] , player2[17] , player2[22]))
t.sort()
list2.append(t)

u.extend((player2[3] , player2[8] , player2[13] , player2[18] , player2[23]))
u.sort()
list2.append(u)

v.extend((player2[4] , player2[9] , player2[14] , player2[19] , player2[24]))
v.sort()
list2.append(v)

w.extend((player2[0] , player2[6] , player2[12] , player2[18] , player2[24]))
w.sort()
list2.append(w)

x.extend((player2[4] , player2[8] , player2[12] , player2[16] , player2[20]))
x.sort()
list2.append(x)

a1 = []
b1 = []
c1 = []
d1 = []
e1 = []
f1 = []
g1 = []
h1 = []
i1 = []
j1 = []
k1 = []
l1 = []

def sort1():
    a1.sort()
    b1.sort()
    c1.sort()
    d1.sort()
    e1.sort()
    f1.sort()
    g1.sort()
    h1.sort()
    i1.sort()
    j1.sort()
    k1.sort()
    l1.sort()

def is_Player1_Winner():
    sort1()
    if intplayer1 == player1[0]:
        a1.append(intplayer1)
        k1.append(intplayer1)
        f1.append(intplayer1)
        sort1()
    if intplayer1 == player1[1]:
        b1.append(intplayer1)
        f1.append(intplayer1)
        sort1()
    if intplayer1 == player1[2]:
        f1.append(intplayer1)
        c1.append(intplayer1)
        sort1()
    if intplayer1 == player1[3]:
        f1.append(intplayer1)
        d1.append(intplayer1)
        sort1()
    if intplayer1 == player1[4]:
        f1.append(intplayer1)
        l1.append(intplayer1)
        e1.append(intplayer1)
        sort1()
    if intplayer1 == player1[5]:
        a1.append(intplayer1)
        g1.append(intplayer1)
        sort1()
    if intplayer1 == player1[6]:
        k1.append(intplayer1)
        b1.append(intplayer1)
        g1.append(intplayer1)
        sort1()
    if intplayer1 == player1[7]:
        c1.append(intplayer1)
        g1.append(intplayer1)
        sort1()
    if intplayer1 == player1[8]:
        l1.append(intplayer1)
        d1.append(intplayer1)
        g1.append(intplayer1)
        sort1()
    if intplayer1 == player1[9]:
        e1.append(intplayer1)
        g1.append(intplayer1)
        sort1()
    if intplayer1 == player1[10]:
        h1.append(intplayer1)
        a1.append(intplayer1)
        sort1()
    if intplayer1 == player1[11]:
        h1.append(intplayer1)
        b1.append(intplayer1)
        sort1()
    if intplayer1 == player1[12]:
        h1.append(intplayer1)
        c1.append(intplayer1)
        l1.append(intplayer1)
        k1.append(intplayer1)
        sort1()
    if intplayer1 == player1[13]:
        h1.append(intplayer1)
        d1.append(intplayer1)
        sort1()
    if intplayer1 == player1[14]:
        h1.append(intplayer1)
        e1.append(intplayer1)
        sort1()
    if intplayer1 == player1[15]:
        i1.append(intplayer1)
        a1.append(intplayer1)
        sort1()
    if intplayer1 == player1[16]:
        i1.append(intplayer1)
        b1.append(intplayer1)
        l1.append(intplayer1)
        sort1()
    if intplayer1 == player1[17]:
        i1.append(intplayer1)
        c1.append(intplayer1)
        sort1()
    if intplayer1 == player1[18]:
        k1.append(intplayer1)
        i1.append(intplayer1)
        d1.append(intplayer1)
        sort1()
    if intplayer1 == player1[19]:
        i1.append(intplayer1)
        e1.append(intplayer1)
        sort1()
    if intplayer1 == player1[20]:
        l1.append(intplayer1)
        j1.append(intplayer1)
        a1.append(intplayer1)
        sort1()
    if intplayer1 == player1[21]:
        j1.append(intplayer1)
        b1.append(intplayer1)
        sort1()
    if intplayer1 == player1[22]:
        j1.append(intplayer1)
        c1.append(intplayer1)
        sort1()
    if intplayer1 == player1[23]:
        j1.append(intplayer1)
        d1.append(intplayer1)
        sort1()
    if intplayer1 == player1[24]:
        j1.append(intplayer1)
        k1.append(intplayer1)
        e1.append(intplayer1)
        sort1()
        
def exep1():
    sort1()
    if intplayer2 in player1:
        
        if intplayer2 == player1[0]:
            a1.append(intplayer2)
            k1.append(intplayer2)
            f1.append(intplayer2)
            sort1()
        if intplayer2 == player1[1]:
            b1.append(intplayer2)
            f1.append(intplayer2)
            sort1()
        if intplayer2 == player1[2]:
            f1.append(intplayer2)
            c1.append(intplayer2)
            sort1()
        if intplayer2 == player1[3]:
            f1.append(intplayer2)
            d1.append(intplayer2)
            sort1()
        if intplayer2 == player1[4]:
            f1.append(intplayer2)
            l1.append(intplayer2)
            e1.append(intplayer2)
            sort1()
        if intplayer2 == player1[5]:
            a1.append(intplayer2)
            g1.append(intplayer2)
            sort1()
        if intplayer2 == player1[6]:
            k1.append(intplayer2)
            b1.append(intplayer2)
            g1.append(intplayer2)
            sort1()
        if intplayer2 == player1[7]:
            c1.append(intplayer2)
            g1.append(intplayer2)
            sort1()
        if intplayer2 == player1[8]:
            l1.append(intplayer2)
            d1.append(intplayer2)
            g1.append(intplayer2)
            sort1()
        if intplayer2 == player1[9]:
            e1.append(intplayer2)
            g1.append(intplayer2)
            sort1()
        if intplayer2 == player1[10]:
            h1.append(intplayer2)
            a1.append(intplayer2)
            sort1()
        if intplayer2 == player1[11]:
            h1.append(intplayer2)
            b1.append(intplayer2)
            sort1()
        if intplayer2 == player1[12]:
            h1.append(intplayer2)
            c1.append(intplayer2)
            l1.append(intplayer2)
            k1.append(intplayer2)
            sort1()
        if intplayer2 == player1[13]:
            h1.append(intplayer2)
            d1.append(intplayer2)
            sort1()
        if intplayer2 == player1[14]:
            h1.append(intplayer2)
            e1.append(intplayer2)
            sort1()
        if intplayer2 == player1[15]:
            i1.append(intplayer2)
            a1.append(intplayer2)
            sort1()
        if intplayer2 == player1[16]:
            i1.append(intplayer2)
            b1.append(intplayer2)
            l1.append(intplayer2)
            sort1()
        if intplayer2 == player1[17]:
            i1.append(intplayer2)
            c1.append(intplayer2)
            sort1()
        if intplayer2 == player1[18]:
            k1.append(intplayer2)
            i1.append(intplayer2)
            d1.append(intplayer2)
            sort1()
        if intplayer2 == player1[19]:
            i1.append(intplayer2)
            e1.append(intplayer2)
            sort1()
        if intplayer2 == player1[20]:
            l1.append(intplayer2)
            j1.append(intplayer2)
            a1.append(intplayer2)
            sort1()
        if intplayer2 == player1[21]:
            j1.append(intplayer2)
            b1.append(intplayer2)
            sort1()
        if intplayer2 == player1[22]:
            j1.append(intplayer2)
            c1.append(intplayer2)
            sort1()
        if intplayer2 == player1[23]:
            j1.append(intplayer2)
            d1.append(intplayer2)
            sort1()
        if intplayer2 == player1[24]:
            j1.append(intplayer2)
            k1.append(intplayer2)
            e1.append(intplayer2)
            sort1()
         
        

m2 = []
n2 = []
o2 = []
p2 = []
q2 = []
r2 = []
s2 = []
t2 = []
u2 = []
v2 = []
w2 = []
x2 = []

def sort2():
    m2.sort()
    n2.sort()
    o2.sort()
    p2.sort()
    q2.sort()
    r2.sort()
    s2.sort()
    t2.sort()
    u2.sort()
    v2.sort()
    w2.sort()
    x2.sort()

def is_Player2_Winner():
    sort2()
    if intplayer2 == player2[0]:
        w2.append(intplayer2)
        r2.append(intplayer2)
        m2.append(intplayer2)
        sort2()
    if intplayer2 == player2[1]:
        m2.append(intplayer2)
        s2.append(intplayer2)
        sort2()
    if intplayer2 == player2[2]:
        m2.append(intplayer2)
        t2.append(intplayer2)
        sort2()
    if intplayer2 == player2[3]:
        m2.append(intplayer2)
        u2.append(intplayer2)
        sort2()
    if intplayer2 == player2[4]:
        x2.append(intplayer2)
        m2.append(intplayer2)
        v2.append(intplayer2)
        sort2()
    if intplayer2 == player2[5]:
        r2.append(intplayer2)
        n2.append(intplayer2)
        sort2()
    if intplayer2 == player2[6]:
        w2.append(intplayer2)
        n2.append(intplayer2)
        s2.append(intplayer2)
        sort2()
    if intplayer2 == player2[7]:
        n2.append(intplayer2)
        t2.append(intplayer2)
        sort2()
    if intplayer2 == player2[8]:
        x2.append(intplayer2)
        n2.append(intplayer2)
        u2.append(intplayer2)
        sort2()
    if intplayer2 == player2[9]:
        n2.append(intplayer2)
        v2.append(intplayer2)
        sort2()
    if intplayer2 == player2[10]:
        r2.append(intplayer2)
        o2.append(intplayer2)
        sort2()
    if intplayer2 == player2[11]:
        o2.append(intplayer2)
        s2.append(intplayer2)
        sort2()
    if intplayer2 == player2[12]:
        x2.append(intplayer2)
        w2.append(intplayer2)
        o2.append(intplayer2)
        t2.append(intplayer2)
        sort2()
    if intplayer2 == player2[13]:
        o2.append(intplayer2)
        u2.append(intplayer2)
        sort2()
    if intplayer2 == player2[14]:
        o2.append(intplayer2)
        v2.append(intplayer2)
        sort2()
    if intplayer2 == player2[15]:
        p2.append(intplayer2)
        r2.append(intplayer2)
        sort2()
    if intplayer2 == player2[16]:
        x2.append(intplayer2)
        p2.append(intplayer2)
        s2.append(intplayer2)
        sort2()
    if intplayer2 == player2[17]:
        p2.append(intplayer2)
        t2.append(intplayer2)
        sort2()
    if intplayer2 == player2[18]:
        w2.append(intplayer2)
        p2.append(intplayer2)
        u2.append(intplayer2)
        sort2()
    if intplayer2 == player2[19]:
        p2.append(intplayer2)
        v2.append(intplayer2)
        sort2()
    if intplayer2 == player2[20]:
        x2.append(intplayer2)
        q2.append(intplayer2)
        r2.append(intplayer2)
        sort2()
    if intplayer2 == player2[21]:
        q2.append(intplayer2)
        s2.append(intplayer2)
        sort2()
    if intplayer2 == player2[22]:
        q2.append(intplayer2)
        t2.append(intplayer2)
        sort2()
    if intplayer2 == player2[23]:
        q2.append(intplayer2)
        u2.append(intplayer2)
        sort2()
    if intplayer2 == player2[24]:
        w2.append(intplayer2)
        q2.append(intplayer2)
        v2.append(intplayer2)
        sort2()
        
def exep2():
    sort2()
    if intplayer1 in player2:
        if intplayer1 == player2[0]:
            w2.append(intplayer1)
            r2.append(intplayer1)
            m2.append(intplayer1)
            sort2()
        if intplayer1 == player2[1]:
            m2.append(intplayer1)
            s2.append(intplayer1)
            sort2()
        if intplayer1 == player2[2]:
            m2.append(intplayer1)
            t2.append(intplayer1)
            sort2()
        if intplayer1 == player2[3]:
            m2.append(intplayer1)
            u2.append(intplayer1)
            sort2()
        if intplayer1 == player2[4]:
            x2.append(intplayer1)
            m2.append(intplayer1)
            v2.append(intplayer1)
            sort2()
        if intplayer1 == player2[5]:
            r2.append(intplayer1)
            n2.append(intplayer1)
            sort2()
        if intplayer1 == player2[6]:
            w2.append(intplayer1)
            n2.append(intplayer1)
            s2.append(intplayer1)
            sort2()
        if intplayer1 == player2[7]:
            n2.append(intplayer1)
            t2.append(intplayer1)
            sort2()
        if intplayer1 == player2[8]:
            x2.append(intplayer1)
            n2.append(intplayer1)
            u2.append(intplayer1)
            sort2()
        if intplayer1 == player2[9]:
            n2.append(intplayer1)
            v2.append(intplayer1)
            sort2()
        if intplayer1 == player2[10]:
            r2.append(intplayer1)
            o2.append(intplayer1)
            sort2()
        if intplayer1 == player2[11]:
            o2.append(intplayer1)
            s2.append(intplayer1)
            sort2()
        if intplayer1 == player2[12]:
            x2.append(intplayer1)
            w2.append(intplayer1)
            o2.append(intplayer1)
            t2.append(intplayer1)
            sort2()
        if intplayer1 == player2[13]:
            o2.append(intplayer1)
            u2.append(intplayer1)
            sort2()
        if intplayer1 == player2[14]:
            o2.append(intplayer1)
            v2.append(intplayer1)
            sort2()
        if intplayer1 == player2[15]:
            p2.append(intplayer1)
            r2.append(intplayer1)
            sort2()
        if intplayer1 == player2[16]:
            x2.append(intplayer1)
            p2.append(intplayer1)
            s2.append(intplayer1)
            sort2()
        if intplayer1 == player2[17]:
            p2.append(intplayer1)
            t2.append(intplayer1)
            sort2()
        if intplayer1 == player2[18]:
            w2.append(intplayer1)
            p2.append(intplayer1)
            u2.append(intplayer1)
            sort2()
        if intplayer1 == player2[19]:
            p2.append(intplayer1)
            v2.append(intplayer1)
            sort2()
        if intplayer1 == player2[20]:
            x2.append(intplayer1)
            q2.append(intplayer1)
            r2.append(intplayer1)
            sort2()
        if intplayer1 == player2[21]:
            q2.append(intplayer1)
            s2.append(intplayer1)
            sort2()
        if intplayer1 == player2[22]:
            q2.append(intplayer1)
            t2.append(intplayer1)
            sort2()
        if intplayer1 == player2[23]:
            q2.append(intplayer1)
            u2.append(intplayer1)
            sort2()
        if intplayer1 == player2[24]:
            w2.append(intplayer1)
            q2.append(intplayer1)
            v2.append(intplayer1)
            sort2()
           
print('Welcom to bingo game ,,  have fun !') 
print('\n')       
      

print('       player1                    ' + '\n'
      + '----------------------' + '\n'
      + str(player1[0]) + ' | ' + str(player1[1]) + ' | ' + str(player1[2]) + ' | ' + str(player1[3]) + ' | ' + str(player1[4]) + '\n'
      '----------------------' + '\n' 
      + str(player1[5]) +   ' | ' + str(player1[6]) +   ' | ' + str(player1[7]) +  ' | '  + str(player1[8]) +    ' | '+ str(player1[9]) + '\n'
      + '----------------------' + '\n' 
      + str(player1[10]) +    ' | '  + str(player1[11]) +    ' | ' + str(player1[12]) +    ' | ' + str(player1[13]) +    ' | ' + str(player1[14]) + '\n' 
      + '----------------------' + '\n' 
      + str(player1[15]) +   ' | ' + str(player1[16]) +   ' | '  + str(player1[17]) +    ' | '  + str(player1[18]) +    ' | ' + str(player1[19]) + '\n'
      + '----------------------' + '\n' 
      + str(player1[20]) +   ' | ' + str(player1[21]) +    ' | ' + str(player1[22]) +   ' | ' + str(player1[23]) +    ' | ' + str(player1[24]) + '\n'
      + '----------------------' + '\n')







print('       player2                    ' + '\n'
      + '----------------------' + '\n'
      + str(player2[0]) + ' | ' + str(player2[1]) + ' | ' + str(player2[2]) + ' | ' + str(player2[3]) + ' | ' + str(player2[4]) + '\n'
      '----------------------' + '\n' 
      + str(player2[5]) +   ' | ' + str(player2[6]) +   ' | ' + str(player2[7]) +  ' | '  + str(player2[8]) +    ' | '+ str(player2[9]) + '\n'
      + '----------------------' + '\n' 
      + str(player2[10]) +    ' | '  + str(player2[11]) +    ' | ' + str(player2[12]) +    ' | ' + str(player2[13]) +    ' | ' + str(player2[14]) + '\n' 
      + '----------------------' + '\n' 
      + str(player2[15]) +   ' | ' + str(player2[16]) +   ' | '  + str(player2[17]) +    ' | '  + str(player2[18]) +    ' | ' + str(player2[19]) + '\n'
      + '----------------------' + '\n' 
      + str(player2[20]) +   ' | ' + str(player2[21]) +    ' | ' + str(player2[22]) +   ' | ' + str(player2[23]) +    ' | ' + str(player2[24]) + '\n'
      + '----------------------' + '\n')





gameIsPlaying = True

while gameIsPlaying:
    
    
    
    intplayer1 = int(input('Enter number from player1 list :  '))
    
    
    is_Player1_Winner()
    exep2()
    
    if len(a1) == 5 or len(b1) == 5 or len(c1) == 5 or len(d1) == 5 or len(e1) == 5 or len(f1) == 5 or len(g1) == 5 or len(h1) == 5 or len(i1) == 5 or len(j1) == 5 or len(k1) == 5 or len(l1) == 5 :
        if (a1 in list1) or (b1 in list1) or (c1 in list1) or (d1 in list1) or (e1 in list1) or (f1 in list1) or (g1 in list1) or (h1 in list1) or (i1 in list1) or (j1 in list1) or (k1 in list1) or (l1 in list1):
            print('BINGO')
            break       
    
    
    
    intplayer2 = int(input('Enter number from player2 list :  '))
    
    
    is_Player2_Winner()
    exep1()
    if len(m2) == 5 or len(n2) == 5 or len(o2) == 5  or len(p2) == 5 or len(r2) == 5 or len(s2) == 5 or len(t2) == 5 or len(u2) == 5 or len(v2) == 5 or len(w2) == 5 or len(x2) == 5 or len(q2) == 5 :
        if (m2 in list2) or (n2 in list2) or (o2 in list2) or (p2 in list2) or (r2 in list2) or (s2 in list2) or (t2 in list2) or (u2 in list2) or (v2 in list2) or (w2 in list2) or (x2 in list2) or (q2 in list2):
            print('BINGO')
            break 
    
    
    