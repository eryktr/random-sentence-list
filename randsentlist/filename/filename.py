import datetime


def unique_filename():
    date = datetime.datetime.now().strftime("%d_%h_%Y_%H_%M_%S")
    return date + ".tex"
