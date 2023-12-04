'''
    1) Download this dataset and compute some
        statistics to compare the performance of the two users. [DONE]

    2) Did one of the users type faster? [DONE]

    3) Was one user more efficient in the sense that they had to click fewer times to make a selection?

    4) Explain your reasoning; your explanation should include some graphs of the data.
'''

import pandas as pd
import matplotlib.pyplot as mp

'''
    @description: this function filters out the data in a data set based on certain criteria

    @params: Data -> This is a pd.read_csv file that contains the raw data of a user
    @returns: modified data -> This is the data set with the filtered out data gone
'''
def typingSpeedParser(data):
    # Deciding the start phrase based on the selection number and the click number
    phrase0 = data[(data['Selection Num'] == 1) & (data['Click Num'] == 1)]

    # Deciding the end phrase based on the ending chars of the Typed text and the Click num column == 3
    phrase1 = data[(data['Typed Text'].str.endswith("..")) & (data['Click Num'] == 3)]

    # This is the rows coming together
    return_data = pd.concat([phrase0, phrase1]).sort_index()
    return return_data

'''
    @description: This takes in preprocessed data and calculates the typing speed and graphs it

    @params: Data -> modified pd.read_csv file containing the users data
    @returns: N/A
'''
def calc_and_print_typeSpeed(data):
    # edge case (The number of rows in the data is not an even number) :
    if len(data) % 2 != 0:
        # change the function to properly fit by removing the last row
        data = data[:-1]

    # vars for helping calc and plot
    speed_list = []
    phrase_list = []

    # take the row data, two at a time
    for i in range(0, len(data), 2):
        row0 = data.iloc[i]
        row1 = data.iloc[i + 1]

        # calculating the total time by taking row1 absolute time - row0 absolute time
        total_time = row1['Click Time Absolute (s)'] - row0['Click Time Absolute (s)']

        # Calculating the len of word to standardize data
        phrase_length = len(row1['Typed Text'])
        if total_time > 0:
            speed = phrase_length / total_time
        else:
            # case where they did not have typing speed
            speed = 0

        speed_list.append(speed)
        phrase_list.append(row0['Phrase Num'])

    # Calculating the average speed
    avg_TS = sum(speed_list)/len(speed_list)

    # Starting the plot
    mp.figure(figsize=(10, 5))
    mp.plot(phrase_list, speed_list, marker='*')
    mp.title('User typing speed')
    mp.xlabel('Phrase Number')
    mp.ylabel('Typing speed (char/sec)')
    mp.grid(True)
    mp.show()

    return avg_TS


def main():

    user1 = pd.read_csv('../urop_ad_sample_data/user_1_click_data.csv')
    user2 = pd.read_csv('../urop_ad_sample_data/user_2_click_data.csv')

    # Running typing speed tests
    print("User 1 typing speed:", calc_and_print_typeSpeed(typingSpeedParser(user1)), "(char/sec)")
    print("User 2 typing speed:", calc_and_print_typeSpeed(typingSpeedParser(user2)), "(char/sec)")


if __name__ == "__main__":
    main()


