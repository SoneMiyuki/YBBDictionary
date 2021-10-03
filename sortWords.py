import codecs


def main():
    lis = codecs.open('words.txt','r',encoding='utf-8').readlines()

    lis.sort()

    codecs.open('words_new.txt','w',encoding='utf-8').writelines(lis)


main()
