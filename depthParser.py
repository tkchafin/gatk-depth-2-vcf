#!/usr/bin/python

import sys
import os
import getopt

def main():
	params = parseArgs()


#Object to parse command-line arguments
class parseArgs():
	def __init__(self):
		#Define options
		try:
			options, remainder = getopt.getopt(sys.argv[1:], 'p:f:hn:o:', \
			["popmap=","help","fasta=","nex=","out="])
		except getopt.GetoptError as err:
			print(err)
			self.display_help("\nExiting because getopt returned non-zero exit status.")
		#Default values for params
		#Input params
		self.popmap=None
		self.out=None
		self.fasta=None
		self.nex=None

		#First pass to see if help menu was called
		for o, a in options:
			if o in ("-h", "-help", "--help"):
				self.display_help("Exiting because help menu was called.")

		#Second pass to set all args.
		for opt, arg_raw in options:
			arg = arg_raw.replace(" ","")
			arg = arg.strip()
			opt = opt.replace("-","")
			#print(opt,arg)
			if opt in ('p', 'popmap'):
				self.popmap = arg
			elif opt in ('h', 'help'):
				pass
			elif opt in ('o','out'):
				self.out = arg
			elif opt in ("f","fasta"):
				self.fasta = arg
			elif opt in ("n","nex"):
				self.nex = arg
			else:
				assert False, "Unhandled option %r"%opt

		#Check manditory options are set
		if not self.popmap:
			self.display_help("Error: Missing required popmap file (-p,--popmap).")



	def display_help(self, message=None):
		if message is not None:
			print()
			print (message)
		print ("\nparseDepths.py\n")
		print ("Contact:Tyler K. Chafin, University of Arkansas,tkchafin@uark.edu")
		print ("\nUsage: ", sys.argv[0], "-i <rtable from GATK> \n")
		print ("Description: Creates a VCF file of positions of acceptable depth from GATK DepthOfCoverage results")

		print("""
	Arguments:
		-i,--input	: 'rtable' from GATK DepthOfCoverage
		-r,--ref	:
		-f,--fasta	: Path to FASTA-formatted haplotype sequences
			--Note for diplotypes:
				Paired haplotypes should be formatted as SampleName_A and _B
		-n,--nex	: Optionally, can provide a NEXUS file to append to.
		-h,--help	: Displays help menu

""")
		print()
		sys.exit()

#Call main function
if __name__ == '__main__':
    main()
