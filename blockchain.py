
import hashlib
import json
from time import time

#blockchain nesnesi olusturuldu.
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="13/Mayis/2022 tarihli hareketlilik.")

# Bir JSON nesnesinde yeni bir blok listeleme anahtar/deger ciftleri blok bilgisi oluşturuldu. Bekleyen islemlerin listesini sifirlandi ve en yeni blog zincire eklendi.

    def new_block(self, previous_hash=None):
        block = {
           'index': len(self.chain) + 1,                                                                                                                                                                                                                                                                                    
           'timestamp':  time(),                                                                                                                                                        
           'transactions':  self.pending_transactions,                                                                                                                                                                        
           'previous_hash': previous_hash or self.hash(self.chain[-1])
            
        }
      
        self.pending_transactions = []
        
        self.chain.append(block)
       
        return block
       
#En son blok için blok zincirini arandi.method kullanildi.

    @property
    def last_block(self):
        
        return self.chain[-1]

# 'Blok havuzuna' ilgili bilgileri içeren bir işlem eklendi.transaction olayi belirlendi

    def new_transaction(self, gonderen,alici, tutar):
        
        transaction = { 'gonderen': gonderen,'alici': alici,'tutar': tutar
        }
        self.pending_transactions.append(transaction) 
        
        return self.last_block['index'  ] +1
       
# bir blok alindi  diziye cevirildi, karma icin cevrildi. SHA256 şifrelemesiyle karma yapildi, sonrasında onaltilik diziye cevrildi.

    def hash(self, block):
       
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash
        
#alici gönderici kisiler ve gönderilen miktarlar belirlendi
blockchain = Blockchain()
t1 = blockchain.new_transaction("Asli", "Melis", '5 BTC')
t2 = blockchain.new_transaction("Melis", "Asli", '1 BTC')
t3 = blockchain.new_transaction("Asli", "Halil", '5 BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Melis", "Alice", '1 BTC')
t5 = blockchain.new_transaction("Alice", "Bora", '0.5 BTC')
t6 = blockchain.new_transaction("Bora", "Melis", '0.5 BTC')
blockchain.new_block(6789)

# ekrana yazdirildi
print("Blockchain: ",'\n', format(blockchain.chain), '\n') 
