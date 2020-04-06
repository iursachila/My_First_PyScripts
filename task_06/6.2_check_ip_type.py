# -*- coding: utf-8 -*-
ip = input('Insert Ip address: ')
while True:
        try:
            octet0 = int(ip.split('.')[0])
            octet1 = int(ip.split('.')[1])
            octet2 = int(ip.split('.')[2])
            octet3 = int(ip.split('.')[3])
        except (ValueError, IndexError):
            print('Incorect format')
            ip = input('Insert Ip address again: ')
            continue
        else:
            ip1 = ip1 = (octet0>255) or (octet1>255) or (octet2>255) or (octet3>255) or (octet0<0) or (octet1<0) or (octet2<0) or (octet3<0)
            if ip1 is True:
                print('Invalid IP octet(s) range:')
                ip = input('Insert Ip address again: ')
                continue
            else:
                if octet0 in range(1,224):
                    print('\nThis IP: {} address is unicast'.format(ip))
                elif octet0 in range(224,239):
                    print('\nThis IP: {} address is multicast'.format(ip))
                elif ip == '255.255.255.255':
                    print('\nThis IP: {} address is local broadcast'.format(ip))
                elif ip =='0.0.0.0':
                    print('\nThis IP: {} address is unassigned'.format(ip))
                else:
                    print('\nThis IP: {} address is unused'.format(ip))
                break
                                                                            
    
                                                                              
   

