import os
os.system('pip install -r requirements.txt')
file='Jeem Boom Bhaa.py'
file2='Jeem Boom Bhaa.pyw'
# get path of the file
path = f'{os.getcwd()}/{file}'

# shell:startup
# get path of the startup folder
startup = f'{os.getenv("APPDATA")}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'

file_content = f'''import os
os.system(r'"{path}"')
'''

# write the file
with open(f'{startup}\\{file2}', 'w') as f:
    f.write(file_content)
