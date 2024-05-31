# import psutil
#
# def format_size(bytes):
#     # Функция для форматирования байт в более читаемые единицы
#     for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']:
#         if bytes < 1024:
#             return f"{bytes:.2f} {unit}"
#         bytes /= 1024
#     return f"{bytes:.2f} PB"
#
# # Информация о загрузке процессора
# cpu_usage_percent = psutil.cpu_percent(interval=1)
#
# # Информация об использовании оперативной памяти
# memory = psutil.virtual_memory()
# memory_usage_percent = memory.percent
#
# # Информация о заполненности дисков
# disk = psutil.disk_usage('/')
# disk_usage_percent = disk.percent
#
# # Информация о сетевой активности
# network = psutil.net_io_counters()
# download_speed = network.bytes_recv
# upload_speed = network.bytes_sent
#
# # Вывод информации
# print(f"CPU Usage: {cpu_usage_percent}%")
# print(f"Memory Usage: {memory_usage_percent}% of {format_size(memory.total)}")
# print(f"Disk Usage: {disk_usage_percent}% of {format_size(disk.total)}")
# print(f"Network Speed - Download: {format_size(download_speed)}/s, Upload: {format_size(upload_speed)}/s")
#
# # import netifaces
# # import socket
# #
# #
# # def get_device_name():
# #     return socket.gethostname()
# #
# #
# # def scan_network():
# #     device_name = get_device_name()
# #     print(f"Scanning network from device: {device_name}\n")
# #
# #     interfaces = netifaces.interfaces()
# #
# #     for iface in interfaces:
# #         addrs = netifaces.ifaddresses(iface)
# #         print(f"Interface: {iface}")
# #
# #         if netifaces.AF_LINK in addrs:
# #             mac = addrs[netifaces.AF_LINK][0]['addr']
# #             print(f"MAC Address: {mac}")
# #
# #         if netifaces.AF_INET in addrs:
# #             ipv4 = addrs[netifaces.AF_INET][0]['addr']
# #             netmask = addrs[netifaces.AF_INET][0]['netmask']
# #             print(f"IPv4 Address: {ipv4}")
# #             print(f"Netmask: {netmask}")
# #
# #         print("=" * 30)
# #
# #
# # if __name__ == "__main__":
# #     scan_network()
#
# import scapy as scapy
# import socket
#
#
# def scan_network(ip_range):
#     arp_request = scapy.ARP(pdst=ip_range)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast / arp_request
#     answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
#     return answered_list
#
#
# def get_host_name(ip):
#     try:
#         return socket.gethostbyaddr(ip)[0]
#     except socket.herror:
#         return "Unknown"
#
#
# def save_to_file(clients_list, file_name="network_scan_results.txt"):
#     with open(file_name, "w") as file:
#         file.write("IP Address\tHost Name\n")
#         file.write("-----------------------------------------\n")
#         for client in clients_list:
#             file.write(f"{client['ip']}\t{client['host']}\n")
#
#
# def perform_scan_and_save(ip_range):
#     clients_list = []
#     answered = scan_network(ip_range)
#     for answer in answered:
#         ip_address = answer[1].psrc
#         host_name = get_host_name(ip_address)
#         clients_list.append({"ip": ip_address, "host": host_name})
#
#     save_to_file(clients_list)
#
#
# # Specify the IP range you want to scan
# ip_range = "192.168.1.1/24"
# perform_scan_and_save(ip_range)
# print("Network scan complete and saved to file.")

