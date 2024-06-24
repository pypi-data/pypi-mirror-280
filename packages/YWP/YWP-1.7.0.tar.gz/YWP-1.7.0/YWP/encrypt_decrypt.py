class endecrypt:
    def aes_encrypt(file_path="", password=""):
        try:
            from Crypto.Util.Padding import pad
            from Crypto.Cipher import AES
            with open(file_path, 'rb') as f:
                data = f.read()
            key = password.encode('utf-8').ljust(32, b'\0')
            cipher = AES.new(key, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(data, AES.block_size))
            result = cipher.iv + ct_bytes
            output_path = file_path + ".ywpdne"
            with open(output_path, 'wb') as f:
                f.write(result)
            return 'done'
        except Exception as e:
            return str(e)

    def aes_decrypt(file_path="", password=""):
        try:
            from Crypto.Util.Padding import unpad
            from Crypto.Cipher import AES
            with open(file_path, 'rb') as f:
                data = f.read()
            key = password.encode('utf-8').ljust(32, b'\0')
            iv = data[:16]
            ct = data[16:]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            result = unpad(cipher.decrypt(ct), AES.block_size)
            output_path = file_path.replace(".ywpdne", "")
            with open(output_path, 'wb') as f:
                f.write(result)
            return 'done'
        except Exception as e:
            return str(e)

    def blowfish_encrypt(file_path="", password=""):
        try:
            from Crypto.Cipher import Blowfish
            from Crypto.Util.Padding import pad
            with open(file_path, 'rb') as f:
                data = f.read()
            key = password.encode('utf-8').ljust(32, b'\0')
            cipher = Blowfish.new(key, Blowfish.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(data, Blowfish.block_size))
            result = cipher.iv + ct_bytes
            output_path = file_path + ".ywpdne"
            with open(output_path, 'wb') as f:
                f.write(result)
            return 'done'
        except Exception as e:
            return str(e)

    def blowfish_decrypt(file_path="", password=""):
        try:
            from Crypto.Cipher import Blowfish
            from Crypto.Util.Padding import unpad
            with open(file_path, 'rb') as f:
                data = f.read()
            key = password.encode('utf-8').ljust(32, b'\0')
            iv = data[:8]
            ct = data[8:]
            cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
            result = unpad(cipher.decrypt(ct), Blowfish.block_size)
            output_path = file_path.replace(".ywpdne", "")
            with open(output_path, 'wb') as f:
                f.write(result)
            return 'done'
        except Exception as e:
            return str(e)

    def rsa_encrypt(file_path="", password=""):
        try:
            from Crypto.PublicKey import RSA
            with open(file_path, 'rb') as f:
                data = f.read()
            key = RSA.generate(2048)
            encrypted_data = key.publickey().encrypt(data, None)[0]
            result = key.export_key() + encrypted_data
            output_path = file_path + ".ywpdne"
            with open(output_path, 'wb') as f:
                f.write(result)
            return 'done'
        except Exception as e:
            return str(e)

    def rsa_decrypt(file_path="", password=""):
        try:
            from Crypto.PublicKey import RSA
            with open(file_path, 'rb') as f:
                data = f.read()
            private_key = RSA.import_key(data[:2048])
            encrypted_data = data[2048:]
            result = private_key.decrypt(encrypted_data)
            output_path = file_path.replace(".ywpdne", "")
            with open(output_path, 'wb') as f:
                f.write(result)
            return 'done'
        except Exception as e:
            return str(e)

    def base64_encrypt(file_path=""):
        try:
            import base64
            with open(file_path, 'rb') as f:
                data = f.read()
            result = base64.b64encode(data)
            output_path = file_path + ".ywpdne"
            with open(output_path, 'wb') as f:
                f.write(result)
            return 'done'
        except Exception as e:
            return str(e)
        
    def base64_decrypt(file_path=""):
        try:
            import base64
            with open(file_path, 'rb') as f:
                data = f.read()
            result = base64.b64decode(data)
            output_path = file_path.replace(".ywpdne", "")
            with open(output_path, 'wb') as f:
                f.write(result)
            return 'done'
        except Exception as e:
            return str(e)
        
    def hex_encrypt(file_path=""):
        try:
            import binascii
            with open(file_path, 'rb') as f:
                data = f.read()
            result = binascii.hexlify(data)
            output_path = file_path + ".ywpdne"
            with open(output_path, 'wb') as f:
                f.write(result)
            return 'done'
        except Exception as e:
            return str(e)
        
    def hex_decrypt(file_path=""):
        try:
            import binascii
            with open(file_path, 'rb') as f:
                data = f.read()
            result = binascii.unhexlify(data)
            output_path = file_path.replace(".ywpdne", "")
            with open(output_path, 'wb') as f:
                f.write(result)
            return 'done'
        except Exception as e:
            return str(e)
