

__author__ = 'Priyatam Nayak'


class Field(object):
    def __init__(self, name, offset, length):
        self.name = name
        self.offset = offset
        self.length = length
        self.end = self.offset + length


class BasicMessageType:
    """
    This Class will validate the message if we need that in future
    """
    fields = []

    @classmethod
    def is_valid(cls, s):
        pass


class Message(BasicMessageType):
    name = 'TransactionMessage'

    client_type = Field(name='CLIENT TYPE',
                        offset=3,
                        length=4,
                        )

    client_number = Field(name='CLIENT NUMBER',
                          offset=7,
                          length=4)

    account_number = Field(name='ACCOUNT NUMBER',
                           offset=11,
                           length=4)

    sub_account_number = Field(name='SUBACCOUNT NUMBER',
                               offset=15,
                               length=4,
                               )

    product_group_code = Field(name='PRODUCT GROUP CODE',
                               offset=25,
                               length=2)

    exchange_code = Field(name='EXCHANGE CODE',
                          offset=27,
                          length=4)

    symbol = Field(name='SYMBOL',
                   offset=31,
                   length=6,
                   )

    expiration_date = Field(name='EXPIRATION DATE',
                            offset=37,
                            length=8)

    quantity_long = Field(name='QUANTITY LONG',
                          offset=52,
                          length=10)
    quantity_short = Field(name='QUANTITY SHORT',
                           offset=63,
                           length=10)

    transaction_date = Field(name='TRANSACTION DATE',
                             offset=121,
                             length=8)

    fields = [client_type,
              client_number,
              account_number,
              sub_account_number,
              product_group_code,
              exchange_code,
              symbol,
              expiration_date,
              quantity_long,
              quantity_short,
              transaction_date
              ]

    groupby_fields = [client_type,
                      client_number,
                      account_number,
                      sub_account_number,
                      product_group_code,
                      exchange_code,
                      symbol,
                      expiration_date,
                      transaction_date]


class ClientInformation:
    name = "Client_Information"
    value = [Message.client_type.name,
             Message.client_number.name,
             Message.account_number.name,
             Message.sub_account_number.name]


class ProductInformation:
    name = "Product_Information"
    value = [Message.exchange_code.name,
             Message.product_group_code.name,
             Message.symbol.name,
             Message.expiration_date.name]


class TotalTransactionAmount:
    name = "Total_Transaction_Amount"


class CsvHeader:
    value = [ClientInformation.name, ProductInformation.name, TotalTransactionAmount.name]
