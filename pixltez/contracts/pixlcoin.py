import smartpy as sp
FA2 = sp.io.import_script_from_url("https://smartpy.io/templates/fa2_lib.py")
Config = sp.io.import_script_from_url("file:./contracts/config.py")

admin = sp.address(Config.ADMIN)

class PiXLCoin(
    FA2.Admin,
    FA2.ChangeMetadata,
    FA2.WithdrawMutez,
    FA2.MintFungible,
    FA2.BurnFungible,
    FA2.OnchainviewBalanceOf,
    FA2.OffchainviewTokenMetadata,
    FA2.Fa2Fungible
):
    def __init__(self, policy=None):
            FA2.Fa2Fungible.__init__(
                self, sp.utils.metadata_of_url("ipfs://example"), policy=policy
            )
            FA2.Admin.__init__(self, admin)


sp.add_compilation_target("PiXLCoin", PiXLCoin())
