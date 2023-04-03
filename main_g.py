from tokenize import Number
import PySimpleGUI as sg
import  os
import conectilu as conectilu



working_directory = os.getcwd()


import graph as graph

sg.theme('DarkAmber')   # Add a touch of color




layout = [  
            [sg.Text('IP Master'), sg.InputText(key='_IP_MASTER_' , enable_events=True)],

            [sg.Button('Ok'), sg.Button('Cancel')], 
     
]

window = sg.Window('FlexGraph', layout)
text_ip_master = window['_IP_MASTER_']


db_color_nowifi     = 'rgba(000,000,255,1)'  
db_color_excellent  = 'rgba(000,255,000,1)'
db_color_good       = 'rgba(255,255,000,1)'
db_color_fair       = 'rgba(255,155,000,1)'
db_color_poor       = 'rgba(255,099,000,1)'
db_color_vpoor      = 'rgba(255,000,000,1)'

db_color_nowifi_b     = 'rgba(000,000,255,0.1)'  
db_color_excellent_b  = 'rgba(000,255,000,0.1)'
db_color_good_b       = 'rgba(255,255,000,0.1)'
db_color_fair_b       = 'rgba(255,155,000,0.1)'
db_color_poor_b       = 'rgba(255,099,000,0.1)'
db_color_vpoor_b      = 'rgba(255,000,000,0.1)'


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'Ok': # if user closes window or clicks cancel   

        ip_master = values["_IP_MASTER_"]
        print('ip_master ', ip_master)

        mac_id_i = []
        mac_id_i.append(["", 0, 0])
        devices = []
        labels = []
        labels.append("")
        devices_type = []
        devices_type.append("")
        labels_show = []
        labels_show.append("")
        id_slave = []
        id_slave.append(0)
        rssi_slave = []
        db_color = []
        db_color_b = []
        type_line = []


        sock = conectilu.conection(ip_master)

        comando_info_rede = ("SRF,16,6")
        _comando_ascii = "".join(comando_info_rede)
        pacote = bytearray(_comando_ascii.encode())
        str_info = conectilu.send_command_teste(pacote, sock)

        mac_master = ""
        name_master = ""
        if(str_info[0] == 1):
                info_master = str_info[1].split(",")
                mac_master = info_master[8]  
                name_master = info_master[10]  

        print(str_info)
        print(mac_master)
        print(name_master)

        

        comando_to_join = ("SRF,10,255")
        _comando_ascii = "".join(comando_to_join)
        pacote = bytearray(_comando_ascii.encode())
        str_info = conectilu.send_command_teste(pacote, sock)

        #criar um array das resposta
        if(str_info[0] == 1):
            arr_info = str_info[1].split("\r")
            arr_bi_info = []
            for i in range(len(arr_info)):
                if(len(arr_info[i]) > 20):
                    arr_bi_info.append(arr_info[i].split(","))

        k = 0
        for i in range(len(arr_bi_info)):
            k = i + 1
            mac_id_i.append([arr_bi_info[i][3], arr_bi_info[i][2], k])
            labels.append(arr_bi_info[i][12])
            labels_show.append("Tipo : " + arr_bi_info[i][6] + "<br>Nome : " + arr_bi_info[i][12] + "<br>MAC : " + arr_bi_info[i][3]+ "<br>ID Slave : " + arr_bi_info[i][2])
            devices_type.append(arr_bi_info[i][6])
            id_slave.append(arr_bi_info[i][2])
            rssi_slave.append(int(arr_bi_info[i][4]))


        mac_id_i[0][0] = mac_master
        labels[0] = name_master
        devices_type[0] = 'IC-315'
        labels_show[0] = "Tipo : " + devices_type[0] + "<br>Nome : " + name_master + "<br>MAC : " + mac_master + "<br>ID Slave : 0" +  "<br>IP : " + ip_master
        master_info = '<br>' + name_master + '(' + ip_master + ') <br>'



        devices_tupla_mac = []
        add_fake_device = False

        for i in range(len(arr_bi_info)):
            if(arr_bi_info[i][5] != '0'):
                devices_tupla_mac.append((arr_bi_info[i][3], arr_bi_info[i][5]))
            else:               
                devices_tupla_mac.append((arr_bi_info[i][3], 'ff:ff:ff:ff:ff:ff'))
                add_fake_device = True

        if(add_fake_device):
            devices_tupla_mac.append(('ff:ff:ff:ff:ff:ff', mac_master))
            mac_id_i.append(['ff:ff:ff:ff:ff:ff', 256, k + 1])
            labels.append("Fake")
            labels_show.append("Fake")
            devices_type.append("Fake")
            id_slave.append(256)
            rssi_slave.append(-200)

        for i in range(len(rssi_slave)):
            if ( rssi_slave[i] > -60 ):
                db_color.append(db_color_excellent)
                db_color_b.append(db_color_excellent_b)
            elif ( rssi_slave[i] > -76 ):
                db_color.append(db_color_good)
                db_color_b.append(db_color_good_b)
            elif ( rssi_slave[i] > -91 ):
                db_color.append(db_color_fair)
                db_color_b.append(db_color_fair_b)
            elif ( rssi_slave[i] > -100 ):
                db_color.append(db_color_poor)
                db_color_b.append(db_color_poor_b)
            elif ( rssi_slave[i] > -110 ):
                db_color.append(db_color_vpoor)
                db_color_b.append(db_color_vpoor_b)
            else:
                db_color.append(db_color_nowifi)
                db_color_b.append(db_color_nowifi_b)

        for i in range(len(devices_type)):
            
            if ( (devices_type[i] == 'IW-233') or (devices_type[i] == 'IW-122') ):
                type_line.append("dot")
            elif ( (devices_type[i] == 'IC-516') or (devices_type[i] == 'IC-518')  ):
                type_line.append("solid")
            elif (devices_type[i] == 'IC-315'):
                print("Pulou")
            else:
                type_line.append("dash")





        devices_array = []

        for i in range(len(devices_tupla_mac)):
            for j in range(len(mac_id_i)):
                if(devices_tupla_mac[i][0] == mac_id_i[j][0]):
                    devices_array.append([mac_id_i[j][2], 0])



        for i in range(len(devices_tupla_mac)):
            for j in range(len(mac_id_i)):
                if(devices_tupla_mac[i][1] == mac_id_i[j][0]):
                    devices_array[i][1] = mac_id_i[j][2]

        
        for i in range(len(devices_array)):
            devices.append((devices_array[i][0], devices_array[i][1]))
                    

        print("mac_id_i")
        print(mac_id_i)
        print("arr_bi_info")
        print(arr_bi_info)
        print("devices_tupla_mac")
        print(devices_tupla_mac)
        print("devices")
        print(devices)
        print("devices_array")
        print(devices_array)
        print("labels")
        print(labels)
        print("devices_type")
        print(devices_type)
        print("labels_show")
        print(labels_show)
        print("rssi_slave")
        print(rssi_slave)
        print("db_color")
        print(db_color)
        print("db_color_b")
        print(db_color_b)
        print("type_line")
        print(type_line)
        print("id_slave")
        print(id_slave)





        



