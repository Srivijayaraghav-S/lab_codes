# Create a simulator instance
set ns [new Simulator]
$ns rtproto DV

# Open nam trace file and trace file
set nf [open "out.nam" w]
set tr [open "out.tr" w]
$ns namtrace-all $nf

set num 6

for {set i 1} {$i<$num} {incr i 2} {

set ftp($i) [new Application/FTP]
}

# Define a procedure to finish the simulation
proc finish {} {
    global ns nf tr
    $ns flush-trace
    close $nf
    close $tr
    exec nam out.nam &
    exit 0
}

# Creating Nodes

set packet_size 1024
for {set i 0} {$i < $num} {incr i} {
    set n($i) [$ns node]
}

# Creating Links (Mesh Topology)
for {set i 0} {$i < $num} {incr i} {
    for {set j 0} {$j < $num} {incr j} {
        if {$i != $j} {
            $ns duplex-link $n($i) $n($j) 1Mb 5ms DropTail
        }
    }
}

# Set up sources and destinations
for {set i 0} {$i < $num} {incr i} {
    if {$i % 2 == 0} {
        # Even-numbered nodes are destinations
        set sink($i) [new Agent/TCPSink]
        $ns attach-agent $n($i) $sink($i)
    } else {
        # Odd-numbered nodes are sources
        set tcp1($i) [new Agent/TCP]
        $ns attach-agent $n($i) $tcp1($i)
        $ftp($i) attach-agent $tcp1($i)
        $ns connect $sink([expr $i-1]) $tcp1($i)

    }
}


for {set i 0} {$i<$num} {incr i} {
 if {$i%2!=0} {
  $ns connect $sink([expr $i-1]) $tcp1($i)
  #$ns connect $sink([expr $i+1]) $tcp1($i)
        $tcp1($i) set packetSize_ $packet_size
        $tcp1($i) set rate_ [expr {$packet_size / 0.001}]
        $tcp1($i) set interval_ 0.005
        $ns at 0.1 "$ftp($i) start"
 $ns at 10 "$ftp($i) stop"
 }
 }


# Schedule the FTP start and stop

$ns at 10.1 "finish"

# Run the simulation
$ns run
