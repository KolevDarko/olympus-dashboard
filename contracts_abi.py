CUSTOM_BOND_ABI = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_customTreasury",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_principalToken",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_olympusTreasury",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_subsidyRouter",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_initialOwner",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_olympusDAO",
                "type": "address"
            },
            {
                "internalType": "uint256[]",
                "name": "_tierCeilings",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "_fees",
                "type": "uint256[]"
            },
            {
                "internalType": "bool",
                "name": "_feeInPayout",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "deposit",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "payout",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "expires",
                "type": "uint256"
            }
        ],
        "name": "BondCreated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "internalPrice",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "debtRatio",
                "type": "uint256"
            }
        ],
        "name": "BondPriceChanged",
        "type": "event"
    },
    {"anonymous": False,
     "inputs": [{"indexed": True, "internalType": "address", "name": "from", "type": "address"},

                {"indexed": True, "internalType": "address", "name": "to", "type": "address"},

                {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}],
     "name": "Transfer", "type": "event"},
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "payout",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "remaining",
                "type": "uint256"
            }
        ],
        "name": "BondRedeemed",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "initialBCV",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newBCV",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "adjustment",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "addition",
                "type": "bool"
            }
        ],
        "name": "ControlVariableAdjustment",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "adjustment",
        "outputs": [
            {
                "internalType": "bool",
                "name": "add",
                "type": "bool"
            },
            {
                "internalType": "uint256",
                "name": "rate",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "target",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "buffer",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "lastBlock",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "bondInfo",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "payout",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vesting",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "lastBlock",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "TruePricePaid",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "bondPrice",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "price_",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_olympusTreasury",
                "type": "address"
            }
        ],
        "name": "changeOlympusTreasury",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "currentDebt",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "currentOlympusFee",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "currentFee_",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "debtDecay",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "decay_",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "debtRatio",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "debtRatio_",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_amount",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_maxPrice",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "_depositor",
                "type": "address"
            }
        ],
        "name": "deposit",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_controlVariable",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_vestingTerm",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_minimumPrice",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_maxPayout",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_maxDebt",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_initialDebt",
                "type": "uint256"
            }
        ],
        "name": "initializeBond",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "lastDecay",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "maxPayout",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "paySubsidy",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "payoutSinceLastSubsidy_",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "payoutFor",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "_payout",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_fee",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_depositor",
                "type": "address"
            }
        ],
        "name": "pendingPayoutFor",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "pendingPayout_",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_depositor",
                "type": "address"
            }
        ],
        "name": "percentVestedFor",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "percentVested_",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "policy",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_depositor",
                "type": "address"
            }
        ],
        "name": "redeem",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bool",
                "name": "_addition",
                "type": "bool"
            },
            {
                "internalType": "uint256",
                "name": "_increment",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_target",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_buffer",
                "type": "uint256"
            }
        ],
        "name": "setAdjustment",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "enum CustomBond.PARAMETER",
                "name": "_parameter",
                "type": "uint8"
            },
            {
                "internalType": "uint256",
                "name": "_input",
                "type": "uint256"
            }
        ],
        "name": "setBondTerms",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "terms",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "controlVariable",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vestingTerm",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "minimumPrice",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxPayout",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxDebt",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalDebt",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalPayoutGiven",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalPrincipalBonded",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_newOwner",
                "type": "address"
            }
        ],
        "name": "transferManagment",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "TrueBondPrice",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "price_",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

