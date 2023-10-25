import re

def is_valid_resident_number(resident_number):
    pattern = r'^\d{6}-[12]\d{6}$'
    return bool(re.search(pattern, resident_number))

# 테스트 케이스
resident_numbers = [
    '990101-1234567',
    '010203-2345678',
    '000101-3456789',
    '071231-4567890',
    '890101-5678901',
    '220304-6789012',
    '120708-7890123',
    '030912-8901234',
    '101112-9012345',
    '020304-1123456'  # 뒤의 첫 자리가 1로 시작하도록 수정했습니다.
]

for number in resident_numbers:
    print(f'{number} 은(는) {"올바른" if is_valid_resident_number(number) else "올바르지 않은"} 주민등록번호예요')
