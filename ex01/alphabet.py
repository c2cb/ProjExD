import random

#③：改行整理をした


#コメントを受けて修正したもの1

#説明を付けました。マークとして、①：を付けました。

#ここまで1


#③：改行整理をした。


#コメントを受けて修正したもの2

# a = ["A", "B", "C", "D", "E", "F", "G", 
# "H", "I", "J", "K", "L", "M", "N", 
# "O", "P", "Q", 
# "R", "S", "T", 
# "U", "V", "W", "X", "Y", "Z"]

#①：アルファベットを入れるリスト
a = []
#①：文字コードで大文字のアルファベットを入れるfor文
for i in range(65, 91):
    a.append(chr(i))
#①：リストaの確認
print(a)

#ここまで2


#③：改行整理をした


#コメントを受けて修正したもの3

#改行を整理した部分に、③とマークを付けました。

#ここまで3


#③：改行整理をした


#①：対象文字のprint
print("対象文字：")


#③：改行整理をした


# b = random.randrange(0,25)
# print(b)
# print(a[b]+"\r\n")


#③：改行整理をした


#①：ランダムでリストaのアルファベットを10個選び、入れる
li1 = []
li1 = random.sample(a, 10)


#③：改行整理をした


#①：リストli1から、さらに二つ選んだものをリストli2として入れる
# print(li1)
print("")

li2 = []
li2 = random.sample(li1, 2)


#③：改行整理をした


# print(li1)
# print(li2)


#③：改行整理をした


#①：li1を丁寧な形で出力する
for i in range(0, 9):
    print(li1[i] + " ", end="")

    # if (a[c] in li1) :
    #     i -= 1
    #     continue

    # li1.append(a[c])
    # print(li1[i])


#③：改行整理をした


#①：改行と、欠陥文字のprint
print("\r\n")
print("欠陥文字：")


#③：改行整理をした


#①：li2を丁寧な形で出力する
for i in range(0, 2):
    print(li2[i] + " ", end="")


#③：改行整理をした


#①：li1から、li2の内容を消去する（失敗）
li1.remove(li2)
print(li1)


#③：改行整理をした

