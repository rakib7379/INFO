import os
import time
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, phonenumberutil
from colorama import Fore, Style, init
import requests

# Initialize Colorama
init(autoreset=True)

# Developer Info
DEVELOPER_INFO = f"""
{Fore.MAGENTA}╔══════════════════════════════════════════╗
{Fore.MAGENTA}║             {Fore.CYAN}👑 DEVELOPER INFO 👑          {Fore.MAGENTA}║
{Fore.MAGENTA}╠══════════════════════════════════════════╣
{Fore.YELLOW}║ 🎭 Developer : {Fore.CYAN}RAKIB                        {Fore.YELLOW}║
{Fore.RED}║ 📘 FACEBOOK  : {Fore.CYAN}RAKIB                        {Fore.RED}║
{Fore.GREEN}║ 📞 WHATSAPP  : {Fore.CYAN}+8801827590353               {Fore.GREEN}║
{Fore.BLUE}║ 🎵 TIKTOK    : {Fore.CYAN}RAKIB ON FORE                {Fore.BLUE}║
{Fore.MAGENTA}║ 🛠️ TOOLS     : {Fore.CYAN}PERSONAL                     {Fore.MAGENTA}║
{Fore.MAGENTA}╚══════════════════════════════════════════╝
"""

# ASCII Logo
LOGO =f"""{Fore.BLUE }
   _____ _____   __________    ______RAKIB
  / ___//  _/ | / / ____/ /   / ____/
  \__ \ / //  |/ / / __/ /   / __/   
 ___/ // // /|  / /_/ / /___/ /___   
/____/___/_/ |_/\____/_____/_____/RAKIB   
                                            
{Style.RESET_ALL}"""

# Function to track phone number
def track_phone_number():
    os.system("clear")
    print(LOGO)
    print(DEVELOPER_INFO)
    
    number = input(f"{Fore.YELLOW}📞 Enter Phone Number: {Fore.CYAN}")
    if not number.startswith("+"):
        number = "+880" + number.lstrip("0")

    try:
        parsed_number = phonenumbers.parse(number)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        number_type = phonenumberutil.number_type(parsed_number)
        country = geocoder.description_for_number(parsed_number, "en")
        region = geocoder.description_for_number(parsed_number, "en", region=True)
        sim_carrier = carrier.name_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)
        country_code = parsed_number.country_code
        national_number = parsed_number.national_number
        formatted_e164 = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        formatted_international = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_national = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        formatted_rfc3966 = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.RFC3966)

        print(f"""
{Fore.CYAN}╔══════════════════════════════════════════╗
{Fore.CYAN}║          {Fore.YELLOW}📞 Phone Number Information {Fore.CYAN}║               
{Fore.CYAN}╠══════════════════════════════════════════╣
{Fore.RED}║ 🌍 Country     : {Fore.GREEN}{country}               
{Fore.RED}║ 🏙️ Region      : {Fore.MAGENTA}{region}               
{Fore.RED}║ 📡 Carrier     : {Fore.MAGENTA}{sim_carrier if sim_carrier else 'Unknown'}     
{Fore.RED}║ ⏰ Time Zones  : {Fore.BLUE}{time_zones}   
{Fore.RED}║ 🗺️ Google Maps: {Fore.CYAN}https://www.google.com/maps/search/?api=1&query={country}
{Fore.RED}║ ✅ Valid       : {Fore.GREEN}{is_valid}
{Fore.RED}║ 📱 Type        : {Fore.MAGENTA}{phonenumberutil.number_type(parsed_number)}
{Fore.RED}║ 🌐 Country Code: {Fore.BLUE}{country_code}
{Fore.RED}║ 📞 National Num: {Fore.CYAN}{national_number}
{Fore.RED}║ 📝 E164 Format : {Fore.GREEN}{formatted_e164}
{Fore.RED}║ 🌍 Intl Format : {Fore.MAGENTA}{formatted_international}
{Fore.RED}║ 📞 National Fmt: {Fore.BLUE}{formatted_national}
{Fore.RED}║ 🔗 RFC3966 Fmt : {Fore.CYAN}{formatted_rfc3966}
{Fore.CYAN}╚══════════════════════════════════════════╝
""")
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"{Fore.RED}❌ Invalid Phone Number: {e}")
    
    back_to_menu()

