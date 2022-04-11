import os
def encode(text):
	os.system("echo You spent way too much time on this >> /tmp/encode/orig")
	os.system("echo '" + text + "' | basenc --base64 | basenc --base64url | basenc --base32 | basenc --base32hex | basenc --base16 | basenc --base2msbf | basenc --base2lsbf  | basenc --base64 | basenc --base64url | basenc --base32 | basenc --base32hex | basenc --base16 | basenc --base2msbf | basenc --base2lsbf  | basenc --base64 | basenc --base64url | basenc --base32 | basenc --base32hex | basenc --base16 | basenc --base2msbf | basenc --base2lsbf >> ./encrypted_file")
def decode():
	os.system("cat ./encrypted_file | basenc -d --base2lsbf | basenc -d --base2msbf | basenc -d --base16 | basenc -d --base32hex | basenc -d --base32 | basenc -d --base64url | basenc -d --base64 | basenc -d --base2lsbf | basenc -d --base2msbf | basenc -d --base16 | basenc -d --base32hex | basenc -d --base32 | basenc -d --base64url | basenc -d --base64  | basenc -d --base2lsbf | basenc -d --base2msbf | basenc -d --base16 | basenc -d --base32hex | basenc -d --base32 | basenc -d --base64url | basenc -d --base64 >> ./decoded")

