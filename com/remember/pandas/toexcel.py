import pandas as pd

if __name__ == '__main__':
    path = "/Users/wangjiahao/Downloads/test1.xlsx"

    data = {
        "name": ["Jason", "Molly", "Tina", "Jake", "Amy"],
        "age": [31, 23, 19, 28, 18],
        "score": [98, 76, 84, 79, 92]
    }

    df = pd.DataFrame(data, columns=["name", "age", "score"])
    df.to_excel(path)
