import re        
import numpy as np
# for random shuffles
import random		
# for getting times for computation
from datetime import datetime		
# for confidence_interval computation	
from scipy import stats				
# for copying lists
import copy								                             

#we set the number of blocks and the number of agents per block and the number of products per block here
blocks = 10
blocksize = 4
numitems = 30
adjustedblocks = 0
locations = set()
locationA = "test"

#Here we define the functions for reading the input files							
def interpret_file_line(line):

	"""
		Interprets a line of the file, and returns six components:
		Location, Block #, Agent #, Order, Product ID, Price
	"""
	
	chunks = re.split(",", line)
	
	location = chunks[0].strip()
	blockno = chunks[1].strip()
	agentno = chunks[2].strip()
	orderno = chunks[3].strip()
	productid =  chunks[4].strip()
	price = chunks[5].strip()

	#capture the name of the first location
	if (locationA == "test"):
		global locationA
		locationA = location
	
	#check if the location is the same as the first location
	#if yes, then we need to set the agentno to be 1 and 2
	#if no, we need to set the agentno to be 3 and 4
	if (location == locationA):
		if (int(agentno) == 3):
			agentno = 1
		elif (int(agentno) == 4):
			agentno = 2
	else:
		if (int(agentno) == 1):
			agentno = 3
		elif (int(agentno) == 2):
			agentno = 4

	
	return location, blockno, agentno, orderno, productid, price

def read_file(input_file):			
	
	"""
		creates a dictionary called input_data
		with the following keys: location, blockno, agentno, orderno, productid, price
		each key will have a list as a value
    """
	
	input_data = {'location':[], 'blockno':[], 'agentno':[], 'orderno':[], 'productid':[], 'price':[]}
	print "Reading file"
	fo = open(input_file, "r")
	
	for line in fo:
		location, blockno, agentno, orderno, productid, price = interpret_file_line(line)
		
		input_data['location'].append(location)
		input_data['blockno'].append(blockno)
		input_data['agentno'].append(agentno)
		input_data['orderno'].append(orderno)
		input_data['productid'].append(productid)
		input_data['price'].append(price)
		
		#set the location information
		locations.add(location)

	print "Reading complete. Blocks read: ", blockno
	global adjustedblocks 
	adjustedblocks = blockno
	
	return input_data

#Here we define the test stat functions
def jaccard_index(observed_values, unit_assignments):
	"""
		Compute the Jaccard Index
	"""
	
	jaccardsum = 0
	
	#items that belong to set A, C = those items with unit_assignments = 0
	#items that belong to set B, D = those items with unit_assignments = 1
	#we will compute the jaccard index per block as follows:
	#agent 1 (location A) will be compared to agent 3 (location B)
	#agent 2 (location A) will be compared to agent 4 (location B)
	#thus, each block will result in 2 jaccard index computations
	#at the end of all blocks, we will average the results
	
	for i in range(0, blocks):
		setA = set()
		setB = set()
		setC = set()
		setD = set()
		for j in range(0, blocksize):
			#get the index values for all entries with this block number and agent no
			block = []
			agents = []
			block = observed_values.get('blockno')
			agents = observed_values.get('agentno')
			indexes = []
			for k, blockno in enumerate(block):
				if ((int(blockno) == i+1) and (int(agents[k]) == j+1)):
					indexes.append(k)		
		
			#get all the productids for this block
			products = []
			products = observed_values.get('productid')
			productlist = []
			for k in range(len(indexes)):
				productlist.append(products[indexes[k]])
			
			#check if the item belongs to set A or set B
			if (unit_assignments[i][j]==0):
				if (len(setA) == 0):
					#assign products in agent 1 to set A
					setA = set(productlist)
				else:
					#assign products in agent 2 to set C
					setC = set(productlist)
			else:
				if (len(setB) == 0):
					#assign products in agent 3 to set B
					setB = set(productlist)
				else:
					#assign products in agent 4 to set D
					setD = set(productlist)
			
		#compute the jaccard index for the block then add it up so we can return the average jaccard index
		numunion = len(setA.union(setB))
		numint = len(setA.intersection(setB))	
		jaccardsum += float(numint)/float(numunion)
		#temp=float(numint)/float(numunion)
		#print "jaccard1: ", temp
		
		numunion = len(setC.union(setD))
		numint = len(setC.intersection(setD))	
		jaccardsum += float(numint)/float(numunion)
		#temp=float(numint)/float(numunion)
		#print "jaccard2: ", temp
		
	#return the average value of the jaccard indexes across all blocks
	return jaccardsum/(blocks*2)

