import os
from subprocess import check_output

if __name__ == '__main__':
    dir_content = os.listdir('./')
    for n in range(1, 100):
        filename = 'problem-{}.py'.format(n)
        if filename in dir_content:
            cmd = ['python', filename]
            try:
                result = check_output(cmd)
            except OSError:
                continue
            formatted_result = result.replace('\n', '\n\t')
            print '{}\t{}'.format(n, formatted_result)
