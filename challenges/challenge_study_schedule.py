def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        counter = list()
        for pair in permanence_period:
            if int(target_time) in range(pair[0], pair[-1] + 1):
                counter.append(pair)

        return len(counter)
    except TypeError:
        return None
