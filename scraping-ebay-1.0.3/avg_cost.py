from pandas import read_csv

def get_avg_cost(csv_file):
    df = read_csv(csv_file)
    prices = []
    for price in df['Price']:
        prices.append(price)

    avg = 0
    i = 0
    for price in prices:
        try:
            # print(price)
            avg += float(price[1:].replace(",", ""))
            i += 1
        except (ValueError, TypeError):
            continue
        except Exception as e:
            print(f"encountered unexpected exception {e}")
            print(price)
            continue
    
    avg /= float(i)
    return avg

def main():
    print(f"avg cost of item: {get_avg_cost('output.csv')}")

if __name__ == '__main__':
    main()

