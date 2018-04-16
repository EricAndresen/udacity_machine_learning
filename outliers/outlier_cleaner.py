#!/usr/bin/python

def drop_x_percent(zipped_data, percentile_drop):
    '''
        Takes in list of tuples with ages, networth, error
        drops top x% of errors
    '''
    ages, networth, errors = zip(*zipped_data)
    errors = list(errors)
    percentile = round((len(errors)/100) * percentile_drop, 0)
    zipped_data = list(zipped_data)
    for _ in range(int(percentile)):
        print(max(max(errors), min(errors), key = abs))
        idxmax = errors.index(max(max(errors), min(errors), key = abs))
        del errors[idxmax], zipped_data[idxmax]
    return zipped_data

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    ### your code goes here
    errors = [ worth - prediction for worth, prediction in zip(net_worths, predictions)]

    cleaned_data = list(zip(ages, net_worths, errors))

    return drop_x_percent(cleaned_data, 10)