CUSTOM_TREASURY_ABI = [{"inputs": [{"internalType": "address", "name": "_payoutToken", "type": "address"},
                                   {"internalType": "address", "name": "_initialOwner", "type": "address"}],
                        "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": False, "inputs": [
    {"indexed": False, "internalType": "address", "name": "bondContract", "type": "address"}],
                                                                                  "name": "BondContractDewhitelisted",
                                                                                  "type": "event"},
                       {"anonymous": False,
                                                                                                     "inputs": [{
                                                                                                         "indexed": False,
                                                                                                         "internalType": "address",
                                                                                                         "name": "bondContract",
                                                                                                         "type": "address"}],
                                                                                                     "name": "BondContractWhitelisted",
                                                                                                     "type": "event"},
                       {"anonymous": False,
                        "inputs": [{"indexed": False, "internalType": "address", "name": "token", "type": "address"},
                                   {"indexed": False, "internalType": "address", "name": "destination",
                                    "type": "address"},
                                   {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"}],
                        "name": "Withdraw", "type": "event"},
                       {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "bondContract",
                        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view",
                        "type": "function"},
                       {"inputs": [{"internalType": "address", "name": "_bondContract", "type": "address"}],
                        "name": "dewhitelistBondContract", "outputs": [], "stateMutability": "nonpayable",
                        "type": "function"}, {"inputs": [], "name": "payoutToken",
                                              "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                                              "stateMutability": "view", "type": "function"},
                       {"inputs": [], "name": "policy",
                        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                        "stateMutability": "view", "type": "function"},
                       {"inputs": [{"internalType": "uint256", "name": "_amountPayoutToken", "type": "uint256"}],
                        "name": "sendPayoutTokens", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
                       {"inputs": [{"internalType": "address", "name": "_newOwner", "type": "address"}],
                        "name": "transferManagment", "outputs": [], "stateMutability": "nonpayable",
                        "type": "function"}, {
                           "inputs": [{"internalType": "address", "name": "_principalTokenAddress", "type": "address"},
                                      {"internalType": "uint256", "name": "_amount", "type": "uint256"}],
                           "name": "valueOfToken",
                           "outputs": [{"internalType": "uint256", "name": "value_", "type": "uint256"}],
                           "stateMutability": "view", "type": "function"},
                       {"inputs": [{"internalType": "address", "name": "_bondContract", "type": "address"}],
                        "name": "whitelistBondContract", "outputs": [], "stateMutability": "nonpayable",
                        "type": "function"}, {
                           "inputs": [{"internalType": "address", "name": "_token", "type": "address"},
                                      {"internalType": "address", "name": "_destination", "type": "address"},
                                      {"internalType": "uint256", "name": "_amount", "type": "uint256"}],
                           "name": "withdraw", "outputs": [], "stateMutability": "nonpayable", "type": "function"}]

ERC20_ABI = [{"inputs":[{"internalType":"address","name":"_kph","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"credit","type":"address"},{"indexed":True,"internalType":"address","name":"job","type":"address"},{"indexed":True,"internalType":"address","name":"creditor","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"AddCredit","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"job","type":"address"},{"indexed":True,"internalType":"address","name":"liquidity","type":"address"},{"indexed":True,"internalType":"address","name":"provider","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"credit","type":"uint256"}],"name":"ApplyCredit","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"delegator","type":"address"},{"indexed":True,"internalType":"address","name":"fromDelegate","type":"address"},{"indexed":True,"internalType":"address","name":"toDelegate","type":"address"}],"name":"DelegateChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"delegate","type":"address"},{"indexed":False,"internalType":"uint256","name":"previousBalance","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"newBalance","type":"uint256"}],"name":"DelegateVotesChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"job","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"address","name":"governance","type":"address"}],"name":"JobAdded","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"job","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"address","name":"governance","type":"address"}],"name":"JobRemoved","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"keeper","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"activated","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"bond","type":"uint256"}],"name":"KeeperBonded","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"keeper","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"active","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"bond","type":"uint256"}],"name":"KeeperBonding","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"keeper","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"}],"name":"KeeperDispute","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"keeper","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"}],"name":"KeeperResolved","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"keeper","type":"address"},{"indexed":True,"internalType":"address","name":"slasher","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"slash","type":"uint256"}],"name":"KeeperSlashed","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"keeper","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"deactive","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"bond","type":"uint256"}],"name":"KeeperUnbonding","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"keeper","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"deactivated","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"bond","type":"uint256"}],"name":"KeeperUnbound","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"credit","type":"address"},{"indexed":True,"internalType":"address","name":"job","type":"address"},{"indexed":True,"internalType":"address","name":"keeper","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"KeeperWorked","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"job","type":"address"},{"indexed":True,"internalType":"address","name":"liquidity","type":"address"},{"indexed":True,"internalType":"address","name":"provider","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"credit","type":"uint256"}],"name":"RemoveJob","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"job","type":"address"},{"indexed":True,"internalType":"address","name":"liquidity","type":"address"},{"indexed":True,"internalType":"address","name":"provider","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"credit","type":"uint256"}],"name":"SubmitJob","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"job","type":"address"},{"indexed":True,"internalType":"address","name":"liquidity","type":"address"},{"indexed":True,"internalType":"address","name":"provider","type":"address"},{"indexed":False,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"credit","type":"uint256"}],"name":"UnbondJob","type":"event"},{"inputs":[],"name":"BASE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"BOND","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DELEGATION_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DOMAINSEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DOMAIN_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"KPRH","outputs":[{"internalType":"contract IKeep3rV1Helper","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"LIQUIDITYBOND","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"UNBOND","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"acceptGovernance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"bonding","type":"address"}],"name":"activate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"credit","type":"address"},{"internalType":"address","name":"job","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"addCredit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"job","type":"address"}],"name":"addCreditETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"job","type":"address"}],"name":"addJob","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"job","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"addKPRCredit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"liquidity","type":"address"},{"internalType":"address","name":"job","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"addLiquidityToJob","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"voter","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"addVotes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"provider","type":"address"},{"internalType":"address","name":"liquidity","type":"address"},{"internalType":"address","name":"job","type":"address"}],"name":"applyCreditToJob","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"liquidity","type":"address"}],"name":"approveLiquidity","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"blacklist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"bonding","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"bond","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"bondings","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"bonds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint32","name":"","type":"uint32"}],"name":"checkpoints","outputs":[{"internalType":"uint32","name":"fromBlock","type":"uint32"},{"internalType":"uint256","name":"votes","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"credits","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"}],"name":"delegate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"delegateBySig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"delegates","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"keeper","type":"address"}],"name":"dispute","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"disputes","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"firstSeen","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getCurrentVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getJobs","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getKeepers","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getPriorVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"governance","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"keeper","type":"address"},{"internalType":"address","name":"bond","type":"address"},{"internalType":"uint256","name":"minBond","type":"uint256"},{"internalType":"uint256","name":"earned","type":"uint256"},{"internalType":"uint256","name":"age","type":"uint256"}],"name":"isBondedKeeper","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"keeper","type":"address"}],"name":"isKeeper","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"keeper","type":"address"},{"internalType":"uint256","name":"minBond","type":"uint256"},{"internalType":"uint256","name":"earned","type":"uint256"},{"internalType":"uint256","name":"age","type":"uint256"}],"name":"isMinKeeper","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"jobList","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"jobProposalDelay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"jobs","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"keeperList","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"keepers","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"lastJob","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"liquidityAccepted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"liquidityAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"liquidityAmountsUnbonding","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"liquidityApplied","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"liquidityPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"liquidityProvided","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"liquidityUnbonding","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"numCheckpoints","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pairs","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"partialUnbonding","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pendingGovernance","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"pendingbonds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"credit","type":"address"},{"internalType":"address","name":"keeper","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"receipt","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"keeper","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"receiptETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"job","type":"address"}],"name":"removeJob","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"liquidity","type":"address"},{"internalType":"address","name":"job","type":"address"}],"name":"removeLiquidityFromJob","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"voter","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"removeVotes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"keeper","type":"address"}],"name":"resolve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"keeper","type":"address"}],"name":"revoke","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"liquidity","type":"address"}],"name":"revokeLiquidity","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_governance","type":"address"}],"name":"setGovernance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IKeep3rV1Helper","name":"_kprh","type":"address"}],"name":"setKeep3rHelper","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"bonded","type":"address"},{"internalType":"address","name":"keeper","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"slash","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalBonded","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"bonding","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"unbond","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"liquidity","type":"address"},{"internalType":"address","name":"job","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"unbondLiquidityFromJob","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"unbondings","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"votes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"bonding","type":"address"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"workCompleted","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"keeper","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"workReceipt","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"keeper","type":"address"}],"name":"worked","outputs":[],"stateMutability":"nonpayable","type":"function"}]