import os
import os.path
import subprocess
import sys

stack = os.environ.get('OLDPWDS', '')
if len(stack):
  stack = stack.split(':')
else:
  stack = []


do = sys.argv[1]

if len(stack):
  if do == 'head':
    last  = stack.pop()
    print last.replace('\:', ':')
    sys.exit()
  elif do == 'tail':
    stack.pop()

if do == 'cd':
  if len(sys.argv) > 1:
    path = sys.argv[2]
  else:
    path = '~'

  if path == '~' or os.path.exists(path):
    cwd = os.environ.get('PWD')
    stack.append(cwd.replace(':','\:'))

print ':'.join(stack)