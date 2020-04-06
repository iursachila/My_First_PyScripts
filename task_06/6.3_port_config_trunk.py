trunk_template = [
                'switchport trunk encapsulation dot1q', 'switchport mode trunk',
                'switchport trunk allowed vlan'
                ]
trunk = {   
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
                    }
for intf,vl_fun in trunk.items():
    print('\ninterface FastEthernet '+intf)
    for commands in trunk_template:
        if commands.endswith('allowed vlan'):
            if 'add' in vl_fun:
                print('{} add {}\n'.format(commands,'10,20'))
            elif 'only' in vl_fun:
                print('{}  {}\n'.format(commands,'11,30'))
            elif 'del' in vl_fun:
                print('{} remove {}\n'.format(commands,17))
        else:
            print('{}'.format(commands))
            
