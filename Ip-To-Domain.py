import socket
import dns.resolver
import dns.reversename
import asyncio
import argparse
import os

async def resolve_ip_to_domain(ip):
    try:
        # Perform reverse DNS lookup
        reverse_name = dns.reversename.from_address(ip)
        answers = dns.resolver.resolve(reverse_name, "PTR")
        domains = [str(answer) for answer in answers]
        return ip, domains
    except dns.resolver.NXDOMAIN:
        return ip, ["No domain found"]
    except Exception as e:
        return ip, [f"Error: {str(e)}"]

async def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Resolve IP to domain/subdomain")
    parser.add_argument("-i", "--ip", help="Single IP address to resolve")
    parser.add_argument("-m", "--multi", help="File containing multiple IP addresses")
    args = parser.parse_args()

    ip_list = []

    # Handle single IP input
    if args.ip:
        ip_list.append(args.ip)

    # Handle multiple IPs from file
    if args.multi:
        if not os.path.exists(args.multi):
            print(f"Error: File {args.multi} not found")
            return
        with open(args.multi, "r") as file:
            ip_list.extend([line.strip() for line in file if line.strip()])

    # Check if any IPs are provided
    if not ip_list:
        print("Error: Please provide an IP using -i or a file using -m")
        return

    # Resolve IPs
    results = []
    for ip in ip_list:
        ip, domains = await resolve_ip_to_domain(ip)
        results.append(f"IP: {ip} -> Domains: {', '.join(domains)}")

    # Print results
    for result in results:
        print(result)

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
