import os
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw() 
choice = '0';

while choice != '4':
	os.system("clear")
	print "*** NOTICE ***"
	print "have to install the application in first use."
	print "\n"
	print "WARNING! please run the following for checking dependecies at least once:"
	print "apt install python2.7 python-dpkt python-numpy make gnuplot texlive-latex-extra mupdf wireshark python-tk"
	print "\n"
	print "this application checked on ubuntu OS."
	print "**************"
	print "1. install"
	print "2. import pcap file"
	print "3. convert cap file to pcap"
	print "4. exit"
	print"\n"
	choice = raw_input('select your choice:')
	if choice == '1':
		os.system("sudo make")
	if choice == '3':
		print "enter full path cap file to convert and pcap file to create,"
		print "(if it already in this project folder, no need for full path)"
		print "cap file to convert: "
		capfile = askopenfilename()
		pcapfile = raw_input('pcap file to create: ') + ".pcap"
		os.system ("sudo editcap " + capfile + " " + pcapfile)
	if choice == '2':
		pcapfile = askopenfilename()
		subchoice = 0	
		while subchoice != '9':	
			print "------------------------------"
			print "what would you want to examing for this pcap file?"
			print "1. make a thoughtout grap"
			print "2. show packets"
			print "3. get pcap statistics"
			print "4. make a time sequence graph"
			print "5. make an inflight graph"
			print "6. make a spacing data graph"
			print "9. back"
			subchoice = raw_input("enter your choice: ")
			if subchoice == '1':
				os.system("sudo mkdir " + pcapfile + "thoughtoutgraphs")
				os.system("sudo rm -rf /" + pcapfile + "thoughtoutgraphs/*")
				os.system("sudo captcp throughput -i -o  " + pcapfile + "thoughtoutgraphs " + pcapfile)
				os.system("cd " + pcapfile +"thoughtoutgraphs; sudo make; xdg-open throughput.pdf")
			if subchoice == '4':
                                os.system("sudo mkdir " + pcapfile + "timesequencegraphs")
                                os.system("sudo rm -rf /" + pcapfile + "timesequencegraphs/*")
                                os.system("sudo captcp timesequence -f 1.2 -i -o  " + pcapfile + "timesequencegraphs " + pcapfile)
                                os.system("cd " + pcapfile +"timesequencegraphs; sudo make; xdg-open time-sequence.pdf")
			if subchoice == '5':
                                os.system("sudo mkdir " + pcapfile + "inflightgraphs")
                                os.system("sudo rm -rf /" + pcapfile + "inflightgraphs/*")
                                os.system("sudo captcp inflight -f 1.2 -i -o  " + pcapfile + "inflightgraphs " + pcapfile)
                                os.system("cd " + pcapfile +"inflightgraphs; sudo make; xdg-open inflight.pdf")
			if subchoice == '6':
                                os.system("sudo mkdir " + pcapfile + "spacinggraphs")
                                os.system("sudo rm -rf /" + pcapfile + "spacinggraphs/*")
                                os.system("sudo captcp spacing -f 1.1 -i -o  " + pcapfile + "spacinggraphs " + pcapfile)
                                os.system("cd " + pcapfile +"spacinggraphs; sudo make; xdg-open spacing.pdf")
			if subchoice == '2':
					command = ""
					print "do you want to filter..."
					print "1. by ip {proper ip address}"
					print "2. by port {port number}"
					print "3. none"
					subchoice2 = raw_input("enter your choice: ")
					if subchoice2 == '1':
						tmp = raw_input("enter the ip: ")
						command = " | grep " + tmp
					if subchoice2 == '2':
						tmp = raw_input("enter the port: ")
                                                command = " | grep :" + tmp
					if subchoice2 == '3':
                                                command = ""				
					os.system("sudo mkdir " + pcapfile + "logs")
					os.system("sudo rm -rf /" + pcapfile + "logs/packets")
					os.system("sudo captcp show " + pcapfile + command + " > " + pcapfile + "logs/packets")
					os.system("gedit " + pcapfile + "logs/packets")
			if subchoice == '3':
				subchoice2 = raw_input("if you want extended statistics press 1, else 0.")
				if subchoice2 == '1':
					command = " -e "
				os.system("sudo mkdir " + pcapfile + "logs")
				os.system("sudo rm -rf /" + pcapfile + "logs/statistics")
				os.system("sudo captcp statistic " + command + pcapfile + " > " + pcapfile + "logs/statistics")
				os.system("gedit " + pcapfile + "logs/statistics")
