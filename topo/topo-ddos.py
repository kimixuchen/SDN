import sys
from mininet.topo import Topo
from mininet.node import Host
from mininet.net import Mininet

class MyTopo( Topo ):
    def __init__( self ):
        # Initialize topology
        Topo.__init__( self )
        
        # Add hosts and switches
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        for h in range(10):
            host = self.addHost('h%s' % (h+1))
            self.addLink(host, switch1, 1, h+1)
        for h in range(10, 20):
            host = self.addHost('h%s' % (h+1))
            self.addLink(host, switch2, 1, h+1-10)
        
        host21 = self.addHost( 'h21' )
        self.addLink( host21, switch3, 1, 1)
        
        # Add links
        self.addLink( switch1, switch3, 11, 2)
        self.addLink( switch2, switch3, 11, 3)

topos = { 'mytopo':(lambda: MyTopo() ) }