def absolute_diff(observed_values, unit_assignments):
	"""
		Compute the sum of the absolute value of price differences for list A and list B
	"""
	
	
	#items that belong to list A, C = those items with unit_assignments = 0
	#items that belong to list B, D = those items with unit_assignments = 1
	#we will compute the price difference per block as follows:
	#agent 1 (location A) will be compared to agent 3 (location B)
	#agent 2 (location A) will be compared to agent 4 (location B)
	#thus, each block will result in 2 price difference computations
	#at the end of all blocks, we will average the results
	
	#the sum of the absolute difference of prices will be computed only on the intersection of products in both lists
	#if there is zero intersection between the 2 lists, we will discard that block
	
	absdiffsum = 0
	adj = 0
	
	for i in range(0, int(adjustedblocks)):
		setA = set()
		setB = set()
		setC = set()
		setD = set()
		dictA = {}
		dictB = {}
		dictC = {}
		dictD = {}
		for j in range(0, blocksize):
			#get the index values for all entries with this block number and agent no
			block = []
			agents = []
			block = observed_values.get('blockno')
			agents = observed_values.get('agentno')
			indexes = []
			for k, blockno in enumerate(block):
				if ((int(blockno) == i+1) and (int(agents[k]) == j+1)):
					indexes.append(k)		
		
			#get all the productids and prices for this block
			products = []
			products = observed_values.get('productid')
			prices = []
			prices = observed_values.get('price')
			#create a dictionary that contain the productid:price
			productpricelist = {}
			#create a product list
			productlist = []
			for k in range(len(indexes)):
				productpricelist[products[indexes[k]]] = prices[indexes[k]]
				productlist.append(products[indexes[k]])
			
			#check if the item belongs to set A or set B
			if (unit_assignments[i][j]==0):
				if (len(setA) == 0):
					#now we need to assign everything in this block for agent 1 to dictA and setA
					dictA.update(productpricelist)
					setA = set(productlist)		
				else:
					#now we need to assign everything in this block for agent 3 to dictC and setC
					dictC.update(productpricelist)
					setC = set(productlist)		
			else:
				if (len(setB) == 0):
					#now we need to assign everything in this block for agent 2 to dictB and setB
					dictB.update(productpricelist)
					setB = set(productlist)		
				else:
					#now we need to assign everything in this block for agent 4 to dictD and setD
					dictD.update(productpricelist)
					setD = set(productlist)		
			
		#get the intersection of the products so we can use this to compute the price differences
		productint = setA.intersection(setB)
		if (len(productint) == 0):
			adj += 1
	
		#compute the absolute difference of the prices in dictA and dictB
		#then add it all up
		for x in productint:
			absdiffsum += abs(float(dictA[x]) - float(dictB[x]))
			
		#print "absdiff1: ", absdiffsum
		#get the intersection of the products so we can use this to compute the price differences
		productint = setC.intersection(setD)
		if (len(productint) == 0):
			adj += 1
			
		#compute the absolute difference of the prices in dictC and dictD
		#then add it all up
		for x in productint:
			absdiffsum += abs(float(dictC[x]) - float(dictD[x]))
		
		#print "absdiff2: ", absdiffsum
	#return the average value of the sum of abs differences across all blocks
	return absdiffsum/((int(adjustedblocks)*2) - adj)
		
