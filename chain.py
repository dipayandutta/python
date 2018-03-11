import hashlib
import datetime as date

class block:

	def __init__(self,index,timestrap,data,previoushash):
		self.index = index
		self.timestrap = timestrap
		self.data = data
		self.previoushash = previoushash
		self.number_once = 0
		self.hash = self.calculate_hash()

	def calculate_hash(self):
		sha = hashlib.sha256()
		sha.update(
			str(self.index) +
			str(self.timestrap) +
			str(self.data) +
			str(self.previoushash) +
			str(self.number_once)
		)

		return sha.hexdigest()

	def mine_block(self,difficulty):
		while(self.hash[:difficulty] != "0"*difficulty):
			self.hash = self.calculate_hash()
			self.number_once += 1
		print "Mined Block ", self.hash
		return self.hash

	def check_if_mined(self,difficulty):
		new_hash = ""
		self.number_once = 0
		while(new_hash[:difficulty] != "0"*difficulty):
			new_hash = self.calculate_hash()
			self.number_once += 1 
		return new_hash 


class BlockChain(block):
	
	def __init__(self):
		self.chain = [self.create_block()]
		self.difficulty = 3

	def create_block(self):
		return block(0,date.datetime.now(),"First Block" ,"0")

	def get_latest_block(self):
		return self.chain[len(self.chain)-1]

	def add_block(self,new_block):
		new_block.previoushash = self.get_latest_block().hash
		new_block.mine_block(self.difficulty)
		self.chain.append(new_block)

	def print_chain(self):
		print "Starting Block Chain Application "
		print "Block Number :",self.chain[0].index ,"data :",self.chain[0].data
		print "Previous hash :",self.chain[0].previoushash
		print "current hash ",self.chain[0].calculate_hash()
		for i in xrange(1,len(self.chain)):
			print "Block Number ",self.chain[i].index ,"data",self.chain[i].data
			print "Previous Hash ",self.chain[i].previoushash
			print "Current Hash" , self.chain[i].mine_block(self.difficulty)

	
	def is_chain_valid(self):
		for i in range(1,len(self.chain)):
			if self.chain[i].hash != self.chain[i].check_if_mined(self.difficulty):
				print "Current Hash ",self.chain[i].hash ,"do not match the printed hash ",self.chain[i].check_if_mined(self.difficulty)
				return False
			elif self.chain[i-1].hash != self.chain[i].previoushash:
				print "Previous hash ",self.chain[i-1].previoushash ,"do not match the printed hash ",self.chain[i].previoushash
				return False

		return True


my_chain = BlockChain()

print "Block 1"
my_chain.add_block(block("1","12/2/2017",20,"0"))
print "Block 2"
my_chain.add_block(block("2","2/3/17",30,"0"))
print "-----------------------------------"
my_chain.print_chain()
print "--------------------------------------"

my_chain.is_chain_valid()
print "---------------------------------------"

my_chain.get_latest_block()