import os

print("path " + os.path.abspath('.'))

os.getcwd()

os.chdir('./')

os.getcwd()

def sanitize(time_string):
    if ("-" in time_string):
        splitter = '-'
        (mins, seconds) = time_string.split(splitter)
        return mins + "." + seconds
    elif (':' in time_string):
        splitter = ":"
        (mins, seconds) = time_string.split(splitter)
        return mins + "." + seconds
    else:
        return time_string


def get_coach_data(filename):
    if os.path.exists(filename):
        data = open(filename)
        for line in data:
            james = line.strip().split(",")
            print(filename,'       ', james)
        cleaned_james = []
        for each in james:
            cleaned_james.append(sanitize(each))
        print('clean',filename, cleaned_james)

        '''列表推导 list comprehension '''
        quick_clean_james = [sanitize(each_t) for each_t in james]
        print('quick_clean',filename, quick_clean_james)

        sorted_james = sorted(cleaned_james)[0:2]
        print('sorted',filename, sorted_james)

        set_james = set(sorted_james)
        print('set_james', filename, set_james)

        data.close()

    else:
        print('no file exist')

    return sorted_james


print('james.txt', get_coach_data('james.txt'))




