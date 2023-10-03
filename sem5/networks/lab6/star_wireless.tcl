set val(chan)   Channel/WirelessChannel

set val(prop)   Propagation/TwoRayGround

set val(ant)    Antenna/OmniAntenna

set val(ll)     LL

set val(ifq)    Queue/DropTail/PriQueue

set val(ifqlen) 5

set val(netif)  Phy/WirelessPhy

set val(mac)    Mac/802_11

set val(rp)     DSDV

set val(nn)     5

set val(x)      2000

set val(y)      1000

set val(stop)   10

set val(traffic)        cbr

set val(traffic)        tcp


set ns    [new Simulator]


set     tracefd       [open out.tr w]

$ns    trace-all   $tracefd

set   namtrace       [open out.nam w]

$ns   namtrace-all-wireless   $namtrace  $val(x)  $val(y)


set topo [new Topography]

$topo load_flatgrid $val(x) $val(y)

set god_ [create-god $val(nn)]


$ns node-config -adhocRouting  $val(rp)

$ns node-config -llType  $val(ll)

$ns node-config -macType  $val(mac)

$ns node-config -ifqType  $val(ifq)

$ns node-config -ifqLen  $val(ifqlen)

$ns node-config -antType  $val(ant)

$ns node-config -propType  $val(prop)

$ns node-config -phyType  $val(netif)

$ns node-config -channelType  $val(chan)

$ns node-config -topoInstance  $topo

$ns node-config -agentTrace  ON

$ns node-config -routerTrace  ON

$ns node-config -macTrace  OFF

$ns node-config -movementTrace  ON

for {set i 0} {$i < $val(nn) } { incr i } {

set node_($i) [$ns node]

}


for {set i 0} {$i < $val(nn)} { incr i } {

# 30 defines the node size for nam

$ns initial_node_pos $node_($i) 60

}

proc destination {} {

        global ns val node_

        set time 1.0

        set now [$ns now]

        for {set i 0} {$i<$val(nn)} {incr i} {

                set xx [expr rand()*100]

                set yy [expr rand()*50]

                $ns at $now "$node_($i) setdest $xx $yy 1000.0"

        }

        $ns at [expr $now+$time] "destination"

}

for {set i 0} {$i < $val(nn) } {incr i } {

$node_($i) color yellow

$ns at 1.0 "$node_($i) color red"

}

for {set i 0} {$i < $val(nn) } {incr i } {

$node_($i) color yellow

$ns at 2.0 "$node_($i) color lightgreen"

}

for {set i 0} {$i < $val(nn) } {incr i } {

$node_($i) color yellow

$ns at 3.0 "$node_($i) color orange"

}

$ns at $val(stop) "$ns nam-end-wireless $val(stop)"

$ns at $val(stop) "stop"

$ns at 10.5 "puts \"end simulation\" ; $ns halt"

proc stop {} {

        global ns tracefd namtrace

        $ns flush-trace

        close $tracefd

        close $namtrace

        exec nam out.nam &

}

$ns run