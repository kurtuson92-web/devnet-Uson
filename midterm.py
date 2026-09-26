

devices = []


def add_device(device_list):
    device_list = {
        "name": "Router1",
        "ip": "192.168.1.1",
        "status": "Active"
    }

    name = str(input("Device name"))
    device_list.append(name)

    ip = int(input("Add IP address"))
    device_list.append(ip)

    status = str(input("Enter status"))
    device_list.append(status)

    pass

def view_devices(device_list):{
    print(device_list)
}

def display_menu():
    print("=== Network Device Inventory ===")
    print("1. Add a device")
    print("2. View all devices")
    print("3. Count active vs inactive devices")
    print("find a device by name")
    print("5. Exit")
    pass



while True:
    display_menu()
    cho = int(input("Choose an option: "))

    if cho == 1:{
        add_device()
    }

    elif cho ==2:{
        view_devices()
    }

    elif cho ==3:{
        print("choice 3")
    }
    elif cho ==4:{
        print("choice 4")
    }
    elif cho ==5:
        break
    else:{
        print("enter a valid choice")
        }
    break