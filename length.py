#file: length.py
#author: E Shijia
#Created: 2013.08.02

def learn_rule():
    rules_dict = {}
    input_file = open(r'input.txt')
    while True:
        rule = input_file.readline().strip('\n')
        if rule == '':
            break
        rule_list = rule.split()
        rules_dict[rule_list[1]] = rule_list[3]
    input_file.close()
    rules_dict['miles'] = rules_dict['mile']
    rules_dict['yards'] = rules_dict['yard']
    rules_dict['inches'] = rules_dict['inch']
    rules_dict['feet'] = rules_dict['foot']
    rules_dict['faths'] = rules_dict['fath']
    rules_dict['furlongs'] = rules_dict['furlong']
    return rules_dict

def get_expression():
    expression_list = []
    input_file = open(r'input.txt')
    while True:
        line = input_file.readline().strip('\n')
        if line == '':
            break
    while True:
        exp = input_file.readline().strip('\n')
        if not exp:
            break
        expression_list.append(exp)
    input_file.close()
    return expression_list

def result(expressions, rules):
    result_list = []
    for exp in expressions:
        temp_list = list()
        count = 0
        slice_exp = exp.split()
        for i in range(0, len(slice_exp)):
            if slice_exp[i] == '+':
                continue
            elif slice_exp[i] == '-':
                slice_exp[i+1] = str(0.0 - float(slice_exp[i+1]))
            elif slice_exp[i].isalpha():
                temp_list[count-1] *= float(rules[slice_exp[i]])
            else:
                temp_list.insert(count, float(slice_exp[i]))
                count += 1
        result_list.append(sum(temp_list))
    return result_list

def output(my_result):
    output_file = open(r'output.txt', 'w')
    output_lines = []
    output_lines.append('e.shijia@gmail.com\n')
    output_lines.append('\n')
    for item in my_result:
        output_lines.append(str('%.2f' % item) + ' m' + '\n')
    output_file.writelines(output_lines)
    output_file.close()

if __name__ == "__main__":
    length_rule = learn_rule()
    length_expression = get_expression()
    length_result = result(length_expression, length_rule)
    output(length_result)
    
        