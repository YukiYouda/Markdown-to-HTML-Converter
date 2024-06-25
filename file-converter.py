import markdown
import sys

input_contents = ''

if len(sys.argv) == 4:
    if sys.argv[1] == 'markdown':
        input_path_name = sys.argv[2]
        output_path_name = sys.argv[3]
        with open(input_path_name) as f:
            input_contents = f.read()
            html_string = markdown.markdown(input_contents)
        with open(output_path_name, 'w') as f:
            f.write(html_string)
    else:
        print('コマンド名が間違っています')
else:
    print('引数が間違っています')
