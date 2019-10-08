#program to check if input string endswith ly, ed, ing or ers
needle = raw_input('Enter a string: ')
#if needle.endswith('ly') or needle.endswith('ed') or needle.endswith('ing') or needle.endswith('ers'):
#    print('Is valid')
#else:
#    print('Invalid')
if needle in ('ly', 'ed', 'ing', 'ers'):#improper code
    print('Is valid')
else:
    print ('invalid')
if 'ers' in needle:#doesnot mean endswith
    print('Is valid')
else:
   print('Invalid')
if any([needle.endswith(e) for e in ('ly', 'ed', 'ing', 'ers')]):
    print('Is valid')
else:
    print('Invalid')