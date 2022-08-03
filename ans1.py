import logging
logging.basicConfig(filename="ans1.log",level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
while True:
    try:
        logging.info("Trying to get the no. of the Rows and Columns of both the matrix")
        R1 = int(input("Entre a no. of rows of first Matrix="))
        C1 = int(input("Entre a no. of columns of first Matrix="))
        R2 = int(input("Entre a no. of rows of Second Matrix="))
        C2 = int(input("Entre a no. of columns of Second Matrix="))
        if R1 > 0 and C1 > 0 and R2 > 0 and C2 > 0:
            if R1 == R2 and C1 == C2:
                print("Enter a elements for first matrix Row Wise=")
                logging.info("Successfully entered the Row and Columns as per defined program")
                break
            else:
                print("No. of Row and Columns of Both the Matrix should equal, Kindly re enter values")
        else:
            print("Rows and Columns should be non zero positive no. ")
    except:
        logging.error("Kindly enter non zero positive no.")
Matrix1 = []
Matrix2 = []
try:
    logging.info("trying to enter the elements of Matrix1")
    for i in range(R1):
        a1 = []
        for j in range(C1):
            a1.append(int(input()))
        M1 = Matrix1.append(a1)
    logging.info("trying to print the elements of Matrix1")
    for i in range(R1):
        for j in range(C1):
            print(Matrix1[i][j], end=" ")
        print()
    print("Enter a elements for Second matrix Row Wise=")
    logging.info("trying to enter the elements of Matrix2")
    for i in range(R2):
        a2 = []
        for j in range(C2):
            a2.append(int(input()))
        M2 = Matrix2.append(a2)
    logging.info("trying to print the elements of Matrix2")
    for i in range(R2):
        for j in range(C2):
            print(Matrix2[i][j], end=" ")
        print()
    print("Multiplication of the Matrix1 and Matrix2 is =")
    for i in range(R2):
        for j in range(C2):
            print(Matrix1[i][j] * Matrix2[i][j], end=" ")
        print()
except Exception as e:
    logging.error("Kindly re-start the program and enter only numerical vales")
    print("Kindly re-start the program and enter only numerical vales")