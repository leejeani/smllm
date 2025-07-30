import pickle

if __name__ == '__main__':
    my_dict = {'name': 'harry', 'age': 21, 'friends': ['Ron', 'Hermione']}

    # 파일로 저장
    with open('data/my_dict.pkl', 'wb') as f:
        pickle.dump(my_dict, f)

    # 파일 불러오기
    with open('data/my_dict.pkl', 'rb') as f:
        loaded_dict = pickle.load(f)

    print(loaded_dict)

    pickle.dump(my_dict, open('data/my_dict2.pkl', 'wb'))
    result = pickle.load(open('data/my_dict2.pkl', 'rb'))
    print(result)



