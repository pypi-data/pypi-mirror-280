#
# NFL 1.0.0
# made by DDavid701
#

def format_number(format, number):
    if type(number) == str or type(number) == int:
        try:
            number = int(number)
        except Exception as e: print(f"E: Couldn't format number! ({str(number)})")
        finally:
            if format == 'simplified':
                if len(str(number)) == 4:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}k'
                    return number_formatted
                elif len(str(number)) == 5:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}k'
                    return number_formatted
                elif len(str(number)) == 6:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}k'
                    return number_formatted
                elif len(str(number)) == 7:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}m'
                    return number_formatted
                elif len(str(number)) == 8:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}m'
                    return number_formatted
                elif len(str(number)) == 9:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}m'
                    return number_formatted
                elif len(str(number)) == 10:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}b'
                    return number_formatted
                elif len(str(number)) == 11:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}b'
                    return number_formatted
                elif len(str(number)) == 12:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}b'
                    return number_formatted
                elif len(str(number)) == 13:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}t'
                    return number_formatted
                elif len(str(number)) == 14:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}t'
                    return number_formatted
                elif len(str(number)) == 15:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}t'
                    return number_formatted
                else:
                    return number
            if format == 'simplified_2':
                if len(str(number)) == 4:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}k'
                    return number_formatted
                elif len(str(number)) == 5:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}k'
                    return number_formatted
                elif len(str(number)) == 6:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}k'
                    return number_formatted
                elif len(str(number)) == 7:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}m'
                    return number_formatted
                elif len(str(number)) == 8:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}m'
                    return number_formatted
                elif len(str(number)) == 9:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}m'
                    return number_formatted
                elif len(str(number)) == 10:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}b'
                    return number_formatted
                elif len(str(number)) == 11:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}b'
                    return number_formatted
                elif len(str(number)) == 12:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}b'
                    return number_formatted
                elif len(str(number)) == 13:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}t'
                    return number_formatted
                elif len(str(number)) == 14:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}t'
                    return number_formatted
                elif len(str(number)) == 15:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}t'
                    return number_formatted
                else:
                    return number
            if format == 'simplified_3':
                if len(str(number)) == 4:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}{number_parts[3]}k'
                    return number_formatted
                elif len(str(number)) == 5:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}{number_parts[4]}k'
                    return number_formatted
                elif len(str(number)) == 6:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}{number_parts[5]}k'
                    return number_formatted
                elif len(str(number)) == 7:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}{number_parts[3]}m'
                    return number_formatted
                elif len(str(number)) == 8:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}{number_parts[4]}m'
                    return number_formatted
                elif len(str(number)) == 9:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}{number_parts[5]}m'
                    return number_formatted
                elif len(str(number)) == 10:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}{number_parts[3]}b'
                    return number_formatted
                elif len(str(number)) == 11:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}{number_parts[4]}b'
                    return number_formatted
                elif len(str(number)) == 12:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}{number_parts[5]}b'
                    return number_formatted
                elif len(str(number)) == 13:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}{number_parts[3]}t'
                    return number_formatted
                elif len(str(number)) == 14:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}{number_parts[4]}t'
                    return number_formatted
                elif len(str(number)) == 15:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}{number_parts[5]}t'
                    return number_formatted
                else:
                    return number
            elif format == 'normal':
                if len(str(number)) == 4:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}{number_parts[3]}'
                    return number_formatted
                elif len(str(number)) == 5:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}{number_parts[4]}'
                    return number_formatted
                elif len(str(number)) == 6:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}{number_parts[5]}'
                    return number_formatted
                elif len(str(number)) == 7:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}{number_parts[3]}.{number_parts[4]}{number_parts[5]}{number_parts[6]}'
                    return number_formatted
                elif len(str(number)) == 8:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}{number_parts[4]}.{number_parts[5]}{number_parts[6]}{number_parts[7]}'
                    return number_formatted
                elif len(str(number)) == 9:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}{number_parts[5]}.{number_parts[6]}{number_parts[7]}{number_parts[8]}'
                    return number_formatted
                elif len(str(number)) == 10:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}{number_parts[3]}.{number_parts[4]}{number_parts[5]}{number_parts[6]}.{number_parts[7]}{number_parts[8]}{number_parts[9]}'
                    return number_formatted
                elif len(str(number)) == 11:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}{number_parts[4]}.{number_parts[5]}{number_parts[6]}{number_parts[7]}.{number_parts[8]}{number_parts[9]}{number_parts[10]}'
                    return number_formatted
                elif len(str(number)) == 12:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}{number_parts[5]}.{number_parts[6]}{number_parts[7]}{number_parts[8]}.{number_parts[9]}{number_parts[10]}{number_parts[11]}'
                    return number_formatted
                elif len(str(number)) == 13:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}.{number_parts[1]}{number_parts[2]}{number_parts[3]}.{number_parts[4]}{number_parts[5]}{number_parts[6]}.{number_parts[7]}{number_parts[8]}{number_parts[9]}.{number_parts[10]}{number_parts[11]}{number_parts[12]}'
                    return number_formatted
                elif len(str(number)) == 14:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}{number_parts[3]}{number_parts[4]}.{number_parts[5]}{number_parts[6]}{number_parts[7]}.{number_parts[8]}{number_parts[9]}{number_parts[10]}.{number_parts[11]}{number_parts[12]}{number_parts[13]}'
                    return number_formatted
                elif len(str(number)) == 15:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}{number_parts[4]}{number_parts[5]}.{number_parts[6]}{number_parts[7]}{number_parts[8]}.{number_parts[9]}{number_parts[10]}{number_parts[11]}.{number_parts[12]}{number_parts[13]}{number_parts[14]}'
                    return number_formatted
                else:
                    return number
            elif format == 'space':
                if len(str(number)) == 4:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]} {number_parts[1]}{number_parts[2]}{number_parts[3]}'
                    return number_formatted
                elif len(str(number)) == 5:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]} {number_parts[2]}{number_parts[3]}{number_parts[4]}'
                    return number_formatted
                elif len(str(number)) == 6:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]} {number_parts[3]}{number_parts[4]}{number_parts[5]}'
                    return number_formatted
                elif len(str(number)) == 7:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]} {number_parts[1]}{number_parts[2]}{number_parts[3]} {number_parts[4]}{number_parts[5]}{number_parts[6]}'
                    return number_formatted
                elif len(str(number)) == 8:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]} {number_parts[2]}{number_parts[3]}{number_parts[4]} {number_parts[5]}{number_parts[6]}{number_parts[7]}'
                    return number_formatted
                elif len(str(number)) == 9:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]} {number_parts[3]}{number_parts[4]}{number_parts[5]} {number_parts[6]}{number_parts[7]}{number_parts[8]}'
                    return number_formatted
                elif len(str(number)) == 10:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]} {number_parts[1]}{number_parts[2]}{number_parts[3]} {number_parts[4]}{number_parts[5]}{number_parts[6]} {number_parts[7]}{number_parts[8]}{number_parts[9]}'
                    return number_formatted
                elif len(str(number)) == 11:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]} {number_parts[2]}{number_parts[3]}{number_parts[4]} {number_parts[5]}{number_parts[6]}{number_parts[7]} {number_parts[8]}{number_parts[9]}{number_parts[10]}'
                    return number_formatted
                elif len(str(number)) == 12:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]} {number_parts[3]}{number_parts[4]}{number_parts[5]} {number_parts[6]}{number_parts[7]}{number_parts[8]} {number_parts[9]}{number_parts[10]}{number_parts[11]}'
                    return number_formatted
                elif len(str(number)) == 13:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]} {number_parts[1]}{number_parts[2]}{number_parts[3]} {number_parts[4]}{number_parts[5]}{number_parts[6]} {number_parts[7]}{number_parts[8]}{number_parts[9]} {number_parts[10]}{number_parts[11]}{number_parts[12]}'
                    return number_formatted
                elif len(str(number)) == 14:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]} {number_parts[2]}{number_parts[3]}{number_parts[4]} {number_parts[5]}{number_parts[6]}{number_parts[7]} {number_parts[8]}{number_parts[9]}{number_parts[10]} {number_parts[11]}{number_parts[12]}{number_parts[13]}'
                    return number_formatted
                elif len(str(number)) == 15:
                    number_parts = str(number).strip()
                    number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]} {number_parts[3]}{number_parts[4]}{number_parts[5]} {number_parts[6]}{number_parts[7]}{number_parts[8]} {number_parts[9]}{number_parts[10]}{number_parts[11]} {number_parts[12]}{number_parts[13]}{number_parts[14]}'
                    return number_formatted
                else:
                    return number
            else:
                print('no this don exis .)!')
    else:
        print(f"E: Number can't be a type of '{type(number)}'")