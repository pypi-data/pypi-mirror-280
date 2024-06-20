from filecoin_lotus.rpc_abi import RPC


class MPool:
    def __init__(self, filecoin):
        self._filecoin = filecoin
        self._provider = filecoin.provider

    def pool_push_message(self, from_address: str, to_address: str, value: float):
        """
        Push Fil transaction message to pool to broadcast
        :param from_address:
        :param to_address:
        :param value:
        :return:  transaction hash
        """
        params = [
            {
                "Version": 0,
                "To": to_address,
                "From": from_address,
                "Nonce": 0,
                "Value": self._filecoin.toAtto(value),
                "GasLimit": 0,
                "GasFeeCap": "0",
                "GasPremium": "0",
                "Method": 0,
                "Params": None,
                "CID": None
            },
            {
                "MaxFee": "0"
            }
        ]
        try:
            res = self._provider.make_request(RPC.mpool_pushMessage, params)
            return res.get("CID").get("/"), ""
        except Exception as e:
            return "", e

    def pool_get_nonce(self, from_address: str):
        """
        Get nonce of the given address
        :param from_address:
        :return:
        """
        return self._provider.make_request(RPC.mpool_getNonce, [from_address])

    def pool_push(self, signed_message: dict):
        """
        Push signed message to pool
        :param signed_message:
        :return:
        """
        return self._provider.make_request(RPC.mpool_push, [signed_message])

    def pool_push_untrusted(self, signed_message: dict):
        """
        Push signed message to pool
        :param signed_message:
        :return:
        """
        return self._provider.make_request(RPC.mpool_pushUntrusted, [signed_message])

    def pool_batch_push_untrusted(self, signed_messages: list):
        """
        Push list of signed messages to pool
        :param signed_messages:
        :return:
        """
        return self._provider.make_request(RPC.mpool_batchPushUntrusted, [signed_messages])
