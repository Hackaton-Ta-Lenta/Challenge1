class Candidate():
    pass

def read_string(lines, current_line, data, counter, init=''):
    result = init
    while counter < len(data) and (not result.endswith('"') or result.strip() == '"'):
        result += ',' + data[counter]
        result = result.replace('""', '')
        counter += 1
    result = result.replace('""', '')
    while not result.endswith('"') or result.strip() == '"' or result.endswith('""'):
        current_line += 1
        data = lines[current_line].strip().split(',')
        counter = 0
        for _ in range(len(data)):
            result += ' ' + data[counter]
            result = result.replace('""', '')
            counter += 1
            if result.endswith('"'): 
                break
    return (result, current_line, data, counter)

if __name__ == '__main__':
    file_path = 'Data/Candidates.csv'
    candidates = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        current_line = 0
        while current_line < len(lines):
            data = lines[current_line].strip().split(',')
            candidate = Candidate()
            candidate.id = data[0]
            candidate.email = data[1]
            candidate.name = data[2]
            candidate.last_name = data[3]
            while data[3].startswith('"') and not candidate.last_name.endswith('"'):
                candidate.last_name += data[4]
                del data[4]
            candidate.phone = data[4]
            candidate.date = data[5]
            candidate.gender = data[6]
            candidate.dni_type = data[7]
            candidate.dni = data[8]
            candidate.country = data[9]
            candidate.city = data[10]
            candidate.education = data[11]
            while data[11].startswith('"') and not candidate.education.endswith('"'):
                candidate.education += data[12]
                del data[12]
            candidate.salary = data[12]

            try:
                description = data[13]
                counter = 14
            except:
                current_line += 1
                data = lines[current_line].strip().split(',')
                counter = 1
                description = data[0]
            if data[counter - 1] != '' and data[counter - 1].startswith('"'):
                res, current_line, data, counter = read_string(lines, current_line, data, counter, description)
                description = res
            candidate.description = description
            # print(current_line)
            # print(candidate.name)
            # print(candidate.description)
            candidate.not_experience = data[counter]
            candidate.not_studies = data[counter+1]
            candidate.proffesion = data[counter+2]
            candidate.movility = data[counter+3]
            candidate.civil_status = data[counter+4]
            candidate.video = data[counter+5]
            data = lines[current_line].strip().split(']')
            try:
                candidate.studies = '[' + data[0].split('[')[1] + ']'
                candidate.experience = '[' + data[1].split('[')[1] + ']'
                candidate.psy_test = '[' + data[2].split('[')[1] + ']'
            except:
                pass
            # candidates.append(candidate)
            current_line += 1