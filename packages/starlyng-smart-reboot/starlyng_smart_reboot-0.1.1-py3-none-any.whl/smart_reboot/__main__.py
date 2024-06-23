"""main.py"""
from smart_reboot.utils.configuration import load_configuration
from smart_reboot.utils.execute import execute_get_offline_hostnames, execute_smart_reboot_for_offline_hostnames
from smart_reboot.utils.file import get_last_reboot

def main():
    """
    Runs the metric collectors for each listed server
    """
    # Load configuration
    bcm_servers, vast_api_key, smart_reboot_dir  = load_configuration()

    # Prevent reboot if recently rebooted
    if get_last_reboot(smart_reboot_dir, 5):
        return

    # Execute ssh commands on servers
    offline_hostnames = execute_get_offline_hostnames(bcm_servers, vast_api_key)
    if offline_hostnames:
        execute_smart_reboot_for_offline_hostnames(offline_hostnames, smart_reboot_dir)

if __name__ == "__main__":
    main()
