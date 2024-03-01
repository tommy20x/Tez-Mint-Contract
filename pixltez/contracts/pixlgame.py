import smartpy as sp
FA2 = sp.io.import_script_from_url("https://smartpy.io/templates/fa2_lib.py")
Config = sp.io.import_script_from_url("file:./contracts/config.py")

admin = sp.address(Config.ADMIN)

class PiXLGame(
    FA2.Admin,
    FA2.ChangeMetadata,
    FA2.WithdrawMutez,
    FA2.BurnNft,
    FA2.OnchainviewBalanceOf,
    FA2.OffchainviewTokenMetadata,
    FA2.Fa2Nft
):
    def __init__(self, policy=None):
            FA2.Fa2Nft.__init__(
                self, sp.utils.metadata_of_url("ipfs://example"), policy=policy
            )
            FA2.Admin.__init__(self, admin)

    @sp.entry_point
    def mint(self, batch):
        with sp.for_("action", batch) as action:
            token_id = sp.compute(self.data.last_token_id)
            metadata = sp.record(token_id=token_id, token_info=action.metadata)
            self.data.token_metadata[token_id] = metadata
            self.data.ledger[token_id] = action.to_
            self.data.last_token_id += 1


sp.add_compilation_target("PiXLGame", PiXLGame())
