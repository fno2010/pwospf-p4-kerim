from scapy.fields import BitField, ByteField, ShortField, IPField
from scapy.packet import Packet, bind_layers
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether, ARP

TYPE_CPU_METADATA = 0x081d


class CPUMetadata(Packet):
    name = "CPUMetadata"
    fields_desc = [ByteField("fromCpu", 0),
                   ShortField("origEtherType", None),
                   ShortField("srcPort", None),
                   IPField("arpDst", '0.0.0.0')]


bind_layers(Ether, CPUMetadata, type=TYPE_CPU_METADATA)
bind_layers(CPUMetadata, IP, origEtherType=0x0800)
bind_layers(CPUMetadata, ARP, origEtherType=0x0806)
