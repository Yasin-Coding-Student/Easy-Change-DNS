import os
import shutil
# ==================================
def clear_Command():
    os.system("cls" if os.name == "nt" else "clear")

def center_text(text):
    """Centers text in terminal width."""
    width = shutil.get_terminal_size().columns
    return text.center(width)

def get_wifi_name():
    try:
        result = os.popen('netsh interface show interface').read()
        for line in result.splitlines():
            if "Wi-Fi" in line:
                return "Wi-Fi"
            elif "Wireless" in line:
                return "Wireless Network Connection"
        return None
    except Exception:
        return None

def main_Menu():
    clear_Command()
    print(center_text("==== 🛜  DNS Control Tools ===="))
    print(center_text("1) Change DNS."))
    print(center_text("2) Show Current DNS."))
    print(center_text("3) Reset DNS to Automatic."))
    print(center_text("4) Exit."))
    print(center_text("========================================"))
    
    choice = input(center_text("Enter your choice: ")).strip()

    if choice == "1":
        dns_Menu()
    elif choice == "2":
        show_Current_Dns()
    elif choice == "3":
        reset_Dns()
    elif choice == "4":
        print(center_text("Exiting... 👋"))
        exit()
    else:
        print(center_text("Invalid Option. Try again."))
        input(center_text("Press Enter..."))
        main_Menu()

def dns_Menu():
    clear_Command()
    print(center_text("==== 🌐 Choose a DNS Provider ===="))
    print(center_text("1) Google : (8.8.8.8 , 8.8.4.4)"))
    print(center_text("2) Cloudflare : (1.1.1.1 , 1.0.0.1)"))
    print(center_text("3) OpenDNS : (208.67.222.222 , 208.67.220.220)"))
    print(center_text("4) AdGuard : (94.140.14.14 , 94.140.15.15)"))
    print(center_text("5) Shecan1 : (178.22.122.100 , 185.51.200.2)"))
    print(center_text("6) Shecan2 : (178.22.122.101 , 185.51.200.1)"))
    print(center_text("7) Electro : (78.157.42.101 , 78.157.42.100)"))
    print(center_text("8) Back to Main Menu <=="))
    print(center_text("========================================"))

    choice = input(center_text("Enter your choice: ")).strip()

    dns_options = {
        "1": ("8.8.8.8", "8.8.4.4"),
        "2": ("1.1.1.1", "1.0.0.1"),
        "3": ("208.67.222.222", "208.67.220.220"),
        "4": ("94.140.14.14", "94.140.15.15"),
        "5": ("178.22.122.100", "185.51.200.2"),
        "6": ("178.22.122.101", "185.51.200.1"),
        "7": ("78.157.42.101", "78.157.42.100")
    }

    if choice in dns_options:
        set_Dns(*dns_options[choice])
    elif choice == "8":
        main_Menu()
    else:
        print(center_text("Invalid Option. Try again."))
        input(center_text("Press Enter..."))
        dns_Menu()

def set_Dns(dns1, dns2):
    clear_Command()
    wifi_name = get_wifi_name()
    if not wifi_name:
        print(center_text("❌ Could not find Wi-Fi interface."))
        input(center_text("Press Enter to return..."))
        main_Menu()
        return

    print(center_text(f"Setting DNS for '{wifi_name}' to {dns1} and {dns2} ..."))
    os.system(f'netsh interface ip set dns name="{wifi_name}" static {dns1}')
    os.system(f'netsh interface ip add dns name="{wifi_name}" {dns2} index=2')
    print(center_text("✅ DNS Changed Successfully !!!"))
    input(center_text("Press Enter to main menu..."))
    main_Menu()

def reset_Dns():
    clear_Command()
    wifi_name = get_wifi_name()
    if not wifi_name:
        print(center_text("❌ Could not find Wi-Fi interface."))
        input(center_text("Press Enter to return..."))
        main_Menu()
        return

    print(center_text(f"Resetting DNS for '{wifi_name}' to automatic..."))
    os.system(f'netsh interface ip set dns name="{wifi_name}" dhcp')
    print(center_text("✅ DNS reset to automatic successfully!"))
    input(center_text("Press Enter to return to main menu..."))
    main_Menu()

def show_Current_Dns():
    clear_Command()
    os.system("netsh interface ip show dns")
    input("\nPress Enter to return to main menu...")
    main_Menu()

# =============================================
if __name__ == "__main__":
    main_Menu()