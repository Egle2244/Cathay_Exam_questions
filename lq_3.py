"""這支程式邏輯題目3"""

def find_last_person(n):
    people = list(range(1, n + 1))
    index = 0
    count = 0
    while len(people) > 1:
        count += 1
        if count == 3:
            # 報到3的人出圈
            people.pop(index)
            count = 0
        else:
            index += 1

        if index >= len(people):
            index = 0
            
    return people[0]

if __name__ == "__main__":
    try:
        n = int(input("請輸入人數（0～100）: "))
        if 0 < n <= 100:
            result = find_last_person(n)
            print(f"最後留下來的同事是原本的第 {result} 位")
        else:
            print("請輸入1~100之間整數")
    except ValueError:
        print("請輸入有效整數")