import os

file = open('assets/user_data.py', 'w')
username = os.environ.get('DAZN_USER_DACH_USR')
password = os.environ.get('DAZN_USER_DACH_PSW')
file.write(f"""
USER_CREDENTIALS = [
    {
        'EMAIL': '{username}',
        'PASSWORD': '{password}'
    },
]
""")
file.close()