#devices =[(1, 0),(2, 1),(3, 0),(4, 3),(5, 1),(6, 0),(9, 0),(20,6),(7,0),(8,9),(10,3),(11,0),(12,7),(13,11),(14,6),(15,9),(16,6),(17,7),(18,11),(19,7)]
#labels = ["Master", "802","803","804","805","806","807","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","21"]
#labels_show = ["IC-315<br>806C<br>4444", "IW-233<br>806A","IW-122<br>806A","3","4","5","6","7","8","9","10","11","12","13","14","14","15","16","17","18","19","20","21"]
#id_slave = ["0", "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","21"]
#rssi_slave = [0, -70,-10,-45,-90,-36,-48,-56,-70,-12,-15,-11,-32,-85,-41,-68,-25,-38,-43,-33,-22,-85,-85]
#devices_type = ["IC-315", "IW-233","IW-122","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","21"]
#db_color = [db_color_good, db_color_excellent,db_color_good,db_color_fair,db_color_good,db_color_good,db_color_excellent,db_color_poor,db_color_fair,db_color_good,db_color_excellent,db_color_good,db_color_excellent,db_color_good,db_color_excellent,db_color_vpoor ,db_color_poor,db_color_poor,db_color_vpoor ,db_color_good,db_color_fair,db_color_good,db_color_good]
#db_color_b = [db_color_good_b, db_color_excellent_b,db_color_good_b,db_color_fair_b,db_color_good_b,db_color_good_b,db_color_excellent_b,db_color_poor_b,db_color_fair_b,db_color_good_b,db_color_excellent_b,db_color_good_b,db_color_excellent_b,db_color_good_b,db_color_excellent_b,db_color_vpoor_b ,db_color_poor_b,db_color_poor_b,db_color_poor_b,db_color_vpoor_b ,db_color_good_b,db_color_fair_b,db_color_good_b]
#type_line = ["solid", "solid","dash","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot"]

        print("Len arr_bi_info", len(arr_bi_info)) 
        print("Len devices", len(devices)) 
        print("Len labels", len(labels))
        print("Len labels_show", len(labels_show)) 
        print("Len id_slave", len(id_slave)) 
        print("Len rssi_slave", len(rssi_slave)) 
        print("Len devices_type", len(devices_type)) 
        print("Len db_color", len(db_color)) 
        print("Len db_color_b", len(db_color_b)) 
        print("Len type_line", len(type_line)) 

        graph.draw(devices, labels, labels_show, id_slave, rssi_slave, devices_type, db_color, db_color_b, type_line, master_info)