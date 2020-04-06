mode = input('Interface mode (access/trunk): ')
interface = input('Insert type and number of interface : ')
vlan = input('Insert vlan(s) number : ')

access_template = [
'switchport mode access', 'switchport access vlan {}',
'switchport nonegotiate', 'spanning-tree portfast',
'spanning-tree bpduguard enable'
]

trunk_template = [
'switchport trunk encapsulation dot1q', 'switchport mode trunk',
'switchport trunk allowed vlan {}'
]
access_template[1] = str(access_template[1].format(vlan))
trunk_template[2] = str(trunk_template[2].format(vlan))
a = {'access' : f'''{access_template[0]}
{access_template[1]}
{access_template[2]}
{access_template[3]}
{access_template[4]}''' , 'trunk' : f'''{trunk_template[0]}
{trunk_template[1]}
{trunk_template[2]}
'''
        }
print('\n')
print('interface {}'.format(interface))
print(a[mode])

