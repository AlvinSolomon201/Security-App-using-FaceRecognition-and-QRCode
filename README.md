# Security-App-using-FaceRecognition-and-QRCode
A security authorisation application built in Python and OpenCV. It have 2 factor authentication process for validation of identity. It scans QR Code in real-time and recognizes face in photos clicked in real-time.
It also uses 128-bit AES File encryption to protect the key generates for encryption and decryption of face models.

Security with QR Code and Face Recognition
This is a Security App which uses Face Recognition and Scans QR Code which is unique to each individual in an organisation.
It goes to these authentication process for giving successfull access to entry in premises or any kind of access required for that matter.
Below are the steps to run the Security App:
  • Create Virtual Environment and install the required modules of Python from 'requirement.txt' file using 'pip'.
  • Go to 'Security' folder from terminal and run the 'security.py' file by enter 'python security.py'
  • Select option for 'Guest' or 'College Person'.
  • A college person will require a face id and his unique QR code
  • A guest only needs to enter his name
  • Only successfull access of any kind of entry person, his/her 'Name' & 'ID' will be recorded in MySQL database along with the entry timestamp automatically.