def kendallstau(observed_values, unit_assignments):
	"""
		Compute the kendall's tau value for list A and list B
		then use the jaccard index to weigh the result
	"""
	
	#items that belong to list A, C = those items with unit_assignments = 0
	#items that belong to list B, D = those items with unit_assignments = 1
	
	#for this function, we are doing several things 
	#first we get the jaccard index for the block using the same logic as jaccard_index()
	#this will be used to weigh the kendall's tau value in order to factor in the situation where the set of products in location A is not the same as the one from location B
	#then we compute the kendall's tau value for the 2 agents at each location as follows:
	#agent 1 (location A) will be compared to agent 3 (location B)
	#agent 2 (location A) will be compared to agent 4 (location B)
	#thus, each block will result in 2 kendall's tau computations
	#at the end of all blocks, we will average the results
	
	
	kendallstausum = 0
	adj = 0
	for i in range(0, int(adjustedblocks)):
		setA = set()
		setB = set()
		setC = set()
		setD = set()
		dictA = {}
		dictB = {}
		dictC = {}
		dictD = {}
		for j in range(0, blocksize):
			#get the index values for all entries with this block number and agent no
			block = []
			agents = []
			block = observed_values.get('blockno')
			agents = observed_values.get('agentno')
			indexes = []
			for k, blockno in enumerate(block):
				if ((int(blockno) == i+1) and (int(agents[k]) == j+1)):
					indexes.append(k)		
		
			#get all the productids for this block
			#also, create a dictionary that contain the productid:order
			products = []
			products = observed_values.get('productid')
			orders = []
			orders = observed_values.get('orderno')
			productlist = []
			productorderlist = {}
			
			for k in range(len(indexes)):
				productlist.append(products[indexes[k]])
				productorderlist[products[indexes[k]]] = orders[indexes[k]]
				
			#check if the item belongs to set A or set B
			if (unit_assignments[i][j]==0):
				if (len(dictA) == 0):
					#update dictA with the product order list
					dictA.update(productorderlist)
					#now we need to assign everything in this block for this agent to set A
					setA = set(productlist)				
				else:
					#update dictC with the product order list
					dictC.update(productorderlist)
					#now we need to assign everything in this block for this agent to set C
					setC = set(productlist)		
			else:
				if (len(dictB) == 0):
					#update dictB with the product order list
					dictB.update(productorderlist)
					#now we need to assign everything in this block for this agent to set B
					setB = set(productlist)				
				else:
					#update dictD with the product order list
					dictD.update(productorderlist)
					#now we need to assign everything in this block for this agent to set D
					setD = set(productlist)		
			
		#compute the jaccard indexes for the block 
		numunion = len(setA.union(setB))
		numint = len(setA.intersection(setB))	
		jaccard1 = float(numint)/float(numunion)
		if (numint == 0):
			adj += 1
			
		numunion = len(setC.union(setD))
		numint = len(setC.intersection(setD))	
		jaccard2 = float(numint)/float(numunion)
		if (numint == 0):
			adj += 1	
		
		#note - we set kendall's tau to 0 of there is no intersection between the 2 sets, and we set it to 1 if 
		#the ranking order is the same in both sets
		
		#get the intersection between the products in setA and setB
		#then create lists of the ordered values for dictA and dictB
		setint = setA.intersection(setB)
		listx = []
		listy = []
		for productid in setint: 
			listx.append(dictA[productid])
			listy.append(dictB[productid])
		
		#compute the numerator for kendall's tau between setA and setB
		numerator = 0
		if (len(setint) == 0):
			numerator == 0
		else:
			for g in range(1,len(listx)):
				for h in range(0,g):
					if (((int(listx[g]) > int(listx[h])) and (int(listy[g]) > int(listy[h]))) or ((int(listx[g]) < int(listx[h])) and (int(listy[g]) < int(listy[h])))):
						numerator = numerator + 1
					elif (((int(listx[g]) > int(listx[h])) and (int(listy[g]) < int(listy[h]))) or ((int(listx[g]) < int(listx[h])) and (int(listy[g]) > int(listy[h])))):
						numerator = numerator - 1
			
		#compute kendall's tau weighted by the first jaccard index
		if numerator == 0: #this means no correlation
			kendallstausum += 0
			#print "KT1: 0"
		else:
			kendallstausum += float(numerator)/float(len(listx)*(len(listx)-1)/2) * jaccard1
			#print "KT1: ", float(numerator)/float(len(listx)*(len(listx)-1)/2) * jaccard1
		
		#get the intersection between the products in setC and setD
		#then create lists of the ordered values for dictC and dictD
		setint = setC.intersection(setD)
		listx = []
		listy = []
		for productid in setint: 
			listx.append(dictC[productid])
			listy.append(dictD[productid])
		
		#compute the numerator for kendall's tau between setC and setD
		numerator = 0
		if (len(setint) == 0):
			numerator == 0
		else:
			for g in range(1,len(listx)):
				for h in range(0,g):
					if (((int(listx[g]) > int(listx[h])) and (int(listy[g]) > int(listy[h]))) or ((int(listx[g]) < int(listx[h])) and (int(listy[g]) < int(listy[h])))):
						numerator = numerator + 1
					elif (((int(listx[g]) > int(listx[h])) and (int(listy[g]) < int(listy[h]))) or ((int(listx[g]) < int(listx[h])) and (int(listy[g]) > int(listy[h])))):
						numerator = numerator - 1
			
		#compute kendall's tau weighted by the second jaccard index
		if numerator == 0: #this means no correlation
			kendallstausum += 0
			#print "KT2: 0"
		else:
			kendallstausum += float(numerator)/float(len(listx)*(len(listx)-1)/2) * jaccard2
			#print "KT2: ", float(numerator)/float(len(listx)*(len(listx)-1)/2) * jaccard2
			
		
	#return the average value of the kendall's tau across all blocks
	return kendallstausum/((int(adjustedblocks) * 2) - adj)
	
		
