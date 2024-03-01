import smartpy as sp
FA2 = sp.io.import_script_from_url("https://smartpy.io/templates/fa2_lib.py")
Config = sp.io.import_script_from_url("file:./contracts/config.py")

admin = sp.address(Config.ADMIN)

class PiXLGame(
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
                self,
                metadata=sp.utils.metadata_of_url("ipfs://example"),
                policy=policy
            )
            FA2.Admin.__init__(self, admin)

    @sp.entry_point
    def mint(self, batch):
        with sp.for_("action", batch) as action:
            with action.token.match_cases() as arg:
                with arg.match("new") as metadata:
                    token_id = sp.compute(self.data.last_token_id)
                    self.data.token_metadata[token_id] = sp.record(
                        token_id=token_id, token_info=metadata
                    )
                    self.data.supply[token_id] = action.amount
                    self.data.ledger[(action.to_, token_id)] = action.amount
                    self.data.last_token_id += 1
                with arg.match("existing") as token_id:
                    sp.verify(self.is_defined(token_id), "FA2_TOKEN_UNDEFINED")
                    self.data.supply[token_id] += action.amount
                    from_ = (action.to_, token_id)
                    self.data.ledger[from_] = (
                        self.data.ledger.get(from_, 0) + action.amount
                    )


sp.add_compilation_target("PiXLGame", PiXLGame())