# Function to track IP address
def track_ip():
    os.system("clear")
    print(LOGO)
    print(DEVELOPER_INFO)

    ip = input(f"{Fore.YELLOW}🌍 Enter IP Address: {Fore.CYAN}")
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url).json()

    if response["status"] == "fail":
        print(f"{Fore.RED}❌ Invalid IP Address")
        return

    print(f"""
{Fore.CYAN}╔══════════════════════════════════════════╗
{Fore.CYAN}║          {Fore.YELLOW}🌍 IP Address Information {Fore.CYAN}║               
{Fore.CYAN}╠══════════════════════════════════════════╣
{Fore.RED}║ 🏳️ Country     : {Fore.GREEN}{response['country']}                   
{Fore.RED}║ 🏙️ City        : {Fore.MAGENTA}{response['city']}                    
{Fore.RED}║ 📡 ISP         : {Fore.GREEN}{response['isp']}                       
{Fore.RED}║ 🏢 Organization: {Fore.MAGENTA}{response['org']}                       
{Fore.RED}║ 🕒 Timezone    : {Fore.BLUE}{response['timezone']}                       
{Fore.RED}║ 🗺️ Google Maps: {Fore.CYAN}https://www.google.com/maps/search/?api=1&query={response['lat']},{response['lon']}
{Fore.RED}║ 🌐 Continent   : {Fore.GREEN}{response.get('continent', 'N/A')}                       
{Fore.RED}║ 📍 ZIP Code    : {Fore.MAGENTA}{response.get('zip', 'N/A')}                       
{Fore.RED}║ 🏞️ Region Code : {Fore.BLUE}{response.get('region', 'N/A')}                       
{Fore.RED}║ 💰 Currency    : {Fore.CYAN}{response.get('currency', 'N/A')}                       
{Fore.CYAN}╚══════════════════════════════════════════╝
""")
    
    back_to_menu()

# Function to validate phone number
def validate_phone_number(number):
    try:
        parsed_number = phonenumbers.parse(number)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumberutil.NumberParseException:
        return False

# Function to send custom SMS
def send_custom_sms():
    os.system("clear")
    print(LOGO)
    print(DEVELOPER_INFO)

    number = input(f"{Fore.YELLOW}📞 Enter phone number: {Fore.CYAN}")
    if not validate_phone_number(number):
        print(f"{Fore.RED}❌ Invalid phone number!")
        back_to_menu()
        return

    message = input(f"{Fore.YELLOW}📩 Enter message: {Fore.CYAN}")
    interval = int(input(f"{Fore.YELLOW}⏳ Enter time interval (seconds): {Fore.CYAN}"))
    count = int(input(f"{Fore.YELLOW}🔁 Enter how many messages: {Fore.CYAN}"))

    success_count = 0
    failed_count = 0

    for i in range(count):
        try:
            # Send SMS using termux-sms-send (or any other API)
            os.system(f'termux-sms-send -n {number} "{message}"')
            print(f"{Fore.GREEN}✅ Sent {i+1}/{count} messages to {number} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            success_count += 1
        except Exception as e:
            print(f"{Fore.RED}❌ Failed to send message {i+1}/{count}: {e}")
            failed_count += 1
        time.sleep(interval)

    print(f"\n{Fore.CYAN}📊 SMS Sending Report:")
    print(f"{Fore.GREEN}✅ Successfully sent: {success_count}")
    print(f"{Fore.RED}❌ Failed to send: {failed_count}")
    print(f"{Fore.YELLOW}📅 Total messages attempted: {count}")

    back_to_menu()

# Function to return to the main menu
def back_to_menu():
    print(f"\n{Fore.CYAN}🔙 Do you want to go back to the main menu? (y/n)")
    choice = input(f"{Fore.YELLOW}👉 Enter choice: {Fore.CYAN}").strip().lower()
    if choice == "y":
        main_menu()
    else:
        print(f"{Fore.RED}👋 Exiting... Bye!")
        exit()

# Main Menu
def main_menu():
    os.system("clear")
    print(LOGO)
    print(DEVELOPER_INFO)
    
    print(f"""
{Fore.YELLOW}🔍 Select an option:
{Fore.GREEN}1. Track Phone Number
{Fore.BLUE}2. Track IP Address
{Fore.MAGENTA}3. Send Custom SMS
{Fore.RED}4. Exit
""")
    
    choice = input(f"{Fore.CYAN}👉 Enter your choice (1/2/3/4): ")

    if choice == "1":
        track_phone_number()
    elif choice == "2":
        track_ip()
    elif choice == "3":
        send_custom_sms()
    elif choice == "4":
        print(f"{Fore.RED}👋 Exiting... Bye!")
        exit()
    else:
        print(f"{Fore.RED}❌ Invalid choice!")
        back_to_menu()

# Run Main Menu
main_menu()