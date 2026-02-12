from kyber_py.kyber.kyber import *
from kyber_py.kyber import default_parameters
from secrets import token_bytes


if __name__ == "__main__":
    kyber = Kyber(default_parameters.DEFAULT_PARAMETERS["kyber_512"])

    pk , sk = kyber._cpapke_keygen()

    m = "Kiarash"

    c = kyber._cpapke_enc(pk,
                          m.encode().ljust(32, b'\x00')
                          , token_bytes(32))

    mprime = kyber._cpapke_dec(sk, c)

    print(mprime)