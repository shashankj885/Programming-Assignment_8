import logging
logging.basicConfig(filename="ans3.log",level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
while True:
    try:
        logging.info("Trying to get the no. of the Rows and Columns of the matrix")
        R = int(input("Entre a no. of rows of Matrix="))
        C = int(input("Entre a no. of columns of Matrix="))
        if R > 0 and C > 0:
            print("Enter a elements of matrix Row Wise=")
            logging.info("Successfully entered the Row and Columns as per defined program")
            break
        else:
            print("Rows and Columns should be non zero positive no. ")
    except:
        logging.error("Kindly enter non zero positive no.")
Matrix = []
try:
    logging.info("trying to enter the elements of Matrix")
    for i in range(R):
        a= []
        for j in range(C):
            a.append(int(input()))
        M = Matrix.append(a)
    logging.info("trying to print the elements of Matrix")
    for i in range(R):
        for j in range(C):
            print(Matrix[i][j], end=" ")
        print()
    print("Transpose of the Matrix is=")
    for i in range(C):
        for j in range(R):
            print(Matrix[j][i], end=" ")
        print()
except Exception as e:
    logging.error("Kindly re-start the program and enter only numerical vales")
    print("Kindly re-start the program and enter only numerical vales")