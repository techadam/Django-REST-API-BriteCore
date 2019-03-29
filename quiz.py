from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

message = b'gAAAAABckW1M9pPXyhLeZQ7D8d9V2ubPNkxguiwZ2qFP5e_Qs6_AJm1EvJzDThLGJmlaSf-ooouaypKT27V9fm_QybBv68__BaEtOFA3GioLZIGxmSVHqD2PlaxAVDKWtFc5i6qYva2kCNA-qnl7DQCUBflRcR96f2knq6FNDFix9RrlRHueeWo='

def main():
	f = Fernet(key)
	print(f.decrypt(message))


if __name__ != '__main__':
	main()
	

# b'https://engineering-application.britecore.com/e/t19e119s2t/testProductEngineer'