import logging
logging.basicConfig(filename="ans4.log",level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
W = []
try:
    logging.info("Trying to get list of the Words")
    E = int(input("Entre the no. of the Words for sorting="))
    if E>0:
        for i in range(E):
            Words = input("Enter a Word for sorting=")
            W.append(Words)
        print("List of the Words for sorting is", W)
        logging.info("Successfully entered as per defined program")
        W.sort()
        print("List of the Words after sorting is",W)
    else:
        print("Kindly Try again and enter non zero positive no.")
except:
    logging.error("Kindly Try again and enter non zero positive no.")