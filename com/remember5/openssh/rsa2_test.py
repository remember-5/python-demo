from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, utils
from cryptography.hazmat.primitives.serialization import load_ssh_public_key
from base64 import b64decode

def verify_ssh_signature(public_key_str: str, signature: str, data: str) -> bool:
    try:
        # 1. 加载 SSH 公钥
        public_key = load_ssh_public_key(public_key_str.encode())

        # 2. 解码 base64 签名
        signature_bytes = b64decode(signature)

        # 3. 验证签名
        public_key.verify(
            signature_bytes,
            data.encode(),
            padding.PKCS1v15(),

            utils.Prehashed(hashes.SHA256())
        )
        return True
    except Exception as e:
        print(f"验证失败: {str(e)}")
        return False

# 使用示例
ssh_public_key = """ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD2Gc22pfTo37ub5vy0KgpPPNjXJ2CszvZxjDNHoOVz1BnbVEC9JUOcRCpmy1TmsT8b9vZGoFCmYUXN8fLAqiC7QcUrPPNXLT6+nRuOHqKxjRg572r3j5f/IMqiTE+2gJhMgja80kKkdgy8ZR+YQHNZgzw5R2zdDdLjohRDh3M0QjuveAWJiqTTA/yf5xcqsmulnZBsIuDEu1aBl7Wm50um8SQEhPQtDZctuTC8+NvjGaJWzG9lTpaZeOxcg81bsZrRIA2DzWaYTWpYoK6+6ViFrBMGbTl3WNp7WalqvWnMJB9/MBFznKzFkl/w8M4F0LXGpjmYv/RvFcYgALz7FFlh"""
signature = "base64_encoded_signature"
data = "要验证的数据"

is_valid = verify_ssh_signature(ssh_public_key, signature, data)
print(f"签名验证结果: {'成功' if is_valid else '失败'}")
