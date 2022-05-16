print("단위변환기 구현")
while(True):
  print("=================메뉴출력==================")
  first_choice=input("1. 면적변환기능, 2. 길이변환기능, 종료를 원한다면 ('Q' 또는 'q'를 입력합세요 : ")
  if first_choice == 'q' or first_choice == 'Q':
    break
  elif first_choice == '1':
    print("\n=================면적변환기능==================")
    eara = int(input('1. 평 ---> m^2,  2. m^2 ---> 평 : '))
    if(eara ==1):
      qyung = float(input("평수를 입력하세요: "))
      print(f"{qyung}평을 m^2으로 변환한 결과 :{qyung*3.3:.3f}m^2\n")
    else:
      meter_square = float(input("m^2을 입력하세요: "))
      print(f"{meter_square:.1f}m^2을 평으로 변환한 결과 :{meter_square/3.3:.3f}평\n")
  elif first_choice == '2':
    print("\n=================길이변환기능==================")
    height = int(input('1. cm ---> inch,  2. inch ---> cm : '))
    if(height ==1):
      cm = float(input("cm를 입력하세요: "))                  
      print(f"{cm}cm을 inch로 변환한 결과 :{cm*2.54:.2f}inch\n")
    else:
      inch = float(input("inch을 입력하세요: "))
      print(f"{inch:.2f}inch을 평으로 변환한 결과 :{inch/2.54:.2f}cm\n")

print("종료되었습니다.\n\n\n")


print("================인접한 리스트 내부의 합================")
lst =[4, 28, 43, 21, 8, 26, 23, 48, 29, 22, 
1, 27, 27, 25, 14, 1, 38, 46, 31, 28, 
42, 35, 44, 26, 37, 17, 8, 1, 39, 48, 
2, 19, 14, 41, 31, 40, 11, 30, 48, 23, 
0, 10, 25, 47, 32, 19, 40, 8, 19, 45]

while(True):
  k = int(input("인접한 숫자의 개수 k개를 입력하세요: "))
  result =[]

  if (k==0 or k==1 or k>len(lst)):
    print("잘못된 수를 입력했습니다.")
    break
  else:
    for i in range(0,len(lst)-k+1):
      sum = 0 
      for j in range(0,k):
        sum = sum+lst[i+j]
      result.append(sum)
  print(len(result))
  print(result)
  print(max(result))
  