print("Masukan nilai koordinat")
x = int(input("Nilai x: "))
y = int(input("Nilai y: "))

if x>0 and y>0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran I" )
elif x<0 and y>0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran II" )    
elif x<0 and y<0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran III" )
elif x>0 and y<0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran IV" )
else:
    pass