# Lauren Farr - March 31, 2022

# Base 64 encoding/decoding program

# constants
BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" 

def main():

    # print title and prompt user for encode or decode
    print("Base-64 Encoder and Decoder")
    print("===========================")
    print()
    user_choice = input("Would you like to decode <d> or encode <ENTER>? ")

    # if the user chose decode
    if user_choice == "d" or user_choice == "D":

        # prompt user for string to decode
        input_string = input("Enter a base-64 string to be decoded: ")

        # initialize final result string
        decoded_string = ""

        # get four characters at a time from the input string
        for index in range(0, len(input_string), 4):
            string_segment = input_string[index:index+4]

            # decode those four characters
            decoded_segment = decode(string_segment)

            # add the decoded string to the final result string
            decoded_string += decoded_segment

        # print the final result string
        print()
        print("Your decoded string is:")
        print(decoded_string)

    # if the user chose encode
    else:

        # prompt user for string to encode
        input_string = input("Enter a string to be encoded in base-64: ")

        # initialize final result string
        encoded_string = ""

        # get three characters at a time from the input string
        for index in range(0, len(input_string), 3):
            string_segment = input_string[index:index+3]

            # encode those three characters
            encoded_segment = encode(string_segment)

            # add the encoded string to the final result string
            encoded_string += encoded_segment

        # print the final result string
        print()
        print("Your encoded string is:")
        print(encoded_string)

def decode( string_segment ):

    # set up empty arry to hold base-64 integer values
    base_64_values = []

    # for each character in the base-64 string
    for character in string_segment:

        # if it is not an equal sign
        if character != "=":

            # for each index of the BASE64 constant
            for index in range(len(BASE64)):

                # if the character is the same as the character in BASE64
                if BASE64[index] == character:
                    
                    # add that base64 int value to the array
                    base_64_values.append(index)

    # get the first ascii int value - guaranteed to have at least numbers in array
    ascii_1 = (base_64_values[0] << 2) + ((base_64_values[1] & 0x30) >> 4)

    # if the array has 4 values
    if len(base_64_values) == 4:
        # get the other ascii values of those integers
        ascii_2 = ((base_64_values[1] & 0xF) << 4) + ((base_64_values[2] & 0x3C) >> 2)
        ascii_3 = ((base_64_values[2] & 0x3) << 6) + base_64_values[3]

        # return the character versions of the ascii values concatonated together
        return chr(ascii_1) + chr(ascii_2) + chr(ascii_3)

    # if the array has 3 values
    elif len(base_64_values) == 3:
        # get the other ascii value of the other integer
        ascii_2 = ((base_64_values[1] & 0xF) << 4) + ((base_64_values[2] & 0x3C) >> 2)

        # return the character versions of the ascii values concatonated together
        return chr(ascii_1) + chr(ascii_2)

    # if the array only has 2 values
    else:

        # return the character version of the ascii value
        return chr(ascii_1)
                     
def encode( string_segment ):

    # convert the first character in the string to its ascii value
    # segment guaranteed to have at least 1 character
    ascii_1 = ord(string_segment[0])

    # grab the first six bits of that number
    num_1 = ascii_1 >> 2

    # if the segment is 3 characters
    if len(string_segment) == 3:
        # get the ascii values of the other two
        ascii_2 = ord(string_segment[1])
        ascii_3 = ord(string_segment[2])
        
        # convert them to 6-bit format
        num_2 = (( ascii_1 << 4 ) & 0x3F ) + (ascii_2 >> 4)
        num_3 = ((ascii_2 << 2) & 0x3F) + (ascii_3 >> 6)
        num_4 = ascii_3 & 0x3F

        # return the base64 encoding of all 4 6-bit numbers
        return BASE64[num_1] + BASE64[num_2] + BASE64[num_3] + BASE64[num_4]

    # if the segment is two characters long
    elif len(string_segment) == 2:
        # convert the other character to ascii
        ascii_2 = ord(string_segment[1])
        # create 8 bits of 0 for the last two bits of third 6-bit number
        ascii_3 = 0

        # convert to 6-bit format
        num_2 = (( ascii_1 << 4 ) & 0x3F ) + (ascii_2 >> 4)
        num_3 = ((ascii_2 << 2) & 0x3F) + (ascii_3 >> 6)

        # return base64 encoding of 3 6-bit numbers, with 1 =
        return BASE64[num_1] + BASE64[num_2] + BASE64[num_3] + "="

    # if the segment is 1 character long
    else:
        # create 8 bits of 0 for the last two bits of second 6-bit number
        ascii_2 = 0

        # convert to 6-bit format
        num_2 = (( ascii_1 << 4 ) & 0x3F ) + (ascii_2 >> 4)

        # return base64 encoding of 2 6-bit numbers, with 2 =
        return BASE64[num_1] + BASE64[num_2] + "=="
main()    
