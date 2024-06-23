"""conversion.py"""
def get_bcm_ip(ip: str, vlan_id: str) -> str:
    """
    Gets the bcm_port based on local or public IP addresses

    Args:
        ip (str):
        vlan_id (str):

    Returns:
        str:
    """
    if ip.startswith("192.168"):
        ip_base_address = int(ip.split(".")[-1])
        return f"192.168.{vlan_id}.{ip_base_address}"
    return ip

def get_bcm_port(ip: str, port: int) -> int:
    """
    Gets the bcm_port based on local or public IP addresses

    Args:
        ip (str):
        port (int):

    Raises:
        ValueError:

    Returns:
        int:
    """
    if ip.startswith("192.168"):
        return "623"
    if port < 2200 or port > 2299:
        raise ValueError(f"Port number must be between 2200 and 2299: port = {port}")
    host_id = str(port % 100).zfill(2)
    return "623" + host_id

def get_hostname(ip: str, port: int) -> int:
    """
    Gets the hostname based on local or public IP addresses

    Args:
        ip (str):
        port (int):

    Raises:
        ValueError:

    Returns:
        int:
    """
    if ip.startswith("192.168"):
        ip_base_address = int(ip.split(".")[-1])
        if ip_base_address < 10 or ip_base_address > 255:
            raise ValueError(f"IP base address must be between 10 and 255: ip_base_address = {ip_base_address}")
        host_id_int = ip_base_address - 10
        host_id = str(host_id_int).zfill(2)
    else:
        if port < 2200 or port > 2299:
            raise ValueError(f"Port number must be between 2200 and 2299: port = {port}")
        host_id = str(port % 100).zfill(2)
    return "starlyng" + host_id
