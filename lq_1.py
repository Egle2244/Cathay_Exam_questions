"""這支程式邏輯題目1"""

def reverse_scores(fixed_scores):
    # 建立固定的對照表
    original = [53, 64, 75, 19, 92]
    fixed =    [35, 46, 57, 91, 29]
    fix_map = {f: o for f, o in zip(fixed, original)}
    
    return [fix_map[s] for s in fixed_scores]

if __name__ == "__main__":
    # 輸入：[35, 46, 57, 91, 29]
    user_input = input("輸入：")

    try:
        fixed_scores = eval(user_input)
        if isinstance(fixed_scores, list):
            original_scores = reverse_scores(fixed_scores)
            print("輸出：", original_scores)
        else:
            print("請輸入正確格式")
    except Exception as e:
        print("發生錯誤沒有：", e)