#Here we define the functions for running the analytical tests	
def get_perm(ylabel):									
	"""
		Generate a permutation for block_p_test.
	"""
	yret = copy.deepcopy(ylabel)
	
	#shuffle the current sequence of the agents in the block
	for i in range(blocks):
		random.shuffle(yret[i])	
	
	return yret
	
def proportion_confint(count, nobs, alpha=0.05):
	q_ = count * 1. / nobs
	alpha_2 = 0.5 * alpha

	#always use beta method
	ci_low = stats.beta.ppf(alpha_2 , count, nobs - count + 1)
	ci_upp = stats.beta.isf(alpha_2, count + 1, nobs - count)
	
	return ci_low, ci_upp
	
#change iterations to 1000 later
def blocked_sampled_test(input_data, unit_assignments, test_stat, alpha=0.01, iterations=1000):
	"""
		Run a block permutation test.
	"""
	
	s = datetime.now()
	Tobs = test_stat(input_data, unit_assignments)
	print 'Tobs: ', Tobs
	under = 0
	for i in range(0,iterations):
		permuted_assignments = get_perm(unit_assignments)
		Tpi = test_stat(input_data, permuted_assignments)
		print 'Tpi: ', Tpi
		if round(Tobs, 10) <= round(Tpi, 10):
		    under += 1
	
	e = datetime.now()
	print "---Time for running permutation test: ", str(e-s)
	print "\nConfidence Interval of p-value:", proportion_confint(under, iterations, alpha)
	return (1.0*under) / (1.0*iterations)


#Main Program starts here	

#read the input file
#input_data = read_file("Extracted data/ebay_usa_vs_indonesia.txt")
#input_data = read_file("Extracted data/orbitz_usa_vs_indonesia.txt")
#input_data = read_file("Extracted data/taobao_US_VS_Indonesia.txt")
input_data = read_file("Extracted data/expedia_US_VS_Indonesia.txt")

#set the original sequence of the agents in the block
#fill up the unit_assignments table, which will be used for permutation later
unit_assignments = []
for i in range(blocks):
	unit_assignments.append([0, 0, 1, 1])

print "Executing the experiment for locations:"
for site in locations:
	print site
	
print "Computing Sum of the Absolute Difference for Product Price experiment"
pvalue = blocked_sampled_test(input_data, unit_assignments, absolute_diff)
print "p-value: ", pvalue
	
print "Computing Jaccard Index for Product List experiment"
pvalue = blocked_sampled_test(input_data, unit_assignments, jaccard_index)
print "p-value: ", pvalue

print "Computing Weighted Kendall's Tau for Product Ranking experiment"
pvalue = blocked_sampled_test(input_data, unit_assignments, kendallstau)
print "p-value: ", pvalue



