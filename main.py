# import calc

# print(calc.plus(5,10))
# print(calc.multiple(5,2))

# ======================================
# penggunaan alias

# import calc as c, hello as h
# import hello

# print(c.plus(5,10))
# print(h.hello("pratama"))

# =====================================
# memanggil fungsi spesifik, dan juga bisa di aliaskan

# from package.calc import plus as pl, minus as min 
# from package.hello import hello as he

# from calc import plus as pl, minus as min
# from hello import hello as he

# print(pl(10,2))
# print(min(10,2))
# print(he("pratama"))

# instalasi menggunakan pip, untuk package eksternal atau di internet

import pandas as pd


data = {
    'col1': [1,2,3,4,5],
    'col2': [5,4,3,2,1]
}

df = pd.DataFrame(data)

print(df['col1'].min(), df['col1'].max())
