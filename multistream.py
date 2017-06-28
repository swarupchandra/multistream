import sys
from manager import Manager
from properties import Properties



def main():
	# datasetName = 'powersupply_normalized'
	datasetName = sys.argv[1]

	props = Properties('config.properties', datasetName)
	srcfile = Properties.BASEDIR + datasetName + Properties.SRCAPPEND
	trgfile = Properties.BASEDIR + datasetName + Properties.TRGAPPEND
	mgr = Manager(srcfile, trgfile)

	Properties.logger.info(props.summary())
	Properties.logger.info('Start Stream Simulation')

	mgr.start(datasetName)
	# mgr.start2(datasetName)

	#baseline methods
	# mgr.start_skmm(datasetName)
	# mgr.start_mkmm(datasetName)
	# mgr.start_srconly(datasetName)
	# mgr.start_trgonly(datasetName)

	mgr.gateway.shutdown()


if __name__ == '__main__':
	main()
