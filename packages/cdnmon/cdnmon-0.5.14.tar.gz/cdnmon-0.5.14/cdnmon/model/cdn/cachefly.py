from cdnmon.model.cdn import CIDR
from cdnmon.model.cdn import CNAMEPattern
from cdnmon.model.cdn import CommonCDN
from cdnmon.util.cidr import deduplicate_networks


class CacheFlyCIDR(CIDR):
    ipv4_urls: str = [
        "https://cachefly.execve.workers.dev/ips/cdn.txt",
    ]

    def extract(self):
        """
        [1] https://help.cachefly.com/hc/en-us/articles/215068666-Reverse-Proxy-Source-IPs
        [2] https://cachefly.cachefly.net/ips/rproxy.txt
        [3] https://cachefly.cachefly.net/ips/cdn.txt
        [4] https://cachefly.execve.workers.dev/ips/rproxy.txt
        [5] https://cachefly.execve.workers.dev/ips/cdn.txt
        """
        import ipaddress

        ipv4_networks = []
        for url in self.ipv4_urls:
            data = self.http_get(url).text.strip()
            for line in data.split("\n"):
                ipv4_networks.append(str(ipaddress.IPv4Network(line, strict=False)))

        return {
            "ipv4": "\n".join(ipv4_networks),
            "ipv6": "",
        }

    def transform(self, response):
        ipv4_networks = [line.strip() for line in response["ipv4"].split("\n") if line.strip() != ""]
        ipv6_networks = [line.strip() for line in response["ipv6"].split("\n") if line.strip() != ""]
        return {
            "ipv4_prefixes": deduplicate_networks(ipv4_networks, filter_version=4),
            "ipv6_prefixes": deduplicate_networks(ipv6_networks, filter_version=6),
        }


CDN = CommonCDN(
    name="cachefly",
    asn_patterns=["cachefly"],
    cname_suffixes=[
        CNAMEPattern(
            suffix=".cachefly.net",
            source="https://help.cachefly.com/hc/en-us/articles/215068846-DNS-Configuration-for-CNAMEs-Hostname-Aliases",
            is_leaf=True,
        ),
    ],
    cidr=CacheFlyCIDR(),
)
