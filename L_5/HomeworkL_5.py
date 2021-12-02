while True:
    try:
        user_input = input('Please enter ID code: ')

        if len(user_input) != 11:
            raise UserWarning
    except user_input([6], [10]):
        continue
    except UserWarning:
        if len(user_input) > 11:
            print('ID code is too long')
        elif len(user_input) < 11:
            print('ID code is too short')
        continue
    else:
        break
print(user_input)
condition = True
while condition:
    user_choice = input('Please chooce:\n1.Get data from ID\n2.Validate\n0.Exit')
    if user_choice == '1':

        gender_num = user_input[7:10]
        by_num = user_input[4:6]
        bm_num = user_input[2:4]
        bd_num  = user_input[0:2]
        b_century = user_input[6]
        check_num = user_input[10]
        p_of_b = user_input[7:10]
        # Get gender of ID owner
        if int(gender_num) % 2 == 0:
            gender_id = 'Female'
        else:
            gender_id = 'Male'
         # Get year of birth first characters
        if b_century == '+':
            b_c = '1800-1899'
        elif b_century == '-':
            b_c = '1900-1999'
        elif b_century == 'A':
            b_c = '2000-2099'
        # PLace of birth or residents
        if int(p_of_b) in range(2, 900):
            type_of = 'Finish or permanent residence'
        else:
            p_of_b = 'Temporary ID'

        print(f'ID : {user_input}')
        print(f'Gender: {gender_id}')
        print(f'Date of birth: {bd_num}.{bm_num}.{by_num}')
        print(f'Birth century: {b_c}')
        print(f'Type of residents: {type_of}')
        print(f'Check num: {check_num}')
