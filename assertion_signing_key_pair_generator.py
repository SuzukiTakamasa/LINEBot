from jwcrypto import jwk
import json
from typing import Tuple


def key_pair_generate() -> Tuple[dict, dict]:
    key = jwk.JWK.generate(kty='RSA', alg='RS256', use='sig', size=2048)

    private_key = key.export_private()
    public_key = key.export_public()

    return private_key, public_key


if __name__ == '__main__':
    private_key, public_key = key_pair_generate()
    print("=== private key ===\n"+json.dumps(json.loads(private_key),indent=2))
    print("=== public key ===\n"+json.dumps(json.loads(public_key),indent=2))   