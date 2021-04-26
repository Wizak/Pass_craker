import pass_cracker as pc 


control_condition_length = range(1, 9)
control_condition_ascii = [(48, 57), (65, 90), (97, 122)]
etalon_password = 'BigBoy20'
mode = 'product-repeat'
mode_file = 'read from db'
filename = 'D:/WTF/pass'

pc.print_count_permutation(control_condition_length, control_condition_ascii, mode, print_mode=True)
pc.database_save(control_condition_length, control_condition_ascii, mode, filename)
# fact = pc.checing_password_conformity(control_condition_length, control_condition_ascii, etalon_password, mode, show_process=True, delta_time=300, mode_file=mode_file, filename=filename)
# print(fact)