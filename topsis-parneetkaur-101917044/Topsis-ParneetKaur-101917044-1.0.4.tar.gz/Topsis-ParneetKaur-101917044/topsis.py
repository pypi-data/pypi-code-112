
import pandas as pd
import os
import sys

def main():
    
    # File Not Found error
    if not os.path.isfile(sys.argv[1]):
        print("File does not Exist")
        exit(1)
    
    # File extension not csv
    elif ".csv" != (os.path.splitext(sys.argv[1]))[1]:
        print("File is not of csv type.Please a csv file...")
        exit(1)
    
    # Arguments not equal to 5
    # print("Checking for Errors...\n")
    elif ((len(sys.argv) < 5) or (len(sys.argv) > 5)):
        print("Number of parameters are not sufficient.Please Enter exactly 5 parameters")
        exit(1)

    else:
        dataset = pd.read_csv(sys.argv[1])
        temp_dataset = pd.read_csv(sys.argv[1])
        nCol = len(temp_dataset.columns.values)

        # less then 3 columns in input dataset
        if nCol < 3:
            print("File has less number of columns than required")
            exit(1)

        # Handeling non-numeric value
        for i in range(1, nCol):
            pd.to_numeric(dataset.iloc[:, i], errors='coerce')
            dataset.iloc[:, i].fillna(
                (dataset.iloc[:, i].mean()), inplace=True)

        # Handling errors of weighted and impact arrays
        try:
            weights = [int(i) for i in sys.argv[2].split(',')]
        except:
            print("ERROR : In weights array please check again")
            exit(1)
        impact = sys.argv[3].split(',')
        for i in impact:
            if not (i == '+' or i == '-'):
                print("ERROR : In impact array please check again")
                exit(1)

        # Checking number of column,weights and impacts is same or not
        if nCol != len(weights)+1 or nCol != len(impact)+1:
            print(
                "ERROR : Number of weights, number of impacts and number of columns not same")
            exit(1)

        if (".csv" != (os.path.splitext(sys.argv[4]))[1]):
            print("ERROR : Output file extension is wrong")
            exit(1)
        if os.path.isfile(sys.argv[4]):
            os.remove(sys.argv[4])
        # print(" No error found\n\n Applying Topsis Algorithm...\n")
        Topsis(temp_dataset, dataset, nCol, weights, impact)


def Normalize(temp_dataset, nCol, weights):
    # normalizing the array
    # print(" Normalizing the DataSet...\n")
    for i in range(1, nCol):
        temp = 0
        for j in range(len(temp_dataset)):
            temp = temp + temp_dataset.iloc[j, i]**2
        temp = temp**0.5
        for j in range(len(temp_dataset)):
            temp_dataset.iat[j, i] = (
                temp_dataset.iloc[j, i] / temp)*weights[i-1]
    return temp_dataset


def Values(temp_dataset, nCol, impact):
    # print(" Calculating Positive and Negative values...\n")
    p_val = (temp_dataset.max().values)[1:]
    n_val = (temp_dataset.min().values)[1:]
    for i in range(1, nCol):
        if impact[i-1] == '-':
            p_val[i-1] = n_val[i-1]
            n_val[i-1] = p_val[i-1]
    return p_val, n_val


def Topsis(temp_dataset, dataset, nCol, weights, impact):
    # normalizing the array
    temp_dataset = Normalize(temp_dataset, nCol, weights)

    # Calculating positive and negative values
    p_val, n_val = Values(temp_dataset, nCol, impact)

    # calculating topsis score
    # print(" Generating Score and Rank...\n")
    score = []
    for i in range(len(temp_dataset)):
        temp_p, temp_n = 0, 0
        for j in range(1, nCol):
            temp_p = temp_p + (p_val[j-1] - temp_dataset.iloc[i, j])**2
            temp_n = temp_n + (n_val[j-1] - temp_dataset.iloc[i, j])**2
        temp_p, temp_n = temp_p**0.5, temp_n**0.5
        score.append(temp_n/(temp_p + temp_n))
    dataset['Topsis Score'] = score

    # calculating the rank according to topsis score
    dataset['Rank'] = (dataset['Topsis Score'].rank(
        method='max', ascending=False))
    dataset = dataset.astype({"Rank": int})

    # Writing the csv
    # print(" Writing Result to CSV...\n")
    dataset.to_csv(sys.argv[4], index=False)
    # print(" Successfully Terminated")


if __name__ == "__main__":
    main()
