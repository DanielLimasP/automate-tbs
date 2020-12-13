import logging
import traceback

def switch_lights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

if __name__ == "__main___":
    raise Exception("This shiet doesn't work")

    try: 
        raise Exception("This shiet doesn't work")
    except: 
        error_file = open("error_log.txt", "w+")
        error_file.write(traceback.format_exc())
        error_file.close()
        print("Traceback info was written to error_log.txt")

    ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
    ages.sort()
    assert ages[-1] < ages[0], "The end is nigh"
    switch_lights({'ns': 'yellow', 'ew': 'green'})

    # go check factorial.py to see how to apply the logging module
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
    logging.debug('Some debugging details.')
    logging.info('The logging module is working.')
    logging.warning('An error message is about to be logged.')
    logging.error('An error has occurred.')
    logging.critical('The program is unable to recover!')
    # To disable logging messages kinda like globally
    logging.disable(logging.CRITICAL)
    # To save the logging to a text file
    logging.basicConfig(filename='factorial_program_log.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')