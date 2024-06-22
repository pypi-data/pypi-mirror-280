import ArimaTP as ATP
import TitanTorch

def ArimaTP(file_csv,name_columna,num_predictions=60):
	ATP.run(file_csv,name_columna,num_predictions)

def ChatBot(file):
	response = TitanTorch.ChatBot(file)