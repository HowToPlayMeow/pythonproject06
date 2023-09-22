def SPN() :
    print('[ โปรแกรมตรวจสอบความเป็นเด็ก หนุ่ม แก่ ]')

def ID( ) :
    name = input('ช์่อ : ')
    age = int(input('อายุ : '))
    return name, age

def CSS( name, age ) :
    if age <= 18 :
        print(f'คุณ {name} อายุ {age} ปี เป็นเด็ก')
    elif age >= 19 and age <= 45 :
        print(f'คุณ {name} อายุ {age} ปี เป็นหนุ่ม')
    else :
        print(f'คุณ {name} อายุ {age} ปี เป็นคนแก่')

print('------------------------------------')
SPN()
print('------------------------------------')
name, age = ID()
print('------------------------------------')
CSS( name, age )
print('------------------------------------')