print('NGUYEN NGOC CHI MSSV 245752021610164')
import numpy as np
#Tao mot mang co cau truc voi cac cot: Ten, Chieu cao, Lop
dt = np.dtype([('Ten','U50'),('Chieu cao','f4'),('Lop','U20')])
#Du lieu ve sinh vien
data = np.array([('NGUYEN NGOC CHI',1.73,'12A2'),
                 ('Thach Hao',1.80,'12A2')],dtype=dt)
#Sap xep mang theo chieu cao (cot'Chieu cao')
sorted_data = np.sort(data, order='Chieu cao')
#In ra mang da sap xep
print(sorted_data)
