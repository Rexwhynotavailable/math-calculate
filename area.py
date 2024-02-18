#正方體, 長方體側面積計算
長 = input("長為:")
寬 = input("寬為:")
柱高 = input("柱高:")

長 = float(長)
寬 = float(寬)
柱高 = float(柱高)
lateral_area = 長 * 寬 * 2 + (長 + 寬) * 2 * 柱高
print("側面積計算為:", lateral_area)