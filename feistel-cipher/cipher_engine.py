from feistel_rounds import feistel_encrypt_block, feistel_decrypt_block
import base64

# Convert text to binary blocks
def string_to_binary_blocks(text, block_size=16):
    binary = ''.join(format(ord(c), '08b') for c in text)
    while len(binary) % block_size != 0:
        binary += '0'
    return [binary[i:i+block_size] for i in range(0, len(binary), block_size)]

# Convert binary blocks back to text
def binary_blocks_to_string(blocks):
    binary = ''.join(blocks)
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    return ''.join(chars).rstrip('\x00')

# Generate 16 pseudo-random binary keys of 8 bits each
def generate_keys(num_rounds=16, block_size=8, seed=42):
    import random
    random.seed(seed)
    return [format(random.randint(0, 2**block_size - 1), f'0{block_size}b') for _ in range(num_rounds)]

# Encrypt text using the Feistel cipher
def feistel_encrypt(text, round_keys):
    blocks = string_to_binary_blocks(text)
    encrypted_blocks = [feistel_encrypt_block(b, round_keys) for b in blocks]
    binary = ''.join(encrypted_blocks)
    byte_data = int(binary, 2).to_bytes(len(binary) // 8, byteorder='big')
    return base64.b64encode(byte_data).decode('utf-8')

# Decrypt text using the Feistel cipher
def feistel_decrypt(base64_text, round_keys):
    byte_data = base64.b64decode(base64_text)
    binary = ''.join(format(b, '08b') for b in byte_data)
    blocks = [binary[i:i+16] for i in range(0, len(binary), 16)]
    decrypted_blocks = [feistel_decrypt_block(b, round_keys) for b in blocks]
    return binary_blocks_to_string(decrypted_blocks)