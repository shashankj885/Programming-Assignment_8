import logging
logging.basicConfig(filename="ans5.log", level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
try:
    logging.info("Trying to get into the program")
    Sentence = input("Enter a sentence  with punctuation marks :")
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in Sentence:
        if i in punc:
            Sentence = Sentence.replace(i, " ")
    print("Sentence without punctuation mark is :",Sentence)
except:
    logging.error("Kindly Try again and enter non zero positive no.")