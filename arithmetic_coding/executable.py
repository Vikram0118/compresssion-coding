import main
frequency_table={"a":2,
		 "b":3,
		 "c":1,
		 "d":4}
AE=main.ArithmeticEncoding(frequency_table)
original_msg="abcd"
print("Original message:{msg}".format(msg=original_msg))
encoder,encoded_msg=AE.encode(msg=original_msg,probability_table=AE.probability_table)

print("Encoded message:{msg}".format(msg=encoded_msg))
decoder,decoded_msg=AE.decode(encoded_msg=encoded_msg,msg_length=len(original_msg),probability_table=AE.probability_table)


print("Decoded message:{msg}".format(msg=decoded_msg))
print("Message decoded successfully?{result}".format(result=original_msg==decoded_msg))
