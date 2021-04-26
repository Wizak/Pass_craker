import itertools
import time


def formating_number(number, separator='.'):
    list_chars = list(reversed(str(number))) 
    editing_list = [''.join(list_chars[k:k+3]) for k in range(0, len(list_chars), 3)]
    editing_number = ''.join(reversed(separator.join(editing_list)))
    return editing_number


def print_count_permutation(control_condition_length, control_condition_ascii, mode, print_mode=False):
    m_range = count_control_condition_ascii(control_condition_ascii)
    place = count_permutation(m_range, control_condition_length, mode)
    if print_mode:
        for p in place:
            print(formating_number(p, separator=' '))
    else:
        return list(place)


def factorial(n):
    return 1 if n == 1 else n*factorial(n-1)


def count_permutation(m_range, n_range, mode):
    if mode == 'combination':
        for n in n_range:
            yield int(factorial(m_range)/(factorial(n)*factorial(n-1)))
    elif mode == 'combination-replacement':
        for n in n_range:
            m = m_range+n-1
            yield int(factorial(m)/(factorial(n)*factorial(m_range-n)))
    elif mode == 'permutation':
        for n in n_range:
            yield int(factorial(m_range)/factorial(m_range-n))
    elif mode == 'product':
        for n in n_range:
            yield m_range
    elif mode == 'product-repeat':
        for n in n_range:
            yield m_range**n


def count_control_condition_ascii(control_condition_ascii):
    return sum([abs(b-a)+1 for a, b in control_condition_ascii])


def condition_ascii_to_char(control_condition_ascii):
    ids = [list(range(a, b+1)) for a, b in control_condition_ascii]
    id_to_char = [list(map(chr, l)) for l in ids]
    return id_to_char


def generator_password(control_condition_length, control_condition_ascii, mode):
    prepear_condition = list(sum(condition_ascii_to_char(control_condition_ascii), []))
    for count in control_condition_length:
        if mode == 'permutation':
            for combination in itertools.permutations(prepear_condition, count):
                yield combination
        elif mode == 'combination':
            for combination in itertools.combinations(prepear_condition, count):
                yield combination
        elif mode == 'combination-replacement':
            for combination in itertools.combinations_with_replacement(prepear_condition, count):
                yield combination
        elif mode == 'product':
            for combination in itertools.product(prepear_condition):
                yield combination
        elif mode == 'product-repeat':
            for combination in itertools.product(prepear_condition, repeat=count):
                yield combination


def database_save(control_condition_length, control_condition_ascii, mode, filename='pass'):
    generator = generator_password(control_condition_length, control_condition_ascii, mode)
    with open(f'{filename}.txt', 'w') as f:
        for gen in generator:
            string_gen = ''.join(gen)
            f.write(string_gen+'\n')


def checing_password_conformity(control_condition_length, control_condition_ascii, etalon_password, mode='permutation', show_process=False, delta_time=30, mode_file=None, filename='pass'):
    timer_start = time.time()
    if mode_file is None:
        generator = generator_password(control_condition_length, control_condition_ascii, mode)
        i = 0
        for gen in generator:
            string_gen = ''.join(gen)
            if show_process:
                i += 1
                timer_end = time.time() - timer_start
                if (timer_end // delta_time) >= 1:
                    timer_start = time.time()
                    print(string_gen, i)
            if etalon_password == string_gen:
                return True
    elif mode_file == 'read from db':
        with open(f'{filename}.txt', 'r') as f:
            i = 0
            for line in f:
                string_gen = line.splitlines()[0]
                if show_process:
                    i += 1
                    timer_end = time.time() - timer_start
                    if (timer_end // delta_time) >= 1:
                        timer_start = time.time()
                        print(string_gen)
                if etalon_password == string_gen:
                    return True
