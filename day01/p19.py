import pickle

if __name__ == '__main__':
    # 파일 불러오기
    f = None
    try:
        f = open('data/my_dict.pkl', 'rb')
        loaded_dict = pickle.load(f)
        print(loaded_dict)
    except FileNotFoundError:
        print("File Not Found")
    finally:
        if f != None:
            print("File Closed")
            f.close()
