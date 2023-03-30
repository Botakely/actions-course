import os

def print_hello_world():
  print('Hello world!')
  print(os.environ.get('TOKEN_SECRET'))
  
if __name__ == '__main__':
  print_hello_world()
