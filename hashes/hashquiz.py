

msg1 = """

 Quiz 3

 Date: 11/5/2025 (Wednesday), during Class, for 20 minutes. 

 Topics:

 Classes: Getters and Setters, Static Methods, Class Methods, Inheritance, Operator Overloading

 Files: Reading, Writing, pathlib Module, JSON Files

 Exceptions 

 Cryptography: Hashing, Encoding/Decoding

 Lectures:

 11 - 18

"""

msg2 = """

 Quiz 3

 Date: 11/3/2025 (Monday), during Class, for 20 minutes. 

 Topics:

 Classes: Getters and Setters, Static Methods, Class Methods, Inheritance, Operator Overloading

 Files: Reading, Writing, pathlib Module, JSON Files

 Exceptions 

 Cryptography: Hashing, Encoding/Decoding

 Lectures:

 11 - 18

"""




msg3 = """

 Quiz 3

 Date: 11/10/2025 (Monday), during Class, for 20 minutes. 

 Topics:

 Classes: Getters and Setters, Static Methods, Class Methods, Inheritance, Operator Overloading

 Files: Reading, Writing, pathlib Module, JSON Files

 Exceptions 

 Cryptography: Hashing, Encoding/Decoding

 Lectures:

 11 - 18

"""


def gethashValue(message):
    hash_value = 0
    for char in message:
        hash_value *= 31
        hash_value += ord(char)
        hash_value %= 10007
    return hash_value

print(gethashValue(msg1))
print(gethashValue(msg2))
print(gethashValue(msg3))