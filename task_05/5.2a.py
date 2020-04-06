a= input('Insert IP/Mask: ')
ip,mask = a.split('/')[0],a.split('/')[1]
ip_bin = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(int(ip.split('.')[0]),int(ip.split('.')[1]),int(ip.split('.')[2]),int(ip.split('.')[3]))

network_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
mask1 = str('1')*int(mask) + (str('0')*(32-int(mask)))

mask_template = '''
Mask:
/{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{2:08b} {2:08b} {3:08b} {4:08b}
'''
print(network_template.format(int(ip_bin[0:8],2) & int(mask1[0:8],2), int(ip_bin[8:16],2) & int(mask1[8:16],2),int(ip_bin[16:24],2) & int(mask1[16:24],2),int(ip_bin[24:32],2) & int(mask1[24:32],2)))
print(mask_template.format(mask,int(int(mask1[0:8],2)),int(int(mask1[8:16],2)),int(int(mask1[16:24],2)),int(int(mask1[24:32],2))))

