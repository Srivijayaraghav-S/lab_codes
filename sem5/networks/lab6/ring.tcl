#This Program will create a ring topology using less number of statements in TCL Language
set ns [new Simulator]
$ns rtproto DV

set nf [open "out.nam" w]
set tr [ open "out.tr" w]
$ns namtrace-all $nf

set num 5
for {set i 1} {$i<$num} {incr i 2} {
 set ftp($i) [new Application/FTP]
 }


proc finish {} {
        global ns nf tr
        $ns flush-trace
        close $nf
        close $tr
        exec nam out.nam &
        exit 0
        }

#Creating Nodes

set packet_size 1024
for {set i 0} {$i<$num} {incr i} {
set n($i) [$ns node]
}

#Creating Links
for {set i 0} {$i<$num} {incr i} {
$ns duplex-link $n($i) $n([expr ($i+1)%$num]) 1Mb 10ms DropTail
}

for {set i 0} {$i < $num} {incr i} {
    if {$i % 2 == 0} {
        # Even-numbered nodes are destinations
        set sink($i) [new Agent/TCPSink]
        $ns attach-agent $n($i) $sink($i)
        #if { $i != 0 } {
        #$ns connect $tcp1([expr $i-1]) $sink($i)
        #}

        } else {
        # Odd-numbered nodes are sources
        set tcp1($i) [new Agent/TCP]
        $ns attach-agent $n($i) $tcp1($i)
        $ftp($i) attach-agent $tcp1($i)

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



$ns at 10.1 "finish"


$ns run